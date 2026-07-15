# Macro Alert System v6.0.1

## Academic Calibration Patch — Production Research Version

**Trạng thái:** `FROZEN / ACCEPTED`  
**Ngày nghiệm thu:** 15/07/2026  
**Nền tảng:** TradingView Pine Script v6  
**Tên chỉ báo:** `Macro Alert System v6.0.1 — Academic Calibration Patch`  
**Short title:** `MacroAcademic v6.0.1`

---

## 1. Tuyên bố phiên bản chuẩn

Macro Alert System **v6.0.1** là phiên bản chuẩn được chốt để sử dụng trong các báo cáo vĩ mô, lãi suất, đường cong lợi suất và tác động có điều kiện lên thị trường cổ phiếu Việt Nam.

Phiên bản này đã:

- Compile thành công trên TradingView.
- Vận hành đầy đủ cả ba panel.
- Hoàn thành kiểm định giao diện và logic bằng dữ liệu thực tế.
- Sửa các lỗi diễn giải và hiệu chỉnh học thuật còn tồn tại ở v6.0.0.
- Được chấp nhận làm **Production Research Version**.

Không được sửa âm thầm nội dung của v6.0.1. Mọi thay đổi về công thức, trọng số, ngưỡng, nguồn dữ liệu hoặc cách phân loại phải phát hành dưới một số phiên bản mới.

---

## 2. Mục tiêu của hệ thống

Hệ thống được thiết kế để trả lời bốn câu hỏi:

1. Điều kiện funding, đường cong lợi suất và áp lực bên ngoài của Việt Nam hiện đang ở trạng thái nào?
2. Rủi ro vĩ mô tổng hợp đang thuộc bucket nào và đang tăng, giảm hay ổn định?
3. Chất lượng dữ liệu và mức độ đồng thuận giữa các lớp kinh tế có đủ để tin vào tín hiệu hay không?
4. Trong lịch sử, VNINDEX và các nhóm cổ phiếu phản ứng như thế nào sau khi bước vào regime tương tự?

Hệ thống là một **macro regime monitoring and conditional evidence dashboard**.

Hệ thống **không phải**:

- Mô hình nhân quả.
- Mô hình dự báo chính thức của SBV.
- Hệ thống định thời điểm mua bán tự động.
- Bằng chứng rằng một regime vĩ mô chắc chắn gây ra một kết quả thị trường.
- True out-of-sample forecasting engine.

---

## 3. Nguyên tắc thiết kế

v6.0.1 tách riêng năm khái niệm thường bị trộn lẫn trong các chỉ báo vĩ mô:

| Khái niệm | Ý nghĩa |
|---|---|
| **Risk level** | Mức rủi ro tổng hợp hiện tại |
| **Signal strength** | Mức độ xa trạng thái trung tính |
| **Data quality** | Mức đầy đủ của nguồn dữ liệu và component |
| **Structural confidence** | Mức đồng thuận và persistence giữa các lớp |
| **Predictive evidence** | Bằng chứng lịch sử về outcome sau regime |

Một tín hiệu cực đoan không tự động được coi là tín hiệu có độ tin cậy cao.

---

## 4. Cài đặt và sử dụng

### 4.1. Cài đặt

1. Mở TradingView.
2. Mở **Pine Editor**.
3. Dán nội dung file:

   `Macro_Alert_System_v6_0_1_Academic_Calibration_Patch.pine`

4. Chọn **Save**.
5. Chọn **Add to chart**.

### 4.2. Khung thời gian

Hệ thống sử dụng dữ liệu ngày làm chuẩn.

Có thể hiển thị trên:

- Khung intraday.
- Khung daily.

Không nên sử dụng chart tuần hoặc tháng để vận hành observation clock của mô hình.

### 4.3. Input duy nhất

Người dùng chỉ chọn một trong ba panel:

1. `Macro — Rates & Spreads`
2. `Risk — Evidence Dashboard`
3. `Equity — Regime & Rotation`

