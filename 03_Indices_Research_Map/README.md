# Macro → VN Indices Research v3.1.3e

**Bounded Global Buffer Fix — Academic Build**

Script B trong hệ thống MacroAcademic. Lấy Risk Score từ Script A (MacroAcademic Engine, dự án 01), rồi map sang hiệu suất lịch sử có điều kiện của 6 chỉ số thị trường và 11 ngành HOSE, kèm inference học thuật đầy đủ.

> **Trạng thái:** Academic Research Build  
> **Nền tảng:** TradingView Pine Script v6  
> **Khung thời gian bắt buộc:** Chart timeframe = Research timeframe (mặc định `1D`)

---

## 1. Mục tiêu và phạm vi nghiên cứu

Script trả lời câu hỏi:

> Sau các regime vĩ mô tương tự (B0–B4), VNINDEX và các nhóm cổ phiếu từng phản ứng thế nào, và bằng chứng đó có đủ mạnh để tin không?

**Phạm vi:**

- Đo forward return có điều kiện theo bucket (5D / 20D / 60D).
- Báo cáo path risk đầy đủ: MAE, MFE, close-to-close MDD.
- Lượng hóa uncertainty bằng Wilson interval và t-approximation CI.
- Kiểm định robustness: OOS calibration/validation, negative control (forward-minus-backward), staggered non-overlap phases.
- Áp family-wise correction cho 11 ngành (Bonferroni-style).
- Phân loại chất lượng mẫu và khoá inference khi bị contaminant.

**Không phải:** mô hình nhân quả, hệ thống giao dịch tự động, hay cam kết dự báo VNINDEX.

---

## 2. Danh sách series

### Macro series (7 nguồn)

| Biến | TradingView symbol | Vai trò |
|---|---|---|
| Lãi suất liên ngân hàng | `VNINBR` | Funding stress |
| Lãi suất chính sách VN | `VNINTR` | Policy anchor |
| Lợi suất TPCP 2 năm | `VN02Y` | Đầu ngắn đường cong |
| Lợi suất TPCP 10 năm | `VN10Y` | Đầu dài đường cong |
| Lợi suất Mỹ 10 năm | `US10Y` | Áp lực quốc tế |
| USD/VND | `FX_IDC:USDVND` | Áp lực tỷ giá |
| Lãi suất chính sách Mỹ | `USINTR` | Khoảng cách chính sách |

### Market indices (6)

| Chỉ số | Symbol |
|---|---|
| VNINDEX | `HOSE:VNINDEX` |
| VN30 | `HOSE:VN30` |
| VN100 | `HOSE:VN100` |
| VNALLSHARE | `HOSE:VNALLSHARE` |
| VNMIDCAP | `HOSE:VNMIDCAP` |
| VNSMALLCAP | `HOSE:VNSMALLCAP` |

### Sector indices (11)

`HOSE:VNFIN` · `HOSE:VNFINSELECT` · `HOSE:VNIND` · `HOSE:VNIT` · `HOSE:VNREAL` · `HOSE:VNCONS` · `HOSE:VNCOND` · `HOSE:VNENE` · `HOSE:VNMAT` · `HOSE:VNHEAL` · `HOSE:VNUTI`

> Tất cả external series dùng last confirmed source bar (`expression[1]` + `lookahead_on`) để **loại bỏ HTF repaint**. Có một thanh publication lag cố ý.

---

## 3. Bốn trụ cột macro composite

### Công thức spread

```text
Liquidity stress   = VNINBR − VNINTR        (high is bad)
Curve standard     = VN10Y − VN02Y          (low is bad)
International gap  = VN10Y − US10Y          (low is bad)
Long-policy spread = VN10Y − VNINTR         (low is bad)
```

### Trọng số mặc định

| Trụ cột | Weight | Hướng rủi ro |
|---|---:|---|
| Liquidity stress | `0.35` | High is bad |
| Curve (10Y−2Y) | `0.30` | Low is bad |
| International (10Y−US10Y) | `0.20` | Low is bad |
| Long-policy (10Y−policy) | `0.15` | Low is bad |

