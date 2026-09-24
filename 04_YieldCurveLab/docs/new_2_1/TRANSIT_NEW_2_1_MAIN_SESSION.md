# Bàn giao VN YieldCurveLab NEW 2.1 cho session chính

Ngày bàn giao: 24/09/2026. Bản dùng hiện tại: `VN_YieldCurveLab_NEW_2_1.pine`, build `20260924-02`, SHA-256 `0c64624faa624699d5ce6d8f4af1e1a1712e777e25265e55c45aa10e4b8b8bfe`. Mã đầy đủ 808 dòng; chỉ sáu `request.security` đến TVC:VN01Y/02Y/03Y/05Y/07Y/10Y. Layout tham chiếu: https://www.tradingview.com/chart/pNvdqrGl/ — TVC:VN10Y, 1D. **Không có lịch tự động; người dùng chạy thủ công.**

## Tình trạng phát hành

- Build `20260924-02` đã biên dịch và nghiệm thu trên ảnh ngày 24/09/2026: nguồn sáu kỳ hạn cùng chốt 23/09, QA PASS, tuổi nguồn 1/5 ngày, 5/20/60P đủ 6/6, REF 251/252 và 754/756, TEST 58/58. Ảnh Báo cáo và Nghiên cứu nằm trong gói.
- Kiểm toán tĩnh và phép tính lại độc lập xác nhận các trị số hiện trên ảnh. Chỉ số TEST là fixture logic, không là thẩm định học thuật hay kiểm chứng nhà cung cấp.
- Có bản `UNVERIFIED/VN_YieldCurveLab_NEW_2_1_1_DRAFT.pine` chỉ sửa chữ `CONFIRMED S` dễ hiểu nhầm. Bản này **chưa biên dịch/nghiệm thu TradingView** do trình biên tập ngừng phản hồi; không thay thế build chính cho đến khi thử lại và so ảnh.
- Không khẳng định trạng thái layout hiện tại sau lần dán bản nháp vào Pine Editor chưa có phản hồi. Trước lần chạy tay tiếp theo, kiểm tra trực tiếp build hiển thị, chỉ một chỉ báo, QA và ngày nguồn. Nếu layout hiển thị build `20260924-03`, phải biên dịch/nghiệm thu nó hoặc khôi phục build `20260924-02`.

## NEW 2.0 → NEW 2.1: phần giữ và phần nâng cấp

| Hạng mục | NEW 2.1 thực hiện | Diễn giải được phép |
|---|---|---|
| Lõi sáu kỳ hạn, cổng QA, rank, độ dốc, ba nhóm kỳ hạn, trạng thái S1–S6, nghiên cứu đợt 5/10/20P | Giữ từ NEW 2.0; không gọi dữ liệu tiền tệ | Mô tả mức và thay đổi lợi suất TPCP trong mẫu hiện có. |
| Độ cong 5Y có dấu | `100 × [y5 − (0,625×y2 + 0,375×y10)]` bp; thêm Δ20P | Dương nghĩa 5Y cao hơn nội suy tuyến tính 2Y–10Y; khác rank độ cong tuyệt đối. |
| Độ dốc từng đoạn | `100×(y5−y2)/3` và `100×(y10−y5)/5`, bp/năm kỳ hạn danh nghĩa | Nêu đoạn nào dốc hơn; không là duration hay phần bù kỳ hạn. |
| Độ phân tán của sáu Δ20P | Độ lệch chuẩn dân số của sáu thay đổi khi cả sáu hợp lệ | Mức khác nhau của chuyển động theo kỳ hạn; 0/6 kỳ hạn vượt biên không nghĩa các Δ đều bằng 0. |
| Động học level/slope | Chỉ phân loại có hướng khi cả hai trị tuyệt đối Δlevel và Δ(10Y−2Y) ≥ biên 20P | Không ép gán nhãn khi biến động nhỏ. |
| Đối chứng nhãn lịch sử | Trung vị đợt của nhãn hiện tại so với các nhãn khác, cùng quy tắc chọn đợt ở ngưỡng ×1 và chân trời 5/10/20P | So sánh mô tả có điều kiện, không là thử nghiệm ngoài mẫu, xác suất, p-value hay dự báo. |

Ảnh chốt 23/09: mặt bằng 4,2545%; 10Y−2Y +0,7955 điểm %; độ cong 5Y +31,2 bp; dốc đoạn 2–5Y +20,4 và 5–10Y +3,7 bp/năm kỳ hạn danh nghĩa; độ phân tán Δ20P 1,7 bp; 0/6 kỳ hạn vượt biên 5 bp. Các trị số này chỉ là mốc đối chiếu ảnh nghiệm thu, **không mang sang ngày nguồn mới**.