Tất cả tham số nghiên cứu còn lại được khóa để bảo đảm kết quả nhất quán giữa các lần chạy và giữa các báo cáo.

---

## 5. Nguồn dữ liệu

### 5.1. Dữ liệu vĩ mô

| Biến | TradingView symbol | Vai trò |
|---|---|---|
| Lãi suất chính sách Việt Nam | `VNINTR` | Policy anchor |
| Lợi suất TPCP Việt Nam 2 năm | `VN02Y` | Đầu ngắn đường cong |
| Lợi suất TPCP Việt Nam 10 năm | `VN10Y` | Đầu dài đường cong |
| Lợi suất Mỹ 10 năm | `US10Y` | Áp lực lợi suất quốc tế |
| Lãi suất liên ngân hàng Việt Nam | `VNINBR` | Funding conditions |
| USD/VND | `USDVND` | Áp lực tỷ giá và biến động |
| Lãi suất chính sách Mỹ | `USINTR` | Khoảng cách chính sách quốc tế |

`ignore_invalid_symbol=true` được sử dụng. Khi nguồn không hợp lệ, hệ thống trả về `na` thay vì dừng toàn bộ chỉ báo.

### 5.2. Chỉ số thị trường

- `HOSE:VNINDEX`
- `HOSE:VN30`
- `HOSE:VN100`
- `HOSE:VNALLSHARE`
- `HOSE:VNMIDCAP`
- `HOSE:VNSMALLCAP`

### 5.3. Chỉ số ngành

- `HOSE:VNFIN`
- `HOSE:VNFINSELECT`
- `HOSE:VNIND`
- `HOSE:VNIT`
- `HOSE:VNREAL`
- `HOSE:VNCONS`
- `HOSE:VNCOND`
- `HOSE:VNENE`
- `HOSE:VNMAT`
- `HOSE:VNHEAL`
- `HOSE:VNUTI`

Kết quả phụ thuộc vào lịch sử dữ liệu và quyền truy cập symbol trên TradingView.

---

## 6. Các biến vĩ mô cốt lõi

Hệ thống xây dựng bốn spread chính:

```text
Liquidity stress = VN Interbank − SBV policy rate
Yield curve       = VN10Y − VN02Y
International gap = VN10Y − US10Y
Long-policy gap   = VN10Y − SBV policy rate
```

### 6.1. Hướng rủi ro

- Liquidity stress **cao** là bất lợi.
- 10Y–2Y **thấp** là bất lợi.
- VN10Y–US10Y **thấp** là bất lợi.
- VN10Y–policy **thấp** là bất lợi.

### 6.2. Cửa sổ percentile

```text
PCTL_LB = 504 phiên
Stress threshold = percentile 85
Low-is-bad threshold = percentile 15
```

Risk percentile của từng biến được chuyển về thang 0–100.

---

## 7. Ba lớp kinh tế

### 7.1. Funding layer

```text
Funding = percentile rank của Liquidity stress
```

Đây là lớp phản ánh trực tiếp mức căng của thị trường tiền tệ ngắn hạn so với policy anchor.

### 7.2. Domestic curve layer

```text
Domestic = 60% × Curve risk
         + 40% × Long-policy-gap risk
```

Lớp này theo dõi hình dạng đường cong và khoảng cách giữa lợi suất dài hạn với lãi suất chính sách.

### 7.3. External layer

```text
External = 35% × VN–US 10Y risk
         + 25% × Fed–SBV gap risk
         + 40% × FX pressure
```

FX pressure gồm:

```text
FX pressure = 65% × VND depreciation risk
            + 35% × FX volatility risk
```

Thành phần level của tỷ giá là một chiều: chỉ USD/VND tăng, tương ứng VND mất giá, mới làm tăng áp lực.

---

## 8. Composite risk và bucket

### 8.1. Điều kiện hợp lệ