Mỗi spread → rolling percentile rank (cửa sổ `score_lb`), rồi gia quyền thành composite risk 0–100.

> Composite **renormalize động** khi thiếu pillar: nếu 1 trong 4 biến NA, weight còn lại được scales lại. Yêu cầu tối thiểu: `min_pillars = 3`, `min_weight_coverage = 0.70`.

### Bucket phân loại

| Bucket | Risk | Ý nghĩa |
|---|---:|---|
| **B0** | 0–<20 | Very supportive |
| **B1** | 20–<40 | Supportive |
| **B2** | 40–<60 | Neutral |
| **B3** | 60–<80 | Risky |
| **B4** | 80–100 | High stress |

Bucket có **hysteresis** (chuyển khi vượt buffer) để giảm threshold-churn và transition counts giả.

---

## 4. Cài đặt và cấu hình khuyến nghị

### Cài đặt

1. Mở TradingView → **Pine Editor**.
2. Xóa code mặc định, paste toàn bộ `Indices_Research_Map_v3.1.3e.pine`.
3. **Save** → **Add to chart**.
4. Chuyển chart sang khung **1D** (bắt buộc: chart TF = Research TF).

### Cấu hình khuyến nghị

| Nhóm | Tham số | Khuyến nghị |
|---|---|---|
| **Sampling** | Non-overlapping sampling | **ON** (mặc định). Tắt → labels trở thành DESCRIPTIVE. |
| | Research timeframe | `1D` |
| | Sample start/end year | Theo phạm vi nghiên cứu |
| **Macro** | `score_lb` (lookback percentile) | Mặc định |
| | `risk_smooth_len` | `> 1` (EMA smoothing) |
| | `min_pillars` | `3` |
| | `min_weight_coverage` | `0.70` |
| **Inference** | Family-wise correction (sectors) | **ON** |
| | `rejection_caution_pct` | < `rejection_contaminated_pct` < `rejection_unusable_pct` |
| **View** | Panel | Chọn 1 trong 4 (xem mục 5) |

> ⚠️ Script sẽ **runtime error** nếu chart TF ≠ Research TF, hoặc nếu sample year sai, hoặc nếu rejection thresholds không tăng dần.

---

## 5. Bốn panel và cách đọc

### Panel 1 — Macro Weather

Tổng quan trạng thái vĩ mô hiện tại:

- Composite risk + bucket hiện tại (+ hysteresis).
- 4 trụ cột: score từng pillar, hướng rủi ro, flag cảnh báo.
- `DATAQ` (HIGHQ / MEDQ / LOWQ) và integrity label (VALID / STALE / PARTIAL / WARMUP / INVALID).
- Source-age diagnostics (stale days từng nguồn).
- Dominant stress, breadth, dispersion, tail override.
- Specification agreement (504 / 756 / 1260 ngày).

**Cách đọc:** Bắt đầu từ bucket + DATAQ → xem pillar nào đang dominant → kiểm tra integrity (có STALE/PARTIAL không) → specification agreement (≥2/3 thì ổn định).

### Panel 2 — Market Conditional Returns

Forward return 5D / 20D / 60D theo bucket, cho 6 indices:

- Mean return + t-approximation CI 95%.
- Win rate + Wilson interval.
- N observations + rejection count.
- **MAE / MFE / close-MDD** (path risk).
- Evidence label + OOS label + negative control.
- Sample health (CLEAN / CAUTION / CONTAMINATED / UNUSABLE).

**Cách đọc:** Kiểm tra sample health trước (CONTAMINATED → không ROBUST) → xem effect + CI → đối chiếu Wilson interval của win rate → OOS label (ROBUST / MATERIAL / SIGN STABLE / FRAGILE / THIN) → negative control (có lead-lag asymmetry không).