## Quy tắc dùng thủ công

1. Mở layout, xác nhận TVC:VN10Y, 1D, không Replay, đúng một chỉ báo, build `20260924-02`, đầu vào 5P=2bp, 20P=5bp, sàn nhảy=25bp.
2. Chỉ viết bản tin khi ảnh Báo cáo có `ĐỦ ĐIỀU KIỆN BẢN TIN TRÁI PHIẾU`, QA PASS hoặc PASS cú nhảy rộng hợp lệ, tuổi ≤5 ngày, 6/6 cửa sổ kỳ hạn, đủ tham chiếu, TEST 58/58 và không NA ở số được trích.
3. Kiểm tra ảnh Nghiên cứu đủ 37 hàng và coverage từng cửa sổ ≥80%; trở lại Báo cáo và chụp đủ dòng QA/QUAN SÁT. Ghi riêng ngày nguồn với ngày chạy. Nếu nguồn chưa có ngày mới, ghi rõ và rút ngắn bản tin.
4. Với build hiện tại, dòng `CONFIRMED Sx` chỉ là **xác nhận gần nhất**. Chỉ gọi trạng thái hiện tại đã xác nhận nếu `Sx:nP` có n≥3 và `CONFIRMED Sx` trùng nhãn hiện tại. Không suy từ đường cong sang thanh khoản, chính sách, lãi suất thực hoặc lợi nhuận trái phiếu.

## Ranh giới học thuật và bước sau

- Chưa xác minh phương pháp nối chuỗi TVC qua thời gian, lịch thay trái phiếu đại diện, vintage và độ đồng nhất lịch sử. Rank 252/756P và các đợt thuộc chuỗi TradingView hiện có.
- Chưa có kiểm định ngoài mẫu hoặc nguồn độc lập. Các nhãn S không là công cụ dự báo. Nếu nghiên cứu sâu thêm, ưu tiên kiểm tra nguồn/chỉ số benchmark và thiết kế đánh giá ngoài mẫu có câu hỏi định trước; thêm nhiều biến biến đổi từ sáu chuỗi sẽ có lợi ích biên thấp.
- Bản nháp sửa nhãn cần biên dịch, đối chiếu kết quả với build `20260924-02`, chụp lại cả hai chế độ và cập nhật prompt/format nếu chính thức nhận build `20260924-03`.

## Tệp trong gói

- `VN_YieldCurveLab_NEW_2_1.pine`: **mã Pine hoàn chỉnh đã nghiệm thu**, bản duy nhất dùng để vận hành hiện tại.
- `BENCHMARK_NEW_2_0_VS_NEW_2_1.md`: thay đổi và trị số đối chiếu.
- `KIEM_TOAN_HOC_THUAT_NEW_2_1_2026-09-24.md`: phép tính lại, lỗi diễn giải, giới hạn.
- `FORMAT_VAN_HANH_NEW_2_1.md`: cách đọc ảnh và khuôn bản tin.
- `MAU_BAN_TIN_NEW_2_1_2026-09-24.txt`: mẫu từ ảnh nghiệm thu, không là số mới.
- `BAO_CAO_2026-09-24.jpg`, `NGHIEN_CUU_2026-09-24.jpg`: hai ảnh bằng chứng.
- `UNVERIFIED/VN_YieldCurveLab_NEW_2_1_1_DRAFT.pine`: nháp sửa chữ, chưa vận hành.

## Đoạn gửi session chính

> Tiếp nhận gói VN YieldCurveLab NEW 2.1. Dùng `VN_YieldCurveLab_NEW_2_1.pine` build `20260924-02` làm mã đã nghiệm thu. Đọc `TRANSIT_NEW_2_1_MAIN_SESSION.md`, benchmark, kiểm toán và hai ảnh. Tôi tự vận hành thủ công, không tạo automation. Hãy giữ phạm vi nghiên cứu lợi suất TPCP; kiểm tra cổng dữ liệu và ngày nguồn mỗi lần chạy. File trong `UNVERIFIED/` chỉ là bản nháp sửa nhãn, chưa được nghiệm thu trên TradingView. Khi có đề xuất nâng cấp, ưu tiên chứng cứ và phép kiểm tra có thêm giá trị học thuật; không tăng số chỉ tiêu chỉ vì còn dư chỗ trong Pine.
