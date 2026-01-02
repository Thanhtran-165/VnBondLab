# VN YieldCurveLab — README (v1.6.9)

## 1) Mục tiêu & phạm vi

**VN YieldCurveLab** là một dashboard nghiên cứu đường cong lợi suất Việt Nam (1Y/2Y/3Y/5Y/7Y/10Y) + **Interbank (VNINBR)** + **Policy rate (VNINTR)**, tập trung 3 lớp:

1. **Shape/Regime**: Level–Slope–Curve và phân loại chế độ YC (YC0…YC4)
2. **Quality/Distortion**: đo “độ méo” theo dispersion của z-score các kỳ hạn → gán nhãn HIGHQ/MEDQ/LOWQ
3. **Research vs VNINDEX** (Panel 3): tương quan/cov/beta giữa **Stress** (raw/adjusted) và **log-return VNINDEX**, có:

* **EffN (effective sample)**: kiểm soát độ đủ mẫu
* **Regime filter**: nghiên cứu theo chế độ (YC4/INVERTED/Stress High…)
* **BestLag (3 lags)** + **Lag Stability**: kiểm tra độ ổn định của “lag tốt nhất”

> Script được thiết kế cho **Daily (1D)**: dữ liệu đều được `request.security(..., "D", ...)` để giảm nhiễu và đồng nhất.

---

## 2) Cấu trúc Panel

### Panel 1 — Shape Dashboard

Hiển thị:

* **LEVEL** = (2Y + 5Y + 10Y) / 3
* **SLOPE** = 10Y − 2Y
* **CURVE** = 2·5Y − 2Y − 10Y
* **YC Regime**: YC1…YC4 dựa trên percentile của Level và trạng thái Slope
* **STRESS**: chỉ số 0–100 (raw) và **Stress_ADJ** (điều chỉnh theo quality)
* **QUALITY**: HIGHQ/MEDQ/LOWQ + **MOVE FOCUS** (short/belly/long)

### Panel 2 — Grid

Bảng lưới theo kỳ hạn:

* **Z STATE**: CHEAP/FAIR/RICH (z-score robust)
* **MOVE**: UP/DN theo chênh lệch `len_change` ngày
* **STRUCT/QUAL/FOCUS**

### Panel 3 — Diagnostics + Research

* Diagnostic: stress, momentum, z-score
* Research (ALL / OKQ / FILTER):

  * **Corr** (t0) raw/adj
  * **Beta** (OLS slope x→y)
  * **R2**
  * **BestLag** trong {lag1, lag2, lag3}
  * **EffN** và **Ratio** (độ đủ mẫu)
  * **Lag Stability** (% ổn định bestlag trong `len_lag_stab` ngày)

---

## 3) Ý nghĩa các khối chính

### 3.1 Robust Z-score (winsorized)

Dùng mean/std + clip outliers để giảm ảnh hưởng điểm cực trị:

* Phù hợp khi dữ liệu yield có “spike” do lỗi/đứt chuỗi.

### 3.2 Percentile rank

Dùng `ta.percentrank` để định nghĩa LOW/MID/HIGH cho Level/Slope/Curve.
Ưu điểm: **phi tham số** (không giả định phân phối chuẩn).

### 3.3 Quality/Distortion

* Tính z-score cho 6 kỳ hạn → lấy **độ phân tán** quanh mean z-score
* Distortion cao → **LOWQ**: đường cong “méo” hoặc dữ liệu nhiễu/không đồng bộ
* **Stress_ADJ = Stress * (Quality/100)** nhằm “trừ điểm” cho giai đoạn dữ liệu kém.

### 3.4 Research vs VNINDEX

* VNINDEX return: **log return** `log(close/close[1])`
* Có tùy chọn **winsorize return** (clip theo stdev) để giảm outlier.
* Tính:

  * `corr = correlation(stress, return, len_research)`
  * `beta = cov(stress, return)/var(stress)`
  * `r2 = corr^2`
* 3 chế độ:

  * **ALL**: toàn bộ mẫu hợp lệ
  * **OKQ**: chỉ tính khi quality != LOWQ
  * **FILTER**: chỉ tính khi thỏa `reg_filter`

---

## 4) Cách sử dụng nhanh (Workflow)

1. Mở chart bất kỳ, **khuyến nghị timeframe = 1D**
2. Add indicator → chọn Panel:

   * Panel 1 để đọc regime nhanh
   * Panel 2 để xem “độ đắt/rẻ” theo kỳ hạn
   * Panel 3 để xem nghiên cứu/độ đủ mẫu
3. Nếu Panel 3 báo **VNINDEX ticker invalid/NA**:

   * đổi `VNINDEX (research)` thành đúng mã bạn dùng (thường: `HOSE:VNINDEX`)
4. Bật/tắt:

   * `Show Stress overlay`
   * `Show Stress_ADJ overlay`
   * `Event Tags` (nhãn biến cố)

---

## 5) “Academic Guideline” — Hướng dẫn học thuật & diễn giải

### A) Nguyên tắc 1: Không kết luận khi LOWQ

* Nếu **quality_label = LOWQ**, coi đó là **giai đoạn nhiễu**:

  * Stress raw có thể “đúng số” nhưng **không đáng tin để diễn giải cấu trúc**
  * Ưu tiên dùng **Stress_ADJ**, hoặc chuyển sang **OKQ research**

### B) Nguyên tắc 2: EffN ≥ ngưỡng trước khi tin Corr/Beta