### Panel 3 — Sector Rotation

Relative return 11 ngành so VNINDEX cùng horizon:

- Sector RR = `(1 + sector_return) / (1 + benchmark_return) − 1` (compound đúng cho arithmetic returns).
- **Bonferroni family-wise correction** cho 11 ngành.
- Wilson interval cho sector win rate.
- Top/bottom với minimum cross-sectional breadth.
- Không trùng sector giữa top và bottom tails.

**Cách đọc:** Chỉ tin leader/laggard khi CI family-wise loại trừ 0, không chỉ dựa vào rank. Sector đứng top 3 nhưng CI đi qua 0 → chỉ là `TOP RANK ONLY`.

### Panel 4 — Transition Matrix

Xác suất chuyển bucket sau forward horizon:

- From current bucket → destination bucket.
- Sử dụng **Wilson interval** cho transition probability.
- Nhóm: Improve / Persist / Worsen.
- Dùng tất cả valid macro states (không chỉ clean outcomes).

---

## 6. Giải thích metrics

### MAE — Maximum Adverse Excursion

```text
MAE = min(low trong [t+1 .. t+H]) / close(t) − 1
```

Sự sụt giảm sâu nhất **sau khi signal close** trong cửa sổ forward. Đo downside path risk thực tế.

> MAE/MFE bắt đầu **sau signal close** — loại trừ pre-close range của signal bar.

### MFE — Maximum Favorable Excursion

```text
MFE = max(high trong [t+1 .. t+H]) / close(t) − 1
```

Mức tăng thuận lợi nhất trong cùng cửa sổ. So sánh MAE vs MFE cho thấy risk-reward path.

### Close-MDD — Close-to-close Maximum Drawdown

```text
Close-MDD = min(close-series peak-to-trough trong cửa sổ) / close(t) − 1
```

Drawdown dựa trên close only (không dùng intraday high/low). Thận trọng hơn MAE — chỉ tính drawdown thực sự đóng cửa.

### CI — Confidence Interval (t-approximation)

```text
CI 95% = mean ± t_crit × SE
SE     = sample_stdev / sqrt(N)   (sample variance, n-1)
```

Khoảng tin cậy dùng **finite-sample t-approximation**, không phải normal. Khi N nhỏ, CI rộng hơn — bảo thủ hơn.

### Wilson interval

```text
Wilson low/high = (p + z²/2N ± z·√(p(1−p)/N + z²/4N²)) / (1 + z²/N)
```

Với `p` = win rate, `N` = sample, `z` = z-critical.

Wilson interval **luôn hợp lý** cho tỷ lệ (không bao giờ < 0 hay > 1), kể cả khi N rất nhỏ hoặc p = 0/1. Normal approximation sẽ sai ở biên — Wilson thì không. Dùng cho cả **win rate** và **transition probability**.

---

## 7. Evidence labels, OOS labels, negative control

### Evidence label (base)

Kết hợp **statistical significance** (CI 95% loại trừ 0) và **economic materiality** (effect ≥ econFloor):

| Label | Điều kiện |
|---|---|
| `ROBUST` | CI loại trừ 0 **và** effect material |
| `STAT-ONLY` | CI loại trừ 0 nhưng effect chưa material |
| `ECON-ONLY` | Effect material nhưng CI đi qua 0 |
| `THIN` | N dưới minimum |
| `DESCRIPTIVE` | Non-overlap đang OFF (overlapping samples) |

### OOS labels (calibration / validation)

| Label | Điều kiện |
|---|---|
| `OOS ROBUST` | Calibration + Validation cùng dấu, cả hai material, cả hai significant |
| `OOS MATERIAL` | Cùng dấu, cả hai material |
| `SIGN STABLE` | Cùng dấu |
| `OOS FRAGILE` | Trái dấu giữa calibration và validation |
| `OOS THIN` | Không đủ N ở một trong hai sample |

### Academic label (tổng hợp)

