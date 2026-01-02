Dưới đây là **README + Guideline học thuật** cho **MacroAcademic – VN Economy Engine v1.2.8 (PCTL Complete)** theo đúng thói quen MacroAcademic: vừa “academic”, vừa “dịch nghĩa bình dân” để dùng được ngay trong TradingView.

---

# 1) Mục tiêu của mã

**MacroAcademic – VN Economy Engine** là một dashboard vĩ mô Việt Nam, thiết kế để trả lời nhanh 4 câu hỏi:

1. **Lạm phát đang “nóng lên / hạ nhiệt / đi ngang” không?** (P1)
2. **Lãi suất và thanh khoản đang “thắt / nới” mức nào?** (P2)
3. **Tăng trưởng đang “mở rộng / ổn định / chậm lại” không?** (P3)
4. Các yếu tố **chi phí/ngoại lực** (PPI–FX–Oil, Yield Curve) có đang “đẩy rủi ro” không? (P4–P5)

Sau đó, mã tổng hợp thành **RiskScore** và **bucket B0–B4** (P6), đồng thời có **Evaluation mini-module** để biết dự báo ổn hay “hay đổi trạng thái” (P7).

---

# 2) Kiến trúc hệ thống (TV-feasible)

## 2.1 Nguyên tắc triển khai panel trong TradingView

TradingView không cho “multi-pane thật sự” trong 1 indicator theo kiểu nhiều panel tách biệt hoàn toàn. Vì vậy kiến trúc chuẩn là:

* **1 mã nguồn**
* **7 panel**
* **7 instance** (mỗi instance chọn `Panel dang xem = 1..7`)

Đây là cách “Bloomberg-like” trong giới hạn Pine.

---

# 3) Dữ liệu & Ticker: logic và chu kỳ cập nhật

## 3.1 Các nhóm dữ liệu chính

* **Lạm phát:** `ECONOMICS:VNIRYY` (Monthly)
* **Lãi suất chính sách:** `ECONOMICS:VNINTR` (Daily → quy về Monthly)
* **Liên ngân hàng:** `ECONOMICS:VNINBR` (Daily → Monthly)
* **GDP YoY:** `ECONOMICS:VNGDPYY` (Quarterly)
* **Drivers (chi phí/ngoại lực):**

  * PPI: `ECONOMICS:VNPPI` (Quarterly)
  * FX: `FX_IDC:USDVND` (Daily → Monthly returns)
  * Oil proxy: `TVC:UKOIL` (Daily → Monthly returns)
* **Yield Curve:** `TVC:VN10Y`, `TVC:VN02Y` (Daily → Monthly)
* **BOT (tuỳ chọn):** `ECONOMICS:VNBOT` (Monthly – có thể NA tuỳ tài khoản)

## 3.2 Quy ước timeframe nội bộ

* Các phép tính cốt lõi đều “khóa” về **M** hoặc **3M** để giảm nhiễu.
* **PCTL** được cập nhật **khi sang tháng mới** (`timeframe.change("M")`).
  Vì vậy nếu chart load ít lịch sử hoặc ticker ít dữ liệu: PCTL có thể “-”.

---

# 4) Các mô hình học thuật đang dùng (đủ mạnh nhưng TV-feasible)

## 4.1 Expectation Proxy Pack (Ensemble)

Mục tiêu: tạo **E[π]** (kỳ vọng lạm phát) mà không cần survey dữ liệu.

Ensemble gồm:

1. **Trend**: EMA của CPI YoY (proxy “xu hướng dài”)
2. **EWMA**: mô hình quán tính (proxy “kỳ vọng thích nghi”)
3. **AR(1)**: kỳ vọng dựa trên tự hồi quy đơn giản (proxy “persistence”)

> Kết quả:

* **E[π]**: dự báo tháng tới (proxy)
* **Surprise = CPI – E[π]**: “lạm phát lệch kỳ vọng”

Đây là cách làm phổ biến trong nghiên cứu “expectations without surveys”: dùng mô hình thống kê tối giản để tạo expected component.

---

## 4.2 State machine cho Lạm phát (P1)

Mục tiêu: phân loại tình trạng lạm phát theo cách “đọc nhanh”.

Tín hiệu chính:

* **Gap**: CPI so với trend (nóng hơn hay lạnh hơn)
* **Momentum (dpi)**: thay đổi theo tháng
* **Surprise**: lệch so với kỳ vọng

Quy tắc (bình dân):

* Nếu tháng này tăng và cao hơn trend/du báo → **“có dấu hiệu nóng lại”**
* Nếu giảm và thấp hơn trend → **“đang hạ nhiệt”**
* Còn lại → **“đi ngang”**

---

## 4.3 Lãi suất – “thắt/nới” (P2)

Có 3 lớp:

1. **Policy rate**: mức điều hành
2. **Interbank rate**: phản ánh thanh khoản ngắn hạn
3. **Real rate proxy**: `policy – E[π]`

Ngoài ra có **Policy gap (Taylor-like)**:

* `i_implied = r* + π + φπ(π-π*) + φy(GDP gap)`
* `policy_gap = i_policy - i_implied`

Diễn giải bình dân:

* `policy_gap > 0` → chính sách đang **thắt hơn mức “hợp lý theo công thức”**
* `policy_gap < 0` → chính sách **nới hơn**

---

## 4.4 Pha kinh tế (P3)

Dùng **GDP gap** (GDP so với trend) + z-score để phân loại:

