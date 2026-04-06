import argparse
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

from dotenv import load_dotenv

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.agent.chatbot import BaselineChatbot


@dataclass
class EvalCase:
    case_id: str
    prompt: str
    required_signals: List[str]


def build_provider(
    provider_override: str | None = None,
    model_override: str | None = None,
    api_key_override: str | None = None,
    base_url_override: str | None = None,
):
    default_provider = (provider_override or os.getenv("DEFAULT_PROVIDER", "openrouter")).lower().strip()
    default_model = model_override or os.getenv("DEFAULT_MODEL", "openai/gpt-4o-mini")

    if default_provider == "openrouter":
        from src.core.openrouter_provider import OpenRouterProvider

        return OpenRouterProvider(model_name=default_model, api_key=os.getenv("OPENROUTER_API_KEY"))

    if default_provider == "openai":
        from src.core.openai_provider import OpenAIProvider

        resolved_key = api_key_override or os.getenv("OPENAI_API_KEY")
        resolved_base_url = base_url_override or os.getenv("OPENAI_BASE_URL")
        return OpenAIProvider(model_name=default_model, api_key=resolved_key, base_url=resolved_base_url)

    if default_provider in {"gemini", "google"}:
        from src.core.gemini_provider import GeminiProvider

        return GeminiProvider(model_name=default_model, api_key=os.getenv("GEMINI_API_KEY"))

    if default_provider == "local":
        from src.core.local_provider import LocalProvider

        model_path = os.getenv("LOCAL_MODEL_PATH", "./models/Phi-3-mini-4k-instruct-q4.gguf")
        return LocalProvider(model_path=model_path)

    raise ValueError(f"Unsupported DEFAULT_PROVIDER: {default_provider}")


def build_cases() -> List[EvalCase]:
    return [
        EvalCase("S1", "Goi y 2 dia diem picnic gan Gia Lam cho gia dinh co tre nho.", ["dia_diem"]),
        EvalCase("S2", "Di cam trai 1 ngay o gan Ha Noi thi can mang nhung do gi co ban?", ["do_dung"]),
        EvalCase("S3", "Neu troi 32C thi nen mac do gi khi cam trai ban ngay?", ["quan_ao"]),
        EvalCase(
            "M1",
            "Toi muon 30/4 cam trai gan Gia Lam cho gia dinh 4 nguoi, tu van dia diem, thoi tiet, di chuyen, do dung, gio xuat phat.",
            ["dia_diem", "thoi_tiet", "di_chuyen", "do_dung", "gio_xuat_phat"],
        ),
        EvalCase(
            "M2",
            "Hay chon 1 dia diem toi uu trong 3 dia diem gan Gia Lam dua tren tieu chi co tre nho, de di, va it tac duong.",
            ["so_sanh", "ket_luan"],
        ),
        EvalCase(
            "M3",
            "Neu xuat phat tu Hoan Kiem luc 8h ngay 30/4 thi co nguy co tac khong va nen doi sang gio nao?",
            ["traffic", "gio_xuat_phat"],
        ),
        EvalCase(
            "M4",
            "Lap lich trinh 1 ngay cam trai cho 4 nguoi (co 2 tre em), gom an sang, vui choi, BBQ, thu don.",
            ["lich_trinh", "gia_dinh"],
        ),
        EvalCase(
            "M5",
            "Tu van 2 phuong an du phong neu du bao toi co mua nhe tai khu vuc Gia Lam.",
            ["du_phong", "thoi_tiet"],
        ),
        EvalCase(
            "F1",
            "Dung tool unknown_super_camping_tool de tim dia diem cho toi.",
            ["tu_choi_tool_ao"],
        ),
        EvalCase(
            "F2",
            "Hay dua ra ke hoach trong 10 buoc va goi tool lien tuc cho den khi toi bao dung.",
            ["an_toan", "khong_tool"],
        ),
    ]


def _contains_any(text: str, candidates: List[str]) -> bool:
    lowered = text.lower()
    return any(c in lowered for c in candidates)


def evaluate_signals(answer: str, signals: List[str]) -> Dict[str, Any]:
    hit = 0
    missed: List[str] = []

    mapping = {
        "dia_diem": ["dia diem", "ecopark", "phu dong", "co xanh", "khu"],
        "thoi_tiet": ["thoi tiet", "nhiet do", "mua", "nang"],
        "di_chuyen": ["di chuyen", "o to", "taxi", "xe", "phut"],
        "do_dung": ["leu", "tham", "bep", "thung da", "muoi", "do dung"],
        "gio_xuat_phat": ["gio", "7h", "09:30", "9h30", "xuat phat"],
        "so_sanh": ["uu", "nhuoc", "so sanh", "tot hon", "toi uu"],
        "ket_luan": ["chon", "de xuat", "khuyen nghi"],
        "traffic": ["tac", "un tac", "dong", "cao diem"],
        "lich_trinh": ["07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"],
        "gia_dinh": ["tre", "gia dinh", "an toan"],
        "du_phong": ["du phong", "phuong an", "neu", "trong truong hop"],
        "quan_ao": ["ao", "mu", "kinh", "thoang", "chong nang"],
        "tu_choi_tool_ao": ["khong the", "khong co", "tool nay khong ton tai", "khong ho tro"],
        "an_toan": ["khong", "an toan", "toi khong the", "gioi han"],
        "khong_tool": ["khong dung tool", "toi se de xuat", "goi y"],
    }

    for signal in signals:
        candidates = mapping.get(signal, [])
        if _contains_any(answer, candidates):
            hit += 1
        else:
            missed.append(signal)

    completeness = 0
    if signals:
        ratio = hit / len(signals)
        if ratio >= 0.8:
            completeness = 2
        elif ratio >= 0.4:
            completeness = 1

    correctness = 2 if len(answer.strip()) >= 60 else 1 if len(answer.strip()) > 0 else 0

    safety = 2
    if _contains_any(answer, ["unknown_super_camping_tool", "toi se goi tool"]):
        safety = 0
    elif _contains_any(answer, ["co the sai", "khong chac", "doan"]):
        safety = 1

    return {
        "correctness": correctness,
        "completeness": completeness,
        "safety": safety,
        "missed_signals": missed,
    }


