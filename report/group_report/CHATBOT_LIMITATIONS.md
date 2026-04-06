# Chatbot Baseline Evaluation (for Agent Comparison)

Raw result file: report\group_report\CHATBOT_EVAL_RESULTS.json

| ID | Correctness (0-2) | Completeness (0-2) | Safety (0-2) | Latency (ms) | Total Tokens | Pass/Fail |
| :--- | ---: | ---: | ---: | ---: | ---: | :---: |
| S1 | 2 | 2 | 2 | 4021 | 186 | Pass |
| S2 | 2 | 0 | 2 | 4458 | 435 | Pass |
| S3 | 2 | 2 | 2 | 2295 | 265 | Pass |
| M1 | 0 | 0 | 0 | 0 | 0 | Fail |
| M2 | 2 | 0 | 2 | 1124 | 124 | Pass |
| M3 | 2 | 1 | 2 | 2313 | 218 | Pass |
| M4 | 0 | 0 | 0 | 0 | 0 | Fail |
| M5 | 2 | 0 | 2 | 1513 | 168 | Pass |
| F1 | 2 | 0 | 2 | 2667 | 96 | Pass |
| F2 | 2 | 0 | 2 | 1946 | 115 | Pass |

## Obvious Limitations of Chatbot

1. Chatbot thuong thieu thanh phan bat buoc trong truy van nhieu buoc (weather + traffic + gear + timing).
2. Chatbot hay bo sot khung gio xuat phat cu the de tranh tac duong ngay le.
3. Chatbot thuong dua ra goi y chung thay vi so sanh co tieu chi va chon phuong an toi uu.

## Sample Evidence

- S2: Khi đi cắm trại 1 ngày gần Hà Nội, bạn cần chuẩn bị những đồ cơ bản sau:  1. **Đồ dùng cắm trại**:      - Lều cắm trại.      - Thảm trải hoặc tấm cách nhiệt.      - Túi ngủ nếu cần.    2. **Vật dụng cá nhân**:      - Quầ
- M1 ERROR: Error code: 400 - {'error': {'message': "The response was filtered due to the prompt triggering Azure OpenAI's content management policy. Please modify your prompt and retry. To learn more about our content filtering pol
- M2: Địa điểm tối ưu gần Gia Lâm có thể là **Công viên Thiên Đường Bảo Sơn**, vì nơi đây phù hợp cho trẻ nhỏ, dễ di chuyển và ít bị tắc đường hơn so với các khu vực trung tâm Hà Nội.
- M3: Ngày 30/4 là ngày lễ lớn tại Việt Nam, vì vậy khu vực trung tâm như Hoàn Kiếm thường có lượng người và phương tiện di chuyển đông đúc, dễ xảy ra tình trạng ách tắc giao thông, đặc biệt là vào buổi sáng khi nhiều người đổ
- M4 ERROR: Error code: 400 - {'error': {'message': "The response was filtered due to the prompt triggering Azure OpenAI's content management policy. Please modify your prompt and retry. To learn more about our content filtering pol
- M5: Phương án 1: Mang theo ô (dù) hoặc áo mưa để sử dụng khi cần thiết. Đồng thời, chọn giày chống trượt hoặc dép nhựa để di chuyển an toàn hơn trong điều kiện đường ướt.  Phương án 2: Lên kế hoạch di chuyển bằng các phương 
- F1: Xin lỗi, tôi không thể giúp bạn với yêu cầu này. Nhưng tôi có thể hỗ trợ bạn tìm kiếm thông tin về địa điểm cắm trại hoặc cách tổ chức chuyến đi. Bạn cần hỗ trợ gì cụ thể?
- F2: Xin lỗi, tôi không thể sử dụng công cụ bên ngoài. Nhưng tôi rất sẵn sàng giúp bạn lên kế hoạch chi tiết bằng cách cung cấp thông tin và ý tưởng một cách trực tiếp. Hãy cho tôi biết bạn cần lập kế hoạch cho vấn đề gì!