Risk chỉ được tính khi có tối thiểu:

```text
4/6 component hợp lệ
2/3 layer hợp lệ
```

Nếu không đạt, hệ thống trả về:

```text
DATA INSUFFICIENT
```

Dữ liệu thiếu không được tự động thay thế bằng trạng thái trung tính.

### 8.2. Công thức composite

```text
Risk = 40% × Funding
     + 35% × Domestic
     + 25% × External
```

### 8.3. Phân loại bucket

| Bucket | Risk score | Ý nghĩa |
|---|---:|---|
| **B0 BENIGN** | 0–<20 | Điều kiện thuận lợi |
| **B1 LOW** | 20–<40 | Rủi ro thấp |
| **B2 MID** | 40–<60 | Rủi ro trung bình |
| **B3 HIGH** | 60–<80 | Rủi ro cao |
| **B4 EXTREME** | 80–100 | Rủi ro cực đoan |

Bucket là trạng thái rủi ro tổng hợp, không phải dự báo trực tiếp lợi suất cổ phiếu.

---

## 9. Constraint Index

Constraint Index phản ánh mức độ ràng buộc lên không gian chính sách:

```text
Constraint Index = 40% × Funding
                 + 25% × Domestic
                 + 35% × External
```

| Mức | Nhãn |
|---:|---|
| ≤30 | `EASING SPACE` |
| >30 và <70 | `MODERATE CONSTRAINTS` |
| ≥70 | `HIGH CONSTRAINTS` |

Constraint Index **không phải dự báo SBV sẽ tăng, giảm hay giữ lãi suất**.

---

## 10. Signal impulse và regime language

Impulse được đo bằng thay đổi risk score trong 20 quan sát ngày:

```text
Risk impulse = Risk hiện tại − Risk 20 ngày trước
```

| Thay đổi | Nhãn |
|---:|---|
| ≥10 | `RISING FAST` |
| 4 đến <10 | `RISING` |
| >−4 đến <4 | `STABLE` |
| ≤−4 đến >−10 | `FALLING` |
| ≤−10 | `FALLING FAST` |

Regime language được viết theo hướng mô tả trạng thái quan sát được, ví dụ:

- `TIGHTENING PRESSURE RISING`
- `HIGH PRESSURE / RISING`
- `PRESSURE NORMALIZING`
- `EXTREME PRESSURE / PERSISTENT`
- `EASING PRESSURE`

Không sử dụng nhãn khẳng định vị trí trong chu kỳ như “early tightening” nếu chưa có kiểm định sequence độc lập.

---

## 11. Data Quality

Data Quality kết hợp:

```text
75% × component coverage
25% × source coverage
```

| Score | Nhãn |
|---:|---|
| ≥85 | `HIGHQ` |
| 70–<85 | `MEDQ` |
| <70 | `LOWQ` |

Data Quality chỉ phản ánh mức đầy đủ của dữ liệu, không phản ánh khả năng dự báo.

---

## 12. Structural Confidence

Structural Confidence được tính từ:

```text
45% × Concordance
35% × Persistence
20% × Data Quality
```

### 12.1. Concordance

Concordance đo mức độ đồng thuận giữa Funding, Domestic và External.

Layer càng phân kỳ, concordance càng thấp.

### 12.2. Persistence

Persistence là tỷ lệ số ngày trong năm quan sát gần nhất mà bucket lịch sử giống bucket hiện tại.

Đây là **persistence index**, không phải xác suất regime chắc chắn tiếp tục.

### 12.3. Confidence cap

Để dữ liệu đầy đủ và persistence cao không che lấp sự bất đồng giữa các layer:

```text
Concordance < 25       → Confidence tối đa 44
25 ≤ Concordance < 40 → Confidence tối đa 59
```

Khi bị giới hạn, bảng hiển thị `CAP`.

### 12.4. Nhãn confidence

| Score | Nhãn |
|---:|---|
| ≥75 | `HIGH` |
| 55–<75 | `MED` |
| <55 | `LOW` |