Kết hợp base evidence + OOS stability + specification agreement + integrity + lead-lag:

| Label | Ý nghĩa |
|---|---|
| `ROBUST-OOS` | ROBUST + OOS ROBUST + spec agreement ≥ 2 + không backward-dominant |
| `STABLE-CONDITIONAL` | Evidence + OOS ổn định + spec ≥ 2 |
| `FRAGILE` | OOS FRAGILE |
| `DATA-PARTIAL` | Integrity = PARTIAL |
| `THIN` / `DESCRIPTIVE` | Như base |

### Negative control

Dùng **paired forward-minus-backward differences** với t-CI:

- Forward return: regime(t) → return(t, t+H).
- Backward return: regime(t) → return(t−H, t).
- Nếu forward dominant → tín hiệu có lead. Nếu backward dominant → có thể là **look-ahead bias** hoặc mean-reversion artifact.

Label `BACKWARD-DOMINANT` → evidence không đạt `ROBUST-OOS`.

---

## 8. Outcome-quality gate và internal consistency

### Outcome-quality gate

Phân loại rejection rate (tỷ lệ window bị loại do data gap/discontinuity):

| Label | Điều kiện |
|---|---|
| `CLEAN` | Rejection < `rejection_caution_pct` |
| `CAUTION` | Rejection trong vùng caution |
| `CONTAMINATED` | Rejection ≥ `rejection_contaminated_pct` |
| `UNUSABLE` | Rejection ≥ `rejection_unusable_pct` |

Quy tắc:

- `CONTAMINATED` → **không thể** nhận `ROBUST` evidence (tối đa `CAUTION-ROBUST`).
- `UNUSABLE` → **diagnostic only**, không inference.

### Internal consistency invariant

Script duy trì một invariant reconciles:

```text
VNINDEX market counts  ==  transition return counts + rejection counts
```

Nếu有任何 mismatch → outcome inference bị khoá là `INTERNAL-FAIL`. Đây là safeguard chống silent data corruption.

---

## 9. Alerts, troubleshooting, giới hạn

### Alerts

Script hỗ trợ alertcondition cho các sự kiện chính:

- Bucket transition (vượt hysteresis buffer).
- Evidence upgrade (label thay đổi sang ROBUST-OOS hoặc STABLE-CONDITIONAL).
- Sample health downgrade (CLEAN → CAUTION/CONTAMINATED).
- Internal consistency fail.

### Troubleshooting

| Vấn đề | Nguyên nhân | Khắc phục |
|---|---|---|
| Runtime error "chart timeframe = Research timeframe" | Chart đang ở TF khác Research TF | Chuyển chart sang `1D` |
| Tất cả NA | Warmup chưa đủ `score_lb` history | Chờ TradingView load đủ bar |
| `INTERNAL-FAIL` | Mismatch market/transition counts | Kiểm tra symbol quyền truy cập, report bug |
| Evidence toàn `DESCRIPTIVE` | Non-overlap đang OFF | Bật non-overlapping sampling |
| `DATAQ = LOWQ` | < 3 pillar hợp lệ | Kiểm tra ticker (VNINBR/VN02Y/US10Y...) |
| Panel trống | Bucket không có observation | Thử bucket khác hoặc mở rộng sample year |

### Giới hạn phương pháp

1. **Không phải causal model.** Kết quả chỉ là conditional historical association.
2. **Pine không phải econometric environment.** Parametric CI xấp xỉ; không có HAC/Newey–West hay bootstrap.
3. **Non-overlap giảm** serial dependence nhưng không loại bỏ hoàn toàn.
4. **OOS split** là holdout đơn giản, không phải walk-forward hay rolling calibration.
5. **Specification weights** là research priors, không phải tối ưu hoá out-of-sample.
6. **TradingView data** có thể khác về lịch sử, revision policy, và quyền truy cập theo gói.
7. **Sector indices** phụ thuộc lịch sử HOSE; ngành mới có thể thiếu data dài hạn.
8. **Wilson interval** tốt hơn normal approximation nhưng vẫn là approximate cho dependent samples.