* **EffN** là số quan sát hợp lệ trong cửa sổ `len_research`
* Dùng `min_eff_ratio` (mặc định 70%) để tránh “ảo giác thống kê” do thiếu dữ liệu.
* Nếu **READY = WAIT/LOW N** → chỉ xem như tín hiệu tham khảo.

### C) Nguyên tắc 3: Corr ≠ Causality

* Correlation chỉ là đồng biến/ nghịch biến, không khẳng định nguyên nhân.
* Với macro: có thể xảy ra **đảo chiều quan hệ** theo chu kỳ (regime dependence).

### D) Nguyên tắc 4: Multiple-testing risk (BestLag)

* Chọn BestLag trong 3 lag là một dạng “tối ưu hoá” → tăng rủi ro overfit.
* Vì vậy script thêm:

  * **Lag Stability**: nếu stability thấp, bestlag chỉ là nhiễu.
* Quy tắc dùng:

  * BestLag **chỉ đáng xem** khi:

    * READY = true
    * |bestCorr| đủ lớn (tự đặt chuẩn)
    * Lag Stability cao (ví dụ >60–70%)

### E) Nguyên tắc 5: Regime-conditioned inference

* Macro thường **phi tuyến**: quan hệ stress→equity khác nhau giữa YC4 vs YC1.
* Khuyến nghị:

  * So sánh **ALL vs FILTER(YC4)**, **ALL vs FILTER(STRESS_HIGH)**
  * Nếu dấu corr đổi khi đổi regime → đó là dấu hiệu **regime dependence** (quan trọng hơn một con số corr tổng).

### F) Nguyên tắc 6: Robustness checklist (tối thiểu)

Khi bạn thấy một kết luận “có vẻ đúng”, hãy check:

1. Có LOWQ không?
2. EffN đủ không?
3. Corr/beta có ổn định qua thời gian không? (đổi `len_research`)
4. Kết quả có giữ được trong OKQ không?
5. Có bị “ăn may” do lag search không? (Lag Stability)

---

## 6) Giải thích nhãn YC Regime (gợi ý diễn giải)

* **YC4**: “Tight” (level cao + slope phẳng/đảo) → thường rủi ro chu kỳ cao hơn
* **YC3**: “Late tightening” (level cao + slope dốc)
* **YC2**: “Early easing” (level thấp + slope dốc)
* **YC1**: “Easing mature” (level thấp)
* **YC0**: trung tính / mixed

> Đây là heuristic theo phân phối (percentile), không phải mô hình kinh tế cấu trúc.

---

## 7) Tham số quan trọng nên chỉnh

* `len_stats` (robust stats): 120–252 ngày tuỳ “chu kỳ” bạn muốn
* `len_research`: 120–250 ngày để nghiên cứu tương quan
* `min_eff_ratio`: 0.7–0.9 nếu bạn muốn nghiêm ngặt hơn
* `lag1/lag2/lag3`: nên đại diện **ngắn / trung / dài** (1,5,20) là hợp lý
* `len_lag_stab`: 60–120 ngày để đánh giá ổn định bestlag
* `reg_filter`: dùng để test “regime dependence”

---

## 8) Giới hạn & lưu ý của TradingView/Pine

* Pine không thuận tiện cho kiểm định thống kê nâng cao (p-value, HAC, bootstrap) với hiệu năng tốt.
* `request.security` nhiều series + bảng + labels có thể nặng. Nếu lag/đơ:

  * tắt `Event Tags`
  * tắt `Panel 2/3: show yield time-series`
  * giảm `max_labels_count` (nếu bạn custom)
* Dữ liệu TVC/tickers có thể đổi chuẩn; script đã có cảnh báo VNINDEX NA.

---

## 9) Changelog tóm tắt (v1.6.9)

* Fix các lỗi phổ biến: “end of line without line continuation”, type `na` trong function, label API
* Thêm **Stress_ADJ**
* Research: **EffN**, **Regime filter**, **BestLag**, **Lag Stability**, màu nền Corr theo strength
* Không dùng `ta.covariance` (đã tự viết cov/var TV-safe)

---

## 10) Đánh giá “đã tạm ổn chưa?”

Theo tiêu chí học thuật thực dụng trong TradingView: **đã đạt mức có thể “tạm dừng”** để sử dụng nghiên cứu/quan sát một thời gian, vì:

* Có robust + percentile (phi tham số)
* Có quality gating
* Có EffN (sample adequacy)
* Có kiểm soát overfit thô (bestlag + stability)
* Có regime-conditioned analysis

**Nâng cấp tiếp theo chỉ nên làm khi bạn đã “quan sát live” 2–4 tuần** và ghi lại: khi nào sai, sai vì ticker/quality/regime, hay do định nghĩa stress.

---

# Research Interpretation Guide (ngắn gọn để dùng hàng ngày)

1. **Xem Panel 1**: YC regime + Stress (raw/adj) + Quality
2. Nếu **LOWQ** → tránh kết luận; ưu tiên Stress_ADJ và OKQ research
3. **Panel 3**:

   * READY? EffN đủ?
   * Corr dấu gì? mạnh không?
   * BestLag có ổn định không?
4. Bật `reg_filter` (YC4 hoặc STRESS_HIGH) để xem quan hệ có “đổi chế độ” không
5. Nếu kết quả chỉ đúng ở 1 filter và lag stability thấp → coi là **nhiễu/overfit**

---


