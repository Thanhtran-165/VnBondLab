# Kiểm toán học thuật VN YieldCurveLab NEW 2.1

Ngày kiểm tra: 24/09/2026. Phạm vi: mã build `20260924-02`, ảnh Báo cáo/Nghiên cứu cùng ngày, benchmark và phép tính độc lập từ sáu giá trị trên ảnh. Lịch chạy do người dùng thực hiện thủ công.

## Kết luận trong phạm vi đã kiểm tra

**Dùng được để mô tả đường cong lợi suất TPCP với giới hạn diễn giải.** Chưa có chứng cứ để chứng nhận tính đồng nhất lịch sử của từng chuỗi TVC, tính đúng đắn độc lập của giá nguồn, hay giá trị dự báo của S1–S6. `QA PASS` và `TEST 58/58` chỉ là cổng dữ liệu và fixture lập trình của chỉ báo.

| Lớp | Kiểm tra | Kết quả |
|---|---|---|
| Nguồn | Sáu `request.security` chỉ lấy TVC:VN01Y/02Y/03Y/05Y/07Y/10Y. Không còn VNINBR/VNINTR. Kiểm tra cùng ngày nguồn, giá trị hợp lệ, tuổi nguồn và cách ly bước nhảy. | Luồng mã phù hợp phạm vi chỉ TPCP; chưa có đối chiếu vendor độc lập. |
| Giá trị ngày chốt 23/09 | Từ 2Y=3,7858%, 5Y=4,3964%, 10Y=4,5813%: trung bình = 4,2545%; 10Y−2Y = 0,7955 điểm %; 5Y trừ nội suy 2Y–10Y tại tỷ trọng 5/8 và 3/8 = +31,22875 bp. | Khớp số công bố 4,2545%; 0,7955; +31,2 bp. Đây là đối chiếu số học từ ảnh, không xác minh giá gốc. |
| Hai đoạn | (5Y−2Y)×100/3 = 20,3533 bp/năm danh nghĩa; (10Y−5Y)×100/5 = 3,6980 bp/năm danh nghĩa. | Khớp 20,4 và 3,7; mẫu số là khoảng kỳ hạn niêm yết, không phải duration. |
| Phân tán và độ rộng | Sáu Δ20P hiển thị: −1,0; +0,7; −1,1; +3,5; +2,0; +2,0 bp. Độ lệch chuẩn dân số tính độc lập = 1,670745 bp; không trị nào đạt biên tuyệt đối 5 bp. | Khớp 1,7 bp và 0/6 sau làm tròn. Không suy ra sáu kỳ hạn không đổi. |
| Cửa sổ và mẫu | `f_delta` dùng hai đầu cách 5/10/20/60 bước chart 1D, yêu cầu ≥80% vị trí hợp lệ và hai đầu không thiếu; không nén ô trống. Nghiên cứu chỉ nhận đợt sau ba bước cùng nhãn; hai điểm bắt đầu đợt cùng cấu hình cách nhau >20 bước. | Có cơ chế chống thiếu dữ liệu và trùng cửa sổ; đợt cách nhau vẫn có thể cùng chịu cú sốc và không độc lập thống kê. |
| Đối chứng | Trung vị của nhãn hiện tại so với các nhãn khác, cùng quy tắc chọn đợt ở ngưỡng ×1, tính sau khi đủ chân trời. | So sánh mô tả có điều kiện; không là mẫu ngẫu nhiên, kết quả ngoài mẫu, p-value hoặc lợi thế dự báo. |

## Một lỗi diễn giải cần sửa

`confirmed` là **nhãn được xác nhận gần nhất**, chỉ cập nhật khi nhãn hiện tại giữ ít nhất ba bước. Dòng `CONFIRMED S...` trên build `20260924-02` không nói rõ tính “gần nhất”; khi nhãn hiện tại vừa đổi, người đọc có thể tưởng nhãn mới đã được xác nhận. Bản `VN_YieldCurveLab_NEW_2_1_1_DRAFT.pine` sửa riêng dòng hiển thị, phân biệt hiện tại đã xác nhận với hiện tại đang chờ. **Bản nháp chưa được biên dịch và nghiệm thu trên TradingView vì trình biên tập ngừng phản hồi sau khi dán. Không thay build vận hành bằng bản nháp.**

Đối với build đang vận hành: khi đọc trạng thái S, dùng `Sx:nP` và ba bộ ngưỡng; chỉ gọi **nhãn hiện tại đã xác nhận** nếu `n≥3` và `CONFIRMED S` trùng `Sx`. Nếu không, coi `CONFIRMED S` là nhãn cũ gần nhất. Trên ảnh nghiệm thu S1:18P và CONFIRMED S1 nên không làm sai bản tin mẫu đó.

## Ranh giới chưa kiểm chứng

- Chưa biết phương pháp TradingView/nhà cung cấp nối chuỗi qua những lần đổi trái phiếu tham chiếu, ngày quan sát đầu gốc và vintage dữ liệu. Rank 252/756P và thống kê đợt chỉ mô tả **chuỗi hiện tại trên TradingView**.
- `gaps_off` của Pine có thể lấp giá trị gần nhất vào vị trí thiếu; mã đối chiếu timestamp nguồn với ngày chart và từ chối cả nhóm sáu kỳ hạn nếu không khớp. Kiểm toán tĩnh xác nhận đường kiểm tra đó, nhưng không chứng minh mọi trường hợp dữ liệu vendor sai timestamp đều bị phát hiện.
- Không diễn giải mức lợi suất là lãi suất thực, kỳ vọng chính sách, thanh khoản liên ngân hàng hay lợi nhuận nắm giữ trái phiếu. Không diễn giải nhãn lịch sử thành xác suất tương lai.
- Ảnh ngày 24/09 đã hiển thị QA PASS, 6/6 kỳ hạn, REF 251/252 và 754/756, TEST 58/58. Đây là một lần nghiệm thu quan sát; không phải bảo đảm các lần chạy tay về sau tự đạt. Mỗi lần chạy vẫn phải kiểm tra lại cổng và ngày nguồn.

Tài liệu Pine chính thức về `request.security` xác nhận `gaps_off` điền giá trị gần nhất trên lịch sử và có thể trả giá trị đang hình thành trên realtime; `barstate.isconfirmed` xác nhận bar của chart. Tham khảo: https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/ và https://www.tradingview.com/pine-script-docs/concepts/bar-states/.
