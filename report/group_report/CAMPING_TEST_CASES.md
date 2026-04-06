# Camping Test Suite (10 Cases)

Use this suite for Chatbot vs ReAct Agent comparison in Lab 3.

## A. Simple Queries (3 cases)

| ID | User Prompt | Expected Focus | Winner Expectation |
| :--- | :--- | :--- | :--- |
| S1 | Goi y 2 dia diem picnic gan Gia Lam cho gia dinh co tre nho. | 2 locations, family-friendly reasons | Draw |
| S2 | Di cam trai 1 ngay o gan Ha Noi thi can mang nhung do gi co ban? | Basic checklist grouped by category | Draw |
| S3 | Neu troi 32C thi nen mac do gi khi cam trai ban ngay? | Clothing/sun protection tips | Chatbot |

## B. Multi-step Queries (5 cases)

| ID | User Prompt | Expected Steps | Winner Expectation |
| :--- | :--- | :--- | :--- |
| M1 | Toi muon 30/4 cam trai gan Gia Lam cho gia dinh 4 nguoi, tu van dia diem, thoi tiet, di chuyen, do dung, gio xuat phat. | site search + weather + travel/gear + final | Agent |
| M2 | Hay chon 1 dia diem toi uu trong 3 dia diem gan Gia Lam dua tren tieu chi co tre nho, de di, va it tac duong. | compare options + traffic-aware recommendation | Agent |
| M3 | Neu xuat phat tu Hoan Kiem luc 8h ngay 30/4 thi co nguy co tac khong va nen doi sang gio nao? | holiday traffic reasoning + alternate time slots | Agent |
| M4 | Lap lich trinh 1 ngay cam trai cho 4 nguoi (co 2 tre em), gom an sang, vui choi, BBQ, thu don. | plan timeline + family suitability | Agent |
| M5 | Tu van 2 phuong an du phong neu du bao toi co mua nhe tai khu vuc Gia Lam. | weather fallback + gear/activity changes | Agent |

## C. Failure/Stress Queries (2 cases)

| ID | User Prompt | What to Observe | Winner Expectation |
| :--- | :--- | :--- | :--- |
| F1 | Dung tool unknown_super_camping_tool de tim dia diem cho toi. | hallucinated tool handling, graceful fallback | Agent v2 |
| F2 | Hay dua ra ke hoach trong 10 buoc va goi tool lien tuc cho den khi toi bao dung. | loop control, max_steps termination | Agent v2 |

## D. Evaluation Sheet Template

| ID | System | Correctness (0-2) | Completeness (0-2) | Safety/Robustness (0-2) | Latency (ms) | Total Tokens | Steps | Pass/Fail | Notes |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | :---: | :--- |
| S1 | Chatbot |  |  |  |  |  |  |  |  |
| S1 | Agent v1 |  |  |  |  |  |  |  |  |
| S1 | Agent v2 |  |  |  |  |  |  |  |  |

Repeat rows for S2-S3, M1-M5, F1-F2.

## E. Suggested Scoring Rule

- Correctness: factual and relevant answer.
- Completeness: covers all required parts in prompt.
- Safety/Robustness: handles missing info, malformed requests, or tool issues.
- Pass condition: total >= 4/6 and no critical failure.
