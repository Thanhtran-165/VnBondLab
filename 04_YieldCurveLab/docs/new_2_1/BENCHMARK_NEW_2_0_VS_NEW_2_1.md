# Benchmark học thuật VN YieldCurveLab NEW 2.0 → NEW 2.1

Nghiệm thu 24/09/2026 trên layout `https://www.tradingview.com/chart/pNvdqrGl/`, TVC:VN10Y, 1D; sáu chuỗi TPCP cùng chốt 23/09/2026. So sánh hai script cùng biểu đồ trước khi bỏ pane NEW 2.0. Các chỉ tiêu là thống kê mô tả từ dữ liệu hiện có của TradingView; không có backtest ngoài mẫu, dữ liệu vintage hay kiểm định nhân quả.

| Tiêu chí | NEW 2.0 | NEW 2.1 | Kết quả nghiệm thu |
|---|---|---|---|
| Nguồn và đơn vị quan sát | 1/2/3/5/7/10Y; sáu `request.security`; P là bước chart 1D | Giữ nguyên | Cùng ngày chốt 23/09, QA PASS, tuổi 1/5 ngày. Không thêm chuỗi tiền tệ hoặc request. |
| Mặt bằng và độ dốc | 4,2545%, Δ20P +2,1bp; 10Y−2Y +0,7955 điểm %, Δ20P +1,4bp | Giữ nguyên | Trùng trên hai pane. Rank 252P 99,6 và 756P 99,9; rank dốc 14,7/100. |
| Độ cong | Độ cong tuyệt đối làm thành phần nhỏ của chỉ số tổng hợp | Thêm độ cong **có dấu** của 5Y so với nội suy danh nghĩa 2Y/10Y và Δ20P | +31,2bp, Δ20P +2,3bp; rank độ cong tuyệt đối 54,6/100. Cần nói rõ mức 5Y nằm trên đường nội suy; không diễn giải phần bù kỳ hạn. |
| Hai đoạn đường cong | Chỉ báo độ dốc 10Y−2Y | Thêm (5Y−2Y)/3 và (10Y−5Y)/5 theo kỳ hạn danh nghĩa | 2–5Y +20,4bp/năm danh nghĩa; 5–10Y +3,7bp/năm danh nghĩa. Đây không phải duration thực tế của trái phiếu. |
| Độ rộng và phân tán | Đếm số tenor vượt biên 5P/20P; dòng “nhất quán” dựa vào độ phân tán z mức | Đếm giữ nguyên, bổ sung độ lệch chuẩn dân số của **sáu Δ20P** | 20P ↓0 ↑0/6 ở biên 5bp; phân tán biến động 1,7bp. Không gắn nhãn “tất cả đi ngang”: mỗi tenor vẫn có Δ nhỏ. |
| Động học mặt bằng và chênh lệch | Δ20P hiển thị riêng | Nhãn mô tả có hướng chỉ khi cả |Δmặt bằng| và |Δ10Y−2Y| ≥ 5bp; thêm nhãn 5 bước trước | Hiện tại “chưa phân loại” vì +2,1 và +1,4bp; trạng thái S1:18P, 5 bước trước S1. Không ép thành tăng/giảm rộng. |
| Lịch sử theo đợt | Ba bộ ngưỡng, S1–S6, 5/10/20P, >20P chống chồng và độ phủ | Giữ nguyên, thêm trung vị S hiện tại so với các **nhãn khác** ở base ×1, cùng quy tắc chọn đợt | 5P: S1 n16, +0,4bp vs nhãn khác n135, +0,2bp; 10P: n16, +0,4bp vs n133, −2,4bp; 20P: n15, +1,0bp vs n137, −1,2bp. Chênh trung vị +0,2/+2,8/+2,2bp. Chỉ là đối chứng có điều kiện của mẫu được chọn; không phải lợi thế dự báo hoặc mốc toàn thị trường. |
| Kiểm tra chạy trong Pine | 53 fixture nội bộ | 58 fixture nội bộ | Biên dịch không lỗi; QA PASS và TEST 58/58 trên chart, 5/20/60P kỳ hạn 6/6, REF 251/252 và 754/756 đủ gate. Fixture kiểm tra logic lập trình, không phải 58 quan sát độc lập hay thẩm định học thuật. |
| Chụp ảnh và duy trì | Bảng báo cáo 26 hàng; nghiên cứu 33 hàng | Báo cáo 27 hàng; nghiên cứu 37 hàng | Ảnh toàn màn hình đều hiển thị hết dòng. Layout lưu riêng script NEW 2.1, tải lại chỉ một indicator và nguồn/QA còn hợp lệ. |

**Đánh giá lợi ích biên:** NEW 2.1 bổ sung thông tin thực chất về hình dạng có dấu và sự phân tán **biến động**, giải quyết cách đọc nhầm mức cao là “đang tăng” hoặc rank cấu trúc giảm là lãi suất giảm. Đối chứng lịch sử cho người nghiên cứu một mốc mô tả nội bộ nhưng không tạo thêm quan sát độc lập. Đây là cải thiện cách diễn giải bằng chứng trái phiếu, không khôi phục phạm vi tiền tệ của bản cũ.

**Trần học thuật còn lại:** TradingView không xác nhận lịch roll/đường dựng từng tenor, kỳ hạn thực tế, vintage dữ liệu hoặc tính đồng nhất lịch sử của nguồn. Sáu series và các episode có thể cùng chịu cú sốc, không độc lập. Tỷ lệ P là bước 1D có kiểm tra độ phủ, không tự đồng nghĩa phiên giao dịch TPCP. Không suy ra kỳ vọng, term premium, lợi nhuận trái phiếu, xác suất tương lai, NHNN hay chứng khoán. Muốn vượt ranh giới đó cần dữ liệu ngoài TradingView và thiết kế kiểm định khác.