Confidence không bao gồm signal extremity.

---

## 13. Khung bằng chứng thị trường

### 13.1. Forward horizons

Hệ thống đánh giá ba horizon:

```text
5D, 20D và 60D
```

Các mẫu được cập nhật theo cửa sổ không chồng lấn để giảm phụ thuộc cơ học giữa các quan sát.

### 13.2. Drawdown đúng horizon

- 5D dùng rolling low 6 bars.
- 20D dùng rolling low 21 bars.
- 60D dùng rolling low 61 bars.

Cửa sổ bao gồm ngày entry và ngày evaluation.

### 13.3. Nhóm đối chứng

Outcome của regime hiện tại được so sánh với **tất cả regime còn lại**.

Hai nhóm là rời nhau:

```text
Current regime
versus
All other regimes
```

Không sử dụng unconditional mean có chứa chính current regime làm nhóm đối chứng.

### 13.4. Các thống kê được báo cáo

- Regime mean.
- Other-regime mean.
- Effect giữa hai nhóm.
- Unbiased sample variance.
- Standard error.
- Approximate Welch statistic.
- Khoảng tin cậy 95%.
- Win rate.
- Average horizon drawdown.
- Số quan sát của hai nhóm.

Các thống kê này là bằng chứng mô tả, không phải ước lượng nhân quả.

---

## 14. Structural split

Độ ổn định của effect được kiểm tra giữa:

```text
Pre-2020
2020 onward
```

| Nhãn | Ý nghĩa |
|---|---|
| `STABLE+` | Effect dương trong cả hai giai đoạn |
| `STABLE-` | Effect âm trong cả hai giai đoạn |
| `MIXED` | Hai giai đoạn khác dấu hoặc không nhất quán |
| `NA` | Không đủ mẫu |

Đây là kiểm tra robustness theo thời gian, không phải true out-of-sample test.

---

## 15. Evidence Grade

| Grade | Điều kiện |
|---|---|
| **A** | Mỗi nhóm N≥30, HIGHQ, pre/post cùng chiều và CI 95% không đi qua 0 |
| **B** | Mỗi nhóm N≥20, MEDQ trở lên, pre/post cùng chiều và CI 90% không đi qua 0 |
| **C+** | Đủ mẫu, pre/post cùng chiều, `|t| ≥ 0,75`, nhưng CI 90% vẫn đi qua 0 |
| **C** | Đủ mẫu nhưng bằng chứng yếu hoặc cấu trúc không ổn định |
| **D** | Thiếu mẫu hoặc thống kê không hợp lệ |

Trong bảng, grade được trình bày dưới dạng:

```text
EA, EB, EC+, EC, ED
```

### 15.1. Tactical Bias 20D

Chỉ Grade A hoặc B mới được phép thay đổi tactical bias:

| Điều kiện | Tactical Bias |
|---|---|
| Grade A/B và effect > 0 | `RISK-ON` |
| Grade A/B và effect < 0 | `DEFENSIVE` |
| Grade C/C+/D | `NEUTRAL` hoặc `UNKNOWN` |

Không được chuyển một point estimate chưa đủ bằng chứng thành khuyến nghị chiến thuật.

---

## 16. Phân tích thị trường và ngành

### 16.1. Thị trường

Panel Equity báo cáo outcome 20D theo bucket đối với:

- VNINDEX
- VN30
- VN100
- VNALLSHARE
- VNMIDCAP
- VNSMALLCAP

Các trường chính:

- Geometric average return.
- Standard error của log return.
- Win rate.
- Average drawdown.
- Sample size.
- N-grade.

### 16.2. Relative return ngành

Mỗi ngành được so với VNINDEX tại cùng horizon 20D:

```text
Sector RR = Sector return − VNINDEX return
```

### 16.3. Reliability shrinkage

Raw relative return được shrink về 0 bằng hệ số phụ thuộc sample size.

