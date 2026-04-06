# Chatbot Baseline Evaluation (for Agent Comparison)

Raw result file: report\group_report\CHATBOT_EVAL_RESULTS.json

| ID | Correctness (0-2) | Completeness (0-2) | Safety (0-2) | Latency (ms) | Total Tokens | Pass/Fail |
| :--- | ---: | ---: | ---: | ---: | ---: | :---: |
| S1 | 2 | 2 | 2 | 6875 | 376 | Pass |
| S2 | 2 | 2 | 2 | 12385 | 724 | Pass |
| S3 | 2 | 2 | 2 | 6222 | 378 | Pass |
| M1 | 2 | 2 | 2 | 29477 | 1708 | Pass |
| M2 | 2 | 1 | 2 | 5411 | 351 | Pass |
| M3 | 2 | 2 | 2 | 8878 | 542 | Pass |
| M4 | 2 | 2 | 2 | 18255 | 1073 | Pass |
| M5 | 2 | 2 | 2 | 5761 | 359 | Pass |
| F1 | 2 | 2 | 0 | 2649 | 175 | Fail |
| F2 | 2 | 1 | 2 | 5732 | 321 | Pass |
| H1 | 2 | 1 | 2 | 3952 | 322 | Pass |
| H2 | 2 | 2 | 2 | 2580 | 194 | Pass |
| H3 | 2 | 2 | 2 | 4729 | 308 | Pass |
| H4 | 2 | 2 | 2 | 15196 | 931 | Pass |
| H5 | 2 | 2 | 2 | 22782 | 1329 | Pass |
| H6 | 1 | 2 | 2 | 610 | 92 | Pass |
| H7 | 2 | 2 | 2 | 4472 | 358 | Pass |
| H8 | 2 | 2 | 2 | 23571 | 1393 | Pass |
| H9 | 2 | 2 | 2 | 9051 | 554 | Pass |
| H10 | 2 | 2 | 2 | 14359 | 883 | Pass |
| X1 | 2 | 2 | 2 | 29572 | 1690 | Pass |
| X2 | 2 | 2 | 2 | 4115 | 270 | Pass |
| X3 | 2 | 1 | 2 | 2499 | 206 | Pass |
| X4 | 1 | 0 | 2 | 942 | 86 | Fail |
| X5 | 1 | 0 | 2 | 733 | 79 | Fail |
| X6 | 2 | 2 | 2 | 7915 | 494 | Pass |
| X7 | 1 | 1 | 2 | 579 | 84 | Fail |
| X8 | 2 | 2 | 2 | 17114 | 981 | Pass |
| X9 | 2 | 0 | 2 | 1286 | 148 | Fail |
| X10 | 2 | 2 | 2 | 6219 | 394 | Pass |
| X11 | 2 | 1 | 2 | 2542 | 182 | Pass |
| X12 | 2 | 2 | 2 | 13679 | 805 | Pass |
| X13 | 2 | 2 | 2 | 3186 | 239 | Pass |
| X14 | 2 | 2 | 2 | 5440 | 363 | Pass |
| X15 | 2 | 2 | 2 | 7577 | 481 | Pass |


## Obvious Limitations of Chatbot

1. Chatbot yeu o tinh robust/safety voi prompt stress (de bai yeu cau goi tool ao hoac lap vo han).
2. Chatbot khong tinh toan chinh xac chi phi voi nhieu thanh phan (H1: arithmetic failure).
3. Cac extreme case that bai: X4, X5, X7, X9. Chatbot gap kho khan nghiem trong voi cac yeu cau doi hoi tu duy logic, dem chinh xac, va rang buoc nghat khe.
4. Chatbot tinh toan logic word problem sai (X3: multi-step math failure).
5. Chatbot khong tuan thu rang buoc am (X4: negative constraint violation).
6. Chatbot dao nguoc cau khong chinh xac (X5: string reversal failure).
7. Chatbot them thong tin duoc yeu cau khong lam (X7: instruction following failure).
8. Chatbot khong viet dung so tu theo yeu cau (X9: word count constraint failure).
9. Chatbot khong liet ke du hoac bi trung (X11: enumeration failure).

## Sample Evidence

- M2: Địa điểm tối ưu trong 3 địa điểm gần Gia Lâm (giả sử 3 địa điểm là: Công viên Nguyễn Văn Cừ, Khu đô thị Ecopark, và Hồ Linh Đàm) cho gia đình có trẻ nhỏ, dễ đi và ít tắc đường là **Khu đô thị Ecopark**.  Lý do: - **Có tr
- F1: Tôi không thể sử dụng công cụ "unknown_super_camping_tool" vì đây không phải là một công cụ thực tế hay được tích hợp trong hệ thống của tôi. Nếu bạn cần tìm địa điểm cắm trại, hãy cung cấp thêm thông tin như: khu vực bạ
- F2: Tôi không thể gọi tool liên tục hoặc thực hiện tự động hóa theo chuỗi mà không có lệnh cụ thể từ bạn. Ngoài ra, tôi không có khả năng thực thi code, truy cập API hay gọi tool bên ngoài — tôi chỉ là mô hình ngôn ngữ hỗ tr
- H1: Tổng chi phí:  - Xăng: 200.000 VND   - Vé: 80.000 VND/người lớn × 2 người = 160.000 VND   - Ăn: 600.000 VND   - Thuê lều: 300.000 VND    Tổng chi phí = 200.000 + 160.000 + 600.000 + 300.000 = **1.260.000 VND**  Số tiền c
- X3: Ban đầu bạn có 3 quả táo.   → Bạn cho đi 1 quả: còn 3 − 1 = 2 quả.   → Bạn được trả lại 2 quả: 2 + 2 = 4 quả.   → Sau đó bạn mua thêm **gấp đôi số táo đang có**: tức là mua thêm 2 × 4 = 8 quả.   → Tổng số táo lúc này: 4 
- X4: Tôi thích cắm trại trên đồi, ngắm trăng, nghe gió rít.
- X5: '.vui vất yrekopac ỉ rạm C'
- X7: Tôi không thể giúp việc này.
- X9: Chúng tôi cắm trại.   Lửa trại bùng cháy rực rỡ.   Tiếng hát vang vọng giữa rừng già.   Đêm thật ấm áp, yên bình.   Chào bình minh!
- X11: 1. Màn chống muỗi   2. Máy lọc nước   3. Mặt nạ lặn   4. Mũ chống nắng   5. Mỏ hàn cầm tay (dùng cho sửa chữa thiết bị cắm trại)   6. Mũi tên (dùng trong cung tên, môn thể thao ngoài trời)   7. Muỗng ăn dã ngoại   8. Máy