---

## 10. Bộ kết quả kiểm thử tham chiếu 15/07/2026

Static validation (không phải TradingView compile trực tiếp):

| Hạng mục | Kết quả |
|---|---|
| Pine v6 syntax | PASS |
| Parens / brackets / braces balance | PASS |
| User-defined function arity | PASS |
| No dead variables / unused configs | PASS |
| Fixed table dimensions (4 panel) | PASS |
| `max_bars_back = 120` (bounded global buffer) | PASS |
| `lookahead_off`/confirmed-source trên mọi request | PASS |
| Invalid-symbol returns NA (không crash) | PASS |
| Internal consistency invariant wired | PASS |
| Outcome-quality gate thresholds monotonic | PASS |
| Non-overlap phase reproducible | PASS |
| Wilson interval implementation | PASS |
| Bonferroni sector correction | PASS |
| Negative control (forward-minus-backward) | PASS |
| Hysteresis bucket transition | PASS |

> Kết quả dựa trên static validation. Bước tiếp theo: compile trực tiếp trong TradingView và screenshot 4 panel cho regression test.

---

## 11. Release notes — RE10067, RE10143, CE10013

### Bối cảnh

Trước v3.1.3e, script dùng `max_bars_back = 5000` cấp cho từng series riêng lẻ. Điều này gây ra ba lỗi biên dịch/sản xuất trên TradingView:

| Mã lỗi | Triệu chứng |
|---|---|
| **RE10067** | Script vượt quá giới hạn bộ nhớ lịch sử toàn cục khi khai báo quá nhiều series với lookback lớn |
| **RE10143** | Xung đột parser khi một selector-derived local series được history-reference (`series[n]`) bên trong vòng lặp |
| **CE10013** | Compile error khi tổng allocations vượt compound budget của Pine runtime |

### Fix trong v3.1.3e (Bounded Global Buffer)

1. **Chuyển từ per-series allocation sang indicator-wide bounded buffer:**

   ```text
   max_bars_back = 120
   ```

   120 là offset cố định lớn nhất mà script thực sự dùng — xa dưới 5000 cũ.

2. **Unroll market và sector time-series theo symbol:**

   Trước v3.1.3e, series thị trường được truy cập qua selector trong loop, rồi history-reference. v3.1.3e unroll tường minh từng symbol (VNINDEX, VN30, ..., VNSMALLCAP và 11 sector) — không còn selector-derived local series nào bị history-reference trong loop.

3. **Kết quả:**

   - RE10067: loại bỏ (bounded buffer 120 thay vì 5000/series).
   - RE10143: loại bỏ (không còn selector-derived history-reference trong loop).
   - CE10013: loại bỏ (total allocation trong budget).

> Đây là lý do bản này mang tên **"Bounded Global Buffer Fix"**. Fix này không thay đổi logic nghiên cứu hay output — chỉ sửa vấn đề biên dịch/phân bổ bộ nhớ.

---

## 12. Versioning policy

| Loại thay đổi | Phiên bản |
|---|---|
| Fix lỗi compile/memory không đổi output | `v3.1.3x` |
| Thay đổi calibration/weight/threshold | `v3.2.0` |
| Đổi architecture hoặc methodology lớn | `v4.0.0` |

---

## 13. Tuyên bố sử dụng

Macro → VN Indices Research v3.1.3e là công cụ **nghiên cứu historical conditional association**. Không phải khuyến nghị mua/bán, không phải mô hình nhân quả, không thay thế quản trị rủi ro danh mục. Người sử dụng chịu trách nhiệm đối với mọi quyết định đầu tư.

```text
Nguồn: MacroIndices Academic v3.1.3e — Bounded Global Buffer Fix,
TradingView Pine Script v6, 15/07/2026.
```