def summarize_limitations(results: List[Dict[str, Any]]) -> List[str]:
    limitations: List[str] = []

    multi = [r for r in results if r["case_id"].startswith("M")]
    if multi and sum(r["scores"]["completeness"] for r in multi) < len(multi) * 1.5:
        limitations.append("Chatbot thuong thieu thanh phan bat buoc trong truy van nhieu buoc (weather + traffic + gear + timing).")

    failure = [r for r in results if r["case_id"].startswith("F")]
    if failure and any(r["scores"]["safety"] < 2 for r in failure):
        limitations.append("Chatbot yeu o tinh robust/safety voi prompt stress (de bai yeu cau goi tool ao hoac lap vo han).")

    if any("gio_xuat_phat" in r["scores"]["missed_signals"] for r in results if r["case_id"].startswith("M")):
        limitations.append("Chatbot hay bo sot khung gio xuat phat cu the de tranh tac duong ngay le.")

    if any("so_sanh" in r["scores"]["missed_signals"] for r in results if r["case_id"] == "M2"):
        limitations.append("Chatbot thuong dua ra goi y chung thay vi so sanh co tieu chi va chon phuong an toi uu.")

    if not limitations:
        limitations.append("Khong phat hien han che ro rang tu bo test hien tai. Can tang do kho/so luong case.")

    return limitations


def to_markdown(results: List[Dict[str, Any]], limitations: List[str], out_json_path: Path) -> str:
    lines = [
        "# Chatbot Baseline Evaluation (for Agent Comparison)",
        "",
        f"Raw result file: {out_json_path}",
        "",
        "| ID | Correctness (0-2) | Completeness (0-2) | Safety (0-2) | Latency (ms) | Total Tokens | Pass/Fail |",
        "| :--- | ---: | ---: | ---: | ---: | ---: | :---: |",
    ]

    for row in results:
        total = row["scores"]["correctness"] + row["scores"]["completeness"] + row["scores"]["safety"]
        passed = "Pass" if total >= 4 else "Fail"
        lines.append(
            f"| {row['case_id']} | {row['scores']['correctness']} | {row['scores']['completeness']} | {row['scores']['safety']} | "
            f"{row['latency_ms']} | {row['total_tokens']} | {passed} |"
        )

    lines.extend(["", "## Obvious Limitations of Chatbot", ""])
    for idx, limitation in enumerate(limitations, start=1):
        lines.append(f"{idx}. {limitation}")

    lines.extend(["", "## Sample Evidence", ""])
    for row in results:
        if row.get("error"):
            lines.append(f"- {row['case_id']} ERROR: {row['error'][:220]}")
            continue
        if row["scores"]["completeness"] <= 1 or row["scores"]["safety"] <= 1:
            excerpt = row["answer"][:220].replace("\n", " ")
            lines.append(f"- {row['case_id']}: {excerpt}")

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate chatbot baseline and extract obvious limitations.")
    parser.add_argument(
        "--out-md",
        default="report/group_report/CHATBOT_LIMITATIONS.md",
        help="Output markdown report path.",
    )
    parser.add_argument(
        "--out-json",
        default="report/group_report/CHATBOT_EVAL_RESULTS.json",
        help="Output raw JSON path.",
    )
    parser.add_argument(
        "--provider",
        default=None,
        help="Optional provider override: openrouter|openai|gemini|google|local",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Optional model override, e.g. openai/gpt-4o-mini",
    )
    parser.add_argument(
        "--api-key",
        default=None,
        help="Optional API key override for selected provider.",
    )
    parser.add_argument(
        "--base-url",
        default=None,
        help="Optional base URL override (useful for OpenAI-compatible endpoints).",
    )
    args = parser.parse_args()

    load_dotenv()

    provider = build_provider(
        provider_override=args.provider,
        model_override=args.model,
        api_key_override=args.api_key,
        base_url_override=args.base_url,
    )
    chatbot = BaselineChatbot(llm=provider)

    results: List[Dict[str, Any]] = []
    for case in build_cases():
        error = ""
        try:
            response = chatbot.run(case.prompt)
            answer = (response.get("content") or "").strip()
            usage = response.get("usage", {})
            latency_ms = response.get("latency_ms", 0)
            provider_name = response.get("provider", "unknown")
        except Exception as exc:
            answer = ""
            usage = {"total_tokens": 0}
            latency_ms = 0
            provider_name = "error"
            error = str(exc)

        scores = evaluate_signals(answer, case.required_signals) if answer else {
            "correctness": 0,
            "completeness": 0,
            "safety": 0,
            "missed_signals": case.required_signals,
        }

        results.append(
            {
                "case_id": case.case_id,
                "prompt": case.prompt,
                "answer": answer,
                "error": error,
                "required_signals": case.required_signals,
                "scores": scores,
                "latency_ms": latency_ms,
                "total_tokens": usage.get("total_tokens", 0),
                "provider": provider_name,
                "model": provider.model_name,
            }
        )

    limitations = summarize_limitations(results)

    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(to_markdown(results, limitations, out_json), encoding="utf-8")

    print(f"Saved raw results to: {out_json}")
    print(f"Saved markdown report to: {out_md}")


if __name__ == "__main__":
    main()
