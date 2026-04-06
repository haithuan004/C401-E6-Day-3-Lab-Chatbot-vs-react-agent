# Hallucination Stress Results

Raw result file: report\group_report\HALLUCINATION_I2_I5_RESULTS.json

| Suite | Data Fidelity | Contradiction Handling | Memory Consistency | Uncertainty Honesty | Score (/8) |
| :--- | ---: | ---: | ---: | ---: | ---: |
| I2 | 2 | 0 | 2 | 2 | 6 |
| I3 | 2 | 2 | 0 | 2 | 6 |
| I4 | 2 | 1 | 1 | 2 | 6 |
| I5 | 2 | 2 | 2 | 2 | 8 |

## Notable Fails

- I2 Turn 5: include_ok=False, exclude_ok=True | Nếu thêm ràng buộc không đi cao tốc, phương án **Công viên Thủ Lệ** vẫn khả thi. Tuy nhiên, cần xem xét lộ trình và phương tiện di chuyển. Nếu đi bằng xe máy hoặc ô tô, có thể sẽ mất nhiều thời gian hơn do đi qua các tuy
- I3 Turn 4: include_ok=False, exclude_ok=True | Để tính tổng chi phí sau khi thêm thue lều 250.000 vào tổng chi phí đã điều chỉnh (1.280.000):  1.280.000 + 250.000 = 1.530.000.  Vậy tổng chi phí sau khi thêm thue lều là 1.530.000.
- I3 Turn 5: include_ok=False, exclude_ok=True | Để chia đều tổng chi phí 1.530.000 cho 4 người, ta thực hiện phép chia:  1.530.000 ÷ 4 = 382.500.  Vậy mỗi người sẽ phải đóng góp 382.500.
- I3 Turn 7: include_ok=False, exclude_ok=True | Tổng chi phí ban đầu được tính như sau:  1. Xăng: 180.000 2. Gửi xe: 50.000 3. Vé cho 2 người lớn: 2 x 70.000 = 140.000 4. Vé cho 2 trẻ em: 2 x 30.000 = 60.000 5. Đồ ăn: 900.000  Tổng chi phí = 180.000 + 50.000 + 140.000
- I4 Turn 2: include_ok=False, exclude_ok=True | Thời tiết đẹp thường đi kèm với những yếu tố như:  1. **Nhiệt độ:** 20-25 độ C là lý tưởng. 2. **Ánh sáng mặt trời:** Có nắng nhẹ, không quá gay gắt. 3. **Độ ẩm:** 50-60% là thoải mái. 4. **Gió:** Lẽ nhẹ nhàng, tạo cảm g
- I4 Turn 6: include_ok=False, exclude_ok=True | Xin chào! Tôi luôn sẵn sàng hỗ trợ bạn. Bạn có câu hỏi gì cụ thể không?