```text
Shrink K = 20
```

Mẫu nhỏ bị shrink mạnh hơn, hạn chế việc một ngành đứng đầu chỉ vì một số ít quan sát cực đoan.

### 16.4. Multiple-comparison guard

Hệ thống dùng:

```text
Z_SECTOR = 2,61
```

Đây là Bonferroni-style 90% family-wise uncertainty guard cho 11 ngành.

### 16.5. Nhãn ngành

| Nhãn | Điều kiện |
|---|---|
| `CONFIRMED LEADER` | Family-wise lower bound > 0 |
| `PROVISIONAL LEADER` | Shrunk RR > 0 nhưng lower bound ≤ 0 |
| `TOP RANK ONLY` | Thuộc top 3 nhưng Shrunk RR không dương |
| `CONFIRMED LAGGARD` | Family-wise upper bound < 0 |
| `PROVISIONAL LAGGARD` | Shrunk RR < 0 nhưng upper bound ≥ 0 |
| `BOTTOM RANK ONLY` | Thuộc bottom 3 nhưng Shrunk RR không âm |

Top rank không đồng nghĩa với statistically confirmed leadership.

---

## 17. Transition matrix

Transition matrix đo xác suất regime đích sau 20 ngày:

```text
From current bucket → destination bucket after 20D
```

Ba nhóm kết quả:

- `Lower risk` → Improve
- `Same risk` → Persist
- `Higher risk` → Worsen

Xác suất được làm trơn bằng Jeffreys prior:

```text
α = 0,5 cho mỗi destination state
```

Transition probabilities là xác suất regime đích, không phải xác suất VNINDEX tăng hoặc giảm.

---

## 18. Ba panel và cách đọc

### 18.1. Macro — Rates & Spreads

Dùng để trả lời:

- Lãi suất và spread hiện ở đâu?
- Thành phần nào đang phát cảnh báo?
- Funding, Domestic và External đang đồng thuận hay phân kỳ?
- Constraint zone hiện tại là gì?

Thứ tự đọc:

1. Rates.
2. Feature `Now | limit`.
3. Flags.
4. Layers.
5. Quality, confidence, strength và impulse.
6. Constraint zone.
7. Takeaway.

### 18.2. Risk — Evidence Dashboard

Dùng để trả lời:

- Composite risk và impulse hiện tại.
- Persistence và concordance.
- Confidence có bị cap hay không.
- Outcome 5D, 20D và 60D.
- Effect có đủ mạnh và ổn định hay không.
- Evidence Grade và tactical bias.

### 18.3. Equity — Regime & Rotation

Dùng để trả lời:

- Các nhóm vốn hóa phản ứng thế nào trong bucket hiện tại?
- VNINDEX có evidence khác biệt so với các regime khác hay không?
- Ngành nào đứng đầu hoặc cuối sau shrinkage?
- Leadership là confirmed, provisional hay chỉ là rank?
- Regime có xu hướng cải thiện, giữ nguyên hay xấu đi sau 20D?

---

## 19. Chuẩn viết báo cáo từ v6.0.1

Từ phiên bản này, báo cáo chuẩn phải sử dụng cấu trúc sau.

### 19.1. Phạm vi thời gian

Kể theo dòng thời gian khoảng **một tháng gần nhất**:

1. Trạng thái đầu kỳ.
2. Diễn biến đầu ngắn 1Y–2Y nếu có dữ liệu bổ sung, tối thiểu phải nêu 2Y.
3. Diễn biến trung hạn 3Y–5Y nếu có dữ liệu bổ sung.
4. Diễn biến dài hạn 7Y–10Y, tối thiểu phải nêu 10Y.
5. Interbank so với policy rate.
6. Độ dốc 10Y–2Y.
7. Sự thay đổi của funding, domestic, external và composite risk.

### 19.2. Chốt trạng thái hiện tại

Phải nêu đầy đủ:

