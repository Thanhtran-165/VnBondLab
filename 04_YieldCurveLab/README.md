# VN YieldCurveLab v2.3.0

**Horizon Separation & Sample Power**

VN YieldCurveLab là chỉ báo nghiên cứu vĩ mô trên TradingView, được thiết kế để theo dõi trạng thái đường cong lợi suất Việt Nam và kiểm định mối quan hệ giữa các regime lãi suất với outcome của VNINDEX.

Phiên bản **v2.3.0** là bản tái thiết kế hoàn chỉnh theo hướng:

- tách **Macro State** khỏi **Predictive Evidence**;
- tách riêng horizon **Tactical 1W** và **Strategic 4W**;
- sử dụng outcome không chồng lấn;
- kiểm định Development/Validation;
- lấy mẫu theo episode để hạn chế pseudo-replication;
- chỉ phát directional bias khi toàn bộ hard gate được vượt qua.

> **Trạng thái phát hành:** Research Release Candidate / Production Monitoring Ready  
> **Không phải:** hệ thống giao dịch tự động, mô hình nhân quả hoặc cam kết dự báo VNINDEX。

---

## 1. Mục tiêu

VN YieldCurveLab trả lời bốn câu hỏi riêng biệt:

1. Đường cong lợi suất Việt Nam hiện đang ở trạng thái nào?
2. Mức độ stress hiện tại cao hay thấp so với lịch sử?
3. Sau các regime tương tự, VNINDEX từng phản ứng thế nào ở horizon 1 tuần và 4 tuần?
4. Bằng chứng hiện tại có đủ mạnh để hình thành Tactical Bias hoặc Strategic bias hay không?

Chỉ báo chủ động cho phép kết quả:

```text
NO SIGNAL
NEUTRAL
INCONCLUSIVE
EPISODE N LOW
```

Đây không phải lỗi. Đó là output hợp lệ khi dữ liệu chưa đủ để chứng minh directional edge.

---

## 2. Thành phần dữ liệu

### Yield curve

| Kỳ hạn | TradingView symbol |
|---|---|
| 1Y | `TVC:VN01Y` |
| 2Y | `TVC:VN02Y` |
| 3Y | `TVC:VN03Y` |
| 5Y | `TVC:VN05Y` |
| 7Y | `TVC:VN07Y` |
| 10Y | `TVC:VN10Y` |

### Thanh khoản và chính sách

| Biến | Symbol |
|---|---|
| Interbank rate | `VNINBR` |
| Policy rate | `VNINTR` |

### Equity outcome

| Biến | Symbol |
|---|---|
| VNINDEX | `HOSE:VNINDEX` |

VNINDEX được request trực tiếp bên trong script. Model không phụ thuộc vào metadata ticker của chart hiện tại.

---

## 3. Macro State Engine

### Level

```text
Level = (2Y + 5Y + 10Y) / 3
```

Đại diện cho mặt bằng lợi suất chung.

### Slope

```text
Slope = 10Y − 2Y
```

Đại diện cho độ dốc của đường cong.

### Curvature

```text
Curvature = 2 × 5Y − 2Y − 10Y
```

Đại diện cho hình dạng phần giữa đường cong.

### Curve Stress

```text
Curve Stress =
0.45 × Level Rank
+ 0.45 × Slope Risk
+ 0.10 × Curvature Risk
```

Các thành phần được chuẩn hóa bằng rolling percentile.

> Percentile chỉ là rolling rank normalization, không đồng nghĩa chuỗi đã trở nên stationary.

---

## 4. Yield-Curve Regime

| Regime | Diễn giải |
|---|---|
| `YC0` | Neutral / Mixed |
| `YC1` | Easing mature |
| `YC2` | Early easing |
| `YC3` | Late tightening |
| `YC4` | High level + non-steep / inverted |

Ví dụ:

```text
Level HIGH
Slope LOW_SLOPE
→ YC4
```

YC4 thể hiện mặt bằng lợi suất cao trong khi đường cong không còn đủ dốc để được xem là trạng thái thuận lợi.

---

## 5. Data Quality

V2.3 tách chất lượng dữ liệu khỏi tín hiệu kinh tế.

Quality không còn được nhân trực tiếp vào Curve Stress.

Bảng coverage gồm:

```text
C / V / F / L
```

Trong đó:

- `C`: Core curve coverage — 2Y, 5Y, 10Y;
- `V`: VNINDEX coverage;
- `F`: Full curve coverage — 1Y đến 10Y;
- `L`: Liquidity coverage — interbank và policy rate.

