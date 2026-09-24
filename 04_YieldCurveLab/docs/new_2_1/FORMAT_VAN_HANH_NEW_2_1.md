# VN YieldCurveLab NEW 2.1 — quy ước ảnh và bản tin trái phiếu

Ngày triển khai: 24/09/2026. Layout chính `https://www.tradingview.com/chart/pNvdqrGl/`, script riêng `VN YieldCurveLab NEW 2.1 — Bond Research`, build `20260924-02`. Chỉ sáu lợi suất TPCP 1Y, 2Y, 3Y, 5Y, 7Y, 10Y; không có nguồn liên ngân hàng hoặc chính sách. NEW 2.0 được giữ dưới dạng mã đối chứng, không nằm trên layout.

## Cổng phát hành

- Chart `TVC:VN10Y`, 1D, không Replay; đúng **một** chỉ báo NEW 2.1, bảng Báo cáo chữ Vừa; đầu vào 5P=2bp, 20P=5bp, sàn nhảy Bond=25bp. Không có lỗi Pine/dấu chấm than.
- Bảng hiện `ĐỦ ĐIỀU KIỆN BẢN TIN TRÁI PHIẾU`, ngày chốt TPCP, QA PASS hoặc PASS cú nhảy rộng được chỉ báo chấp nhận, tuổi nguồn ≤5 ngày lịch, đủ sáu cửa sổ tenor 5/20/60P, tham chiếu 252P và 756P đủ theo cổng, `TEST 58/58`; không có NA ở số liệu được đưa vào bản tin.
- Chuyển Nghiên cứu/chữ Nhỏ, mở toàn màn hình và mở rộng pane đến khi thấy đủ 37 hàng, chụp ảnh phụ. Xác nhận cửa sổ 5/10/20P có ngày, độ phủ ≥80%, không nén ô thiếu. Chuyển lại Báo cáo/chữ Vừa; mở rộng pane đến hết dòng QA và QUAN SÁT, chụp ảnh chính toàn màn hình. Hai ảnh cùng build/ngày nguồn; nếu nguồn đổi giữa hai ảnh thì chụp lại. Layout kết thúc ở Báo cáo.
- Giá trị từ **bảng đã chốt**, không dùng con số intraday của legend hay vị trí con trỏ trên quá khứ. Ngày nguồn khác ngày chụp. Nếu không qua cổng hoặc ảnh không đọc được: dừng phát hành, ghi lỗi và cách khắc phục, không mượn ảnh trước.

## Phép đọc chuẩn

| Bằng chứng trên ảnh | Cách kể đúng | Giới hạn |
|---|---|---|
| Mặt bằng 2/5/10Y, rank 252P/756P | Mức cao/thấp **tương đối trong mẫu hiện có**, Δ20P riêng là chiều thay đổi | Mức cao không đồng nghĩa đang tăng; rank không là mức lãi suất “đúng”. |
| 10Y−2Y; dốc 2–5Y và 5–10Y | Đọc dấu 10Y−2Y, độ phẳng tương đối, đoạn nào dốc hơn; số bp/năm chia theo **kỳ hạn niêm yết danh nghĩa** | Không là duration thực tế, kỳ vọng chính sách hay term premium. |
| 5Y so nội suy 2Y/10Y | Dấu dương là 5Y cao hơn đường nối 2Y/10Y; Δ20P là độ cong đổi bao nhiêu bp | Độ cong tuyệt đối dùng riêng trong chỉ số cấu trúc; không được nhầm dấu với rank. |
| Sáu Δ20P, độ rộng và phân tán | Đếm ↑/↓ chỉ kỳ hạn vượt biên 5bp; độ lệch chuẩn dân số của sáu thay đổi đo chênh lệch chuyển động | 0/6 không có nghĩa sáu số đều 0; phân tán không thay kết luận thống kê. |
| Động học 20P | Chỉ gọi cùng tăng/giảm khi cả Δmặt bằng lẫn Δ10Y−2Y đạt biên 5bp theo từng trị tuyệt đối; khác thì “chưa phân loại” | Đó là quy tắc mô tả, không là tín hiệu hay dự báo. |
| S1–S6, năm bước trước, tuổi nhãn và ngưỡng ×0,75/×1/×1,25 | Nêu trạng thái và sự nhạy ngưỡng khi giúp hiểu | Nhãn không là xác suất hay dự báo phiên sau. |
| Chỉ số cấu trúc | Nói là điểm theo quy ước, tách Δgiá trị và Δmốc so sánh khi nhắc điểm | Điểm giảm không đồng nghĩa lợi suất giảm; không dùng để khuyến nghị. |
| Lịch sử chọn đợt 5/10/20P và đối chứng các nhãn khác | Chỉ trình bày nếu có câu hỏi nghiên cứu: n, trung vị và hiệu số với nhóm **cũng được chọn theo quy tắc base ×1** | Không là nhóm đối chứng ngẫu nhiên, toàn thị trường, p-value, lợi nhuận hay xác suất. Không đưa vào bản tin thường ngày như kết luận dự báo. |

P là **bước chart 1D có độ phủ được kiểm tra**. 1bp=0,01 điểm phần trăm. Nhóm ngắn 1–2Y, trung 3–5Y, dài 7–10Y. Đợt cách >20P vẫn có thể phụ thuộc; dữ liệu lịch sử hiện có không lưu vintage và không xác minh lịch roll/benchmark từng tenor.

## Cấu trúc bản tin phổ thông

Khoảng 140–230 từ nếu có nguồn mới; ngắn hơn khi cùng ngày chốt. Chỉ 3–5 số then chốt, ưu tiên “What I See, not What I Think”.

1. `🔎 ĐIỂM CHÍNH`: hai bullet, mức/chiều riêng và độ rộng hoặc phần nào chuyển động lệch nhau.
2. `📆 DIỄN BIẾN 20 BƯỚC 1D`: ngày đầu–cuối từ ảnh; ba bullet nhóm ngắn/trung/dài; 5P chỉ khi bổ sung góc nhìn.
3. `📐 HÌNH DẠNG VÀ ĐỘ BỀN`: 1–2 bullet về 10Y−2Y, độ cong có dấu hoặc độ phân tán; trạng thái S và tuổi chỉ khi giúp đọc. Khi thay đổi <ngưỡng, ghi rõ “chưa phân loại”.
4. `👀 CẦN THEO DÕI`: một hay hai **điều kiện kiểm tra được** trong ảnh kế tiếp, không dự báo.

Cuối: `Nguồn TPCP chốt: [ngày]; ảnh: [giờ Việt Nam]. Chỉ đo lợi suất TPCP.` Không suy luận thanh khoản, lãi suất chính sách, điều hành, VNINDEX hoặc khuyến nghị. Nếu so với báo cáo trước, phải có hai ảnh có ngày nguồn; nếu ngày nguồn chưa đổi, ghi “Chưa có phiên chốt mới” và rút ngắn bản tin. Ảnh nghiên cứu và biên bản dùng để truy vết, không chép thống kê mẫu thành nhận định phổ thông không có ngữ cảnh.