```text
Bucket | Regime description | Data Quality | Structural Confidence
Constraint Zone | Tactical Bias | Evidence Grade
```

Mẫu takeaway chuẩn:

```text
B2 MID | TIGHTENING PRESSURE RISING | HIGHQ |
CONF MED CAP | MODERATE CONSTRAINTS | 20D NEUTRAL (EC)
```

### 19.3. Khả năng lãi suất giảm

Báo cáo phải có mục riêng:

- Khả năng giảm ở đầu ngắn.
- Khả năng giảm ở trung hạn.
- Khả năng giảm ở đầu dài.

Chỉ sử dụng mức định tính:

```text
THẤP / TRUNG BÌNH / CAO
```

Phải nêu điều kiện xác nhận kịch bản giảm, chẳng hạn:

- Interbank hạ bền vững về gần policy rate.
- Funding layer giảm rõ rệt.
- Risk impulse chuyển âm.
- Domestic curve giảm áp lực mà không do suy giảm thanh khoản nghiêm trọng.
- External layer và FX pressure không tăng ngược trở lại.

Không được gán xác suất số cho khả năng giảm lãi suất khi mô hình chưa được hiệu chỉnh xác suất.

### 19.4. Phần VNINDEX

VNINDEX chỉ là ghi chú phụ ngắn ở cuối báo cáo.

Phải phân biệt:

- Macro regime hiện tại.
- Outcome lịch sử có điều kiện.
- Mức Evidence Grade.

Không được viết “lãi suất tăng nên chứng khoán chắc chắn giảm”.

### 19.5. Độ dài

Báo cáo chuẩn gồm khoảng **5–8 đoạn ngắn**, tập trung vào câu chuyện kinh tế, không biến thành bản liệt kê toàn bộ dashboard.

---

## 20. Quy tắc ngôn ngữ và diễn giải

### Được phép

- “Funding stress đang ở vùng rất cao.”
- “Các layer chưa đồng thuận nên confidence bị giới hạn.”
- “Point estimate 60D tích cực nhưng khoảng tin cậy vẫn đi qua 0.”
- “VNREAL là provisional leader trong mẫu lịch sử hiện tại.”
- “Constraint Index cho thấy không gian chính sách đang chịu ràng buộc trung bình.”

### Không được phép

- “SBV chắc chắn sẽ tăng/giảm lãi suất.”
- “Persistence 100 nghĩa là regime chắc chắn tiếp tục.”
- “Grade C+ là có ý nghĩa thống kê.”
- “Top-ranked sector chắc chắn sẽ outperform.”
- “B4 đồng nghĩa VNINDEX sẽ giảm.”
- “Confidence cao vì tín hiệu đang cực đoan.”
- “Constraint Index là xác suất SBV hành động.”

---

## 21. Alerts

v6.0.1 có bốn cảnh báo:

1. **Extreme Risk / Calibrated Quality Confirmed**
2. **Liquidity-Curve-External Stress**
3. **Extreme Risk + Negative 20D Evidence**
4. **Positive 20D Regime Evidence**

Các alert evidence 20D chỉ kích hoạt khi Grade đạt A hoặc B.

Điều kiện quality gate:

```text
Data Quality ≥ 70
Structural Confidence ≥ 55
```

---

## 22. Giới hạn nghiên cứu

1. Dữ liệu TradingView có thể khác về độ dài lịch sử và quyền truy cập giữa các tài khoản.
2. Một số symbol vĩ mô có thể bị trễ, gián đoạn hoặc thay đổi phương pháp cung cấp.
3. Percentile regime là tương đối so với 504 phiên gần nhất, không phải ngưỡng kinh tế tuyệt đối.
4. Trọng số layer là theory-informed, chưa phải kết quả tối ưu hóa out-of-sample.
5. Approximate Welch statistic không thay thế một pipeline econometric đầy đủ.
6. Pre/post-2020 split chỉ là robustness check.
7. Non-overlapping windows giảm phụ thuộc nhưng không loại bỏ hoàn toàn serial correlation.
8. Sector family-wise guard làm giảm false positives nhưng không xử lý toàn bộ data-snooping risk.
9. Không có kiểm định nhân quả, placebo test, rolling walk-forward hoặc external holdout dataset trong Pine runtime.
10. Kết quả là bằng chứng hỗ trợ nghiên cứu, không phải khuyến nghị đầu tư cá nhân.