Model readiness chủ yếu dựa trên core curve, VNINDEX và freshness. Liquidity coverage thấp sẽ được công khai nhưng không tự động xóa bỏ tín hiệu curve.

---

## 6. Horizon Separation

### Tactical Model — 1W

Mục tiêu:

- đo phản ứng ngắn hạn;
- nhận diện relief rally;
- kiểm tra phản ứng sau regime transition;
- hỗ trợ Tactical Bias.

Outcome:

```text
VNINDEX close tuần t+1 / close tuần t
```

Mẫu tuần không chồng lấn.

### Strategic Model — 4W

Mục tiêu:

- đo lực cản định giá;
- kiểm tra truyền dẫn vĩ mô chậm hơn;
- hỗ trợ Strategic Bias.

Outcome:

```text
VNINDEX close tuần t+4 / close tuần t
```

Strategic engine dùng cooldown 4 tuần để hạn chế outcome overlap.

---

## 7. Adaptive Sample Power

V2.3 tự động chọn chế độ sample:

```text
STANDARD POWER
52 tuần Development
52 tuần Validation
```

Khi lịch sử đủ dài:

```text
HIGH POWER
104 tuần Development
104 tuần Validation
```

Sample Power trả lời:

> Tổng chiều dài lịch sử có đủ hay không?

Nó không trả lời:

> Có đủ episode độc lập trong regime hiện tại hay không?

Vì vậy hoàn toàn có thể xuất hiện:

```text
POWER HIGH
READINESS 100
PREDICTIVE EVIDENCE 0
EPISODE N LOW
```

Đây là kết quả hợp lệ.

---

## 8. Episode-Aware Sampling

Các tuần nằm liên tiếp trong cùng một regime không được xem là các episode hoàn toàn độc lập.

Ví dụ:

```text
Stress HIGH kéo dài 12 tuần
```

Weekly descriptive có thể chứa 12 outcome, nhưng episode engine chỉ coi đây là một episode HIGH.

V2.3 sử dụng:

- regime-entry sampling;
- Tactical cooldown 1 tuần;
- Strategic cooldown 4 tuần;
- state và complement dùng chung cooldown clock.

Mục tiêu là hạn chế pseudo-replication do regime persistence.

---

## 9. Development và Validation

Mỗi horizon được chia thành:

```text
Development sample
Validation sample
```

Directional evidence chỉ được công nhận khi:

1. Development và Validation cùng dấu;
2. effect vượt minimum economic threshold;
3. Validation có đủ episode;
4. `|Welch t-stat| ≥ 1.96`;
5. CI 95% của state-minus-complement không chứa 0;
6. downside evidence nhất quán;
7. dữ liệu đạt gate;
8. daily bar đã được xác nhận.

Nếu Development và Validation trái dấu:

```text
DIRECTION UNSTABLE
```

và directional decision bị khóa.

---

## 10. Readiness và Predictive Evidence

### Model Readiness

Đánh giá:

- data coverage;
- history length;
- freshness;
- engine availability;
- sample power.

### Predictive Evidence

đánh giá:

- episode sample adequacy;
- effect size;
- sign consistency;
- Welch t-stat;
- confidence interval;
- downside consistency.

> Predictive Evidence không phải xác suất mô hình đúng.

---

## 11. Decision Engine

### Tactical Bias

Dựa trên validated Tactical 1W model.

Các trạng thái có thể gồm:

```text
DEFENSIVE
CAUTIOUS
NEUTRAL
CONSTRUCTIVE
NO SIGNAL
```

### Strategic Bias

Dựa trên validated Strategic 4W model.

### Combined Stance

Strategic bias có quyền ưu tiên. Khi hai horizon đối nghịch:

```text
MIXED
```

Model không ép hai horizon thành một tín hiệu duy nhất.

---

## 12. Các panel

### Panel 1 — Macro + Dual Horizon

Hiển thị:

- Level, Slope, Curvature;
- YC Regime;
- Curve Stress;
- Liquidity Gap;
- Data Quality;
- Sample Power;
- Tactical Evidence;
- Strategic Evidence;
- Combined Stance.

### Panel 2 — Tactical 1W Validation

Hiển thị:

- Development episode N;
- Validation episode N;
- State mean;
- Complement mean;
- Difference;
- Hit-down difference;
- Welch t-stat;
- CI 95%;
- hard gate;
- Tactical Bias.