* gap dương mạnh → “mở rộng”
* gap âm mạnh → “chậm lại”
* còn lại → “ổn định”

Lưu ý học thuật: GDP theo quý nên phản ứng chậm, phải đọc cùng P1–P2.

---

## 4.5 Drivers (P4): “chi phí đẩy” tối giản

Tạo **IDI** (Inflation Driver Index) từ:

* PPI gap (chi phí sản xuất)
* FX mom (áp lực tỷ giá)
* Oil mom (năng lượng)

Tất cả đều chuẩn hoá bằng robust z-score.

Diễn giải bình dân:

* IDI cao → chi phí đầu vào/ngoại lực đang “đẩy CPI” trong vài tháng tới.

---

## 4.6 Yield Curve (P5)

Dùng slope: `VN10Y - VN02Y` và chuẩn hoá `yc_idx`.

Diễn giải bình dân:

* slope < 0 (đảo ngược) → rủi ro chu kỳ/niềm tin tăng
* slope cao bất thường → có thể là lạm phát kỳ vọng/nợ/term premium (đọc kèm P1–P4)

---

## 4.7 RiskScore (P6)

RiskScore là tổng hợp theo trọng số:

* Lam phat: `S_infl`
* Lai suat: `S_pol`
* Tang truong: `S_grow` (đảo dấu để “yếu” = rủi ro)
* Drivers: `S_drv`
* (BOT optional)

Sau đó chuyển sang **PCTL** và bucket **B0–B4**.

Ý nghĩa Bucket:

* **B0–B1:** dễ chịu / ít áp lực
* **B2:** trung tính
* **B3:** rủi ro cao (phòng thủ hơn)
* **B4:** rủi ro rất cao (ưu tiên an toàn)

---

## 4.8 Evaluation (P7)

Mục tiêu: biết mô hình có “đáng tin” không.

* **Abs error:** |CPI – E[π]|
* **MAE24 / RMSE24:** sai số trung bình (24 tháng)
* **Churn12:** số lần đổi trạng thái trong 12 tháng (proxy “regime instability”)

Diễn giải bình dân:

* MAE/RMSE cao + churn cao → tín hiệu hay “giật”, nên giảm tự tin.

---

# 5) Cột PCTL là gì? đọc thế nào?

**PCTL = percentile**: giá trị hiện tại đang ở “mấy %” của lịch sử mà script lưu.

* PCTL ~ 50: bình thường
* PCTL > 80: cao bất thường (màu nóng)
* PCTL < 20: thấp bất thường (màu lạnh)

Quan trọng:

* Với chỉ số “high is bad” (inflation pressure, tightness, risk…), PCTL cao = xấu hơn.
* Với chỉ số “high is good” (GDP strength), PCTL cao = tốt hơn.

Trong v1.2.8:

* Dòng **không phải số** → “KHONG XEP HANG”
* Dòng số mà thiếu lịch sử/ticker NA → “-” (thực sự thiếu dữ liệu)

---

# 6) Workflow dùng thử khuyến nghị (rất thực dụng)

## Bước 1: Setup 7 pane

* Add indicator 7 lần
* Mỗi lần chọn `Panel dang xem = 1..7`
* Đặt `Mode = Full` trong giai đoạn test.

## Bước 2: Dùng P1–P2 làm “core”

* P1 trả lời: CPI đang nóng lên hay hạ nhiệt?
* P2 trả lời: lãi suất/ thanh khoản đang thắt hay nới?

## Bước 3: P3–P5 để kiểm tra chéo

* GDP xác nhận pha (chậm, ổn định, mở rộng)
* Drivers báo áp lực chi phí (FX/Oil/PPI)
* YC cảnh báo chu kỳ

## Bước 4: P6 ra quyết định mức rủi ro

* B3/B4: ưu tiên phòng thủ, giảm đòn bẩy, tăng chất lượng
* B0/B1: linh hoạt hơn nhưng vẫn kiểm soát rủi ro

## Bước 5: P7 để biết “có đáng tin không”

* Nếu MAE/RMSE tăng và churn cao → giảm tự tin vào tín hiệu ngắn hạn.

---

# 7) Giới hạn học thuật (đã đạt gì / chưa đạt gì)

## Đạt tốt (TV-feasible, ~80–85% mục tiêu)

* Ensemble kỳ vọng lạm phát không cần survey
* State machine + PCTL dashboard dễ đọc
* Drivers + Yield curve làm control factors
* Evaluation module giúp chống “ảo tưởng tín hiệu”

## Chưa làm (cố ý để không vượt năng lực TradingView)

* Mô hình VAR/DSGE/Phillips curve đầy đủ
* Kalman filter / state-space ước lượng output gap
* Out-of-sample backtest theo đúng chuẩn econometrics (TV hạn chế)

---

# 8) Checklist debug nhanh (khi thấy “-”)

1. Mở DEBUG: xem `piN/ipolN/gdpN/ycN/idiN` có đang = 0 không
2. Nếu = 0 → ticker NA hoặc chart thiếu lịch sử
3. Kéo chart lùi thêm quá khứ hoặc đổi ticker tương đương

---

# 9) “Rule of thumb” giải thích cho người dùng bình thường

* **PCTL cao** ở dòng “xấu” = áp lực tăng
* **CPI nóng lại + lãi suất thắt + drivers tăng** = rủi ro tăng nhanh
* **GDP chậm + YC xấu** = ưu tiên phòng thủ
* **P7 xấu** = tin hiệu kém tin, cần chờ thêm dữ liệu

---