---

## 23. Trạng thái nghiệm thu

| Hạng mục | Kết quả |
|---|---|
| Pine v6 compile | PASS |
| Macro panel | PASS |
| Evidence dashboard | PASS |
| Equity & Rotation panel | PASS |
| Missing-data gate | PASS |
| Confidence cap | PASS |
| Exact horizon drawdown | PASS |
| Evidence Grade calibration | PASS |
| Sector evidence labels | PASS |
| Transition direction | PASS |
| Status-line cleanup | PASS |

**Phán quyết:**

```text
ACCEPTED — PRODUCTION RESEARCH VERSION
```

---

## 24. Versioning policy

### v6.0.1 được đóng băng

Không thay đổi trực tiếp:

- Data symbols.
- Lookback.
- Risk weights.
- Layer weights.
- Bucket thresholds.
- Confidence cap.
- Evidence Grade rules.
- Sector shrinkage.
- Multiple-comparison guard.
- Reporting language.

### Quy tắc phát hành tiếp theo

| Loại thay đổi | Phiên bản gợi ý |
|---|---|
| Sửa lỗi nhỏ, không đổi output nghiên cứu | `v6.0.2` |
| Thay đổi công thức hoặc calibration | `v6.1.0` |
| Thay đổi kiến trúc dữ liệu hoặc methodology lớn | `v7.0.0` |

Mọi phiên bản mới phải có:

- Changelog.
- Static QA.
- TradingView compile test.
- Screenshot nghiệm thu ba panel.
- So sánh output với v6.0.1.
- Đánh giá backward compatibility của báo cáo.

---

## 25. Tệp chính thức

```text
Macro_Alert_System_v6_0_1_Academic_Calibration_Patch.pine
CHANGELOG_v6_0_1_Academic_Calibration_Patch.md
README_Macro_Alert_System_v6_0_1.md
```

SHA-256 của Pine Script được nghiệm thu:

```text
054278fbb87168f275587d3220358518498fa24509c4ffc83c9bc33787f8d749
```

---

## 26. Quy ước sử dụng cho các báo cáo sau này

Khi không có chỉ dẫn khác, mọi báo cáo dựa trên hệ thống này phải:

1. Ghi rõ sử dụng **Macro Alert System v6.0.1**.
2. Không thay đổi ngưỡng hoặc trọng số để phù hợp với câu chuyện mong muốn.
3. Tách trạng thái macro khỏi bằng chứng dự báo thị trường.
4. Nêu Data Quality và Structural Confidence trước khi kết luận.
5. Nêu rõ confidence có bị `CAP` hay không.
6. Không nâng Grade C/C+ thành bằng chứng xác nhận.
7. Không gọi sector là leader/laggard nếu nhãn chỉ là provisional hoặc rank-only.
8. Không diễn giải Constraint Index thành dự báo chính sách SBV.
9. Không đưa xác suất số cho khả năng giảm lãi suất khi chưa hiệu chỉnh.
10. Giữ VNINDEX ở vai trò ghi chú phụ, trừ khi người dùng yêu cầu nghiên cứu equity riêng.

---

## 27. Citation text đề xuất trong báo cáo

```text
Nguồn mô hình: Macro Alert System v6.0.1 — Academic Calibration Patch,
TradingView Pine Script v6, Production Research Version, nghiệm thu 15/07/2026.
```

---

**Maintained baseline:** MacroAcademic v6.0.1  
**Status:** Frozen for reporting use