### Panel 3 — Strategic 4W Validation

Tương tự Panel 2 nhưng dành cho horizon 4 tuần.

### Panel 4 — Horizon + Power Diagnostics

Hiển thị:

- LOW / MID / HIGH theo hai horizon;
- episode N;
- descriptive sample;
- sample-power mode;
- data coverage;
- structure diagnostics.

---

## 13. Cách cài đặt

1. Mở TradingView.
2. Mở **Pine Editor**.
3. Tạo indicator mới.
4. Xóa code mặc định.
5. Paste toàn bộ file `VN_YieldCurveLab_v2.3.0.pine`.
6. Nhấn **Save**.
7. Nhấn **Add to chart**.
8. Chạy trên chart `1D`.

Model request VNINDEX trực tiếp, nhưng timeframe chart vẫn phải là `1D` để bảo đảm rolling daily statistics và sampling clock vận hành đúng.

---

## 14. Cách đọc nhanh

### Trường hợp 1

```text
Curve Stress HIGH
Tactical NEUTRAL
Strategic CAUTIOUS
```

Diễn giải:

> Stress vĩ mô cao, chưa có edge ngắn hạn rõ ràng, nhưng horizon 4 tuần có dấu hiệu bất lợi đã được xác nhận.

### Trường hợp 2

```text
Readiness 100
Evidence 0
Episode N Low
```

Diễn giải:

> Engine có đủ dữ liệu tổng thể để vận hành, nhưng số episode độc lập trong regime hiện tại chưa đủ để kết luận.

### Trường hợp 3

```text
Macro Stress HIGH
Combined Stance NEUTRAL
```

Diễn giải:

> Trạng thái vĩ mô căng, nhưng outcome validation chưa đủ mạnh để phát directional bias.

`NEUTRAL` không có nghĩa macro trung tính.

---

## 15. Alert

Alert chỉ nên được sử dụng trên bar ngày đã xác nhận.

Các alert định hướng chỉ được phép phát sau khi:

- hard gate vượt qua;
- bias thay đổi;
- daily bar đóng.

Không sử dụng provisional intraday state như tín hiệu xác nhận.

---

## 16. Hạn chế

V2.3 không phải:

- causal model;
- machine-learning model;
- hệ thống trading tự động;
- công cụ position sizing;
- cam kết dự báo VNINDEX;
- bằng chứng rằng yield curve luôn dẫn dắt thị trường cổ phiếu.

Các hạn chế chính:

- số episode độc lập có thể rất thấp;
- dữ liệu yield Việt Nam trên TradingView có độ dài hữu hạn;
- liquidity coverage có thể thưa;
- regime persistence làm effective sample nhỏ hơn weekly N;
- statistical edge có thể thay đổi theo chu kỳ;
- một kết quả validated trong sample hiện tại vẫn có thể suy yếu về sau.

---

## 17. Nguyên tắc sử dụng

VN YieldCurveLab nên được dùng như:

```text
Macro monitoring
Regime classification
Risk-context dashboard
Validated decision support
```

Không nên dùng như:

```text
Standalone buy/sell signal
Guaranteed market forecast
Replacement for portfolio risk management
```

---

## 18. Trạng thái phát hành

| Hạng mục | Trạng thái |
|---|---|
| Pine compile/runtime | PASS |
| Host-independent VNINDEX source | PASS |
| Macro State Engine | PASS |
| Data Quality gating | PASS |
| Tactical 1W separation | PASS |
| Strategic 4W separation | PASS |
| Non-overlap control | PASS |
| Episode-aware sampling | PASS |
| Development/Validation | PASS |
| Adaptive Sample Power | PASS |
| Readiness/Evidence separation | PASS |
| Predictive edge | Chưa mặc định được xác nhận |

### Định vị chính thức

> **VN YieldCurveLab v2.3.0 là hệ thống theo dõi trạng thái đường cong lợi suất và kiểm định outcome VNINDEX theo hai horizon, sử dụng episode-aware sampling, Development/Validation và hard decision gates.**

---

## 19. Disclaimer

Chỉ báo được cung cấp cho mục đích nghiên cứu và hỗ trợ quyết định.

Không phải khuyến nghị mua, bán hoặc nắm giữ bất kỳ tài sản nào. Kết quả lịch sử không bảo đảm kết quả tương lai. Người sử dụng chịu trách nhiệm đối với mọi quyết định đầu tư dựa trên dữ liệu, mô hình hoặc diễn giải từ chỉ báo này.
