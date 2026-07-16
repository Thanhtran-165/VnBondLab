# Macro Alert System v7.0.0 — Review & Academic Methodology

## 1. Kết luận review

Phiên bản v6.0.1 đã có nền tảng tốt hơn đáng kể so với một indicator thông thường: tách mức tín hiệu khỏi chất lượng dữ liệu, dùng mẫu forward không chồng lấn, so regime hiện tại với phần bù “các regime khác”, có kiểm tra pre/post-2020, shrinkage cho sector và Jeffreys smoothing cho transition.

Tuy nhiên, audit phát hiện một số điểm có thể làm bằng chứng trông chắc hơn mức thực tế:

1. Composite risk là trung bình có trọng số của các percentile thành phần nhưng lại được chia bucket trực tiếp tại 20/40/60/80. Phân phối của trung bình percentile không còn đồng đều, nên bucket cực đoan có thể bị nén.
2. `barmerge.gaps_off` có thể carry-forward giá trị cũ; kiểm tra “không phải NA” chưa đủ để kết luận dữ liệu còn mới.
3. Grade lịch sử dùng data quality ở thời điểm hiện tại thay vì chất lượng dữ liệu tại thời điểm tín hiệu được hình thành.
4. Chất lượng mẫu mới chỉ phản ánh nhóm regime, chưa bảo thủ hóa theo nhóm đối chứng.
5. Welch statistic chưa dùng bậc tự do để điều chỉnh critical value; kiểm định ba horizon chưa có family-wise guard đầy đủ.
6. Kiểm tra pre/post mới dựa vào cùng dấu, chưa phân biệt “cùng dấu nhưng độ lớn đã thay đổi mạnh”.
7. Một pha non-overlap duy nhất có thể tạo kết quả nhạy với ngày bắt đầu lấy mẫu.
8. Drawdown có thể dương nếu đáy trong cửa sổ vẫn cao hơn mức entry, trái với định nghĩa drawdown.
9. “Structural confidence” là điểm heuristic nhưng tên gọi có thể bị hiểu như xác suất thống kê.

## 2. Nâng cấp trong v7.0.0

### 2.1 Empirical regime calibration

- Giữ latent score theo trọng số kinh tế học.
- Chuyển latent score thành rolling empirical percentile trước khi chia B0–B4.
- Tạo thêm equal-weight specification để đo độ nhạy với lựa chọn trọng số.
- `Specification score` giảm khi weighted model và equal-weight model phân kỳ.

Điều này làm ngưỡng 20/40/60/80 có ý nghĩa percentile thực nghiệm rõ hơn, thay vì giả định trung bình percentile vẫn phân phối đều.

### 2.2 Freshness-aware data quality

Data quality mới kết hợp:

- component coverage;
- source coverage;
- độ mới của timestamp từng nguồn.

Nguồn nhanh dùng tolerance 5 ngày; policy series dùng 14 ngày. Điểm giữ ở 100 trong tolerance rồi giảm tuyến tính về 0 tại 3 lần tolerance.

### 2.3 Entry-time sample quality

Mỗi observation forward 5D/20D/60D lưu data quality tại **thời điểm entry**. Grade sử dụng mức thấp hơn giữa:

- chất lượng trung bình của nhóm regime;
- chất lượng trung bình của nhóm đối chứng.

Nhờ vậy, dữ liệu tốt hôm nay không thể “nâng hạng hồi tố” cho mẫu lịch sử kém chất lượng.

### 2.4 Welch inference mạnh hơn

Mỗi horizon hiện báo cáo hoặc sử dụng:

- mean regime và mean nhóm khác;
- Welch standard error;
- Welch–Satterthwaite degrees of freedom;
- Welch t statistic;
- Hedges’ g;
- family-wise confidence bounds trên ba horizon.

Critical value được điều chỉnh từ normal sang Student-t bằng xấp xỉ Cornish–Fisher, đặc biệt bảo thủ hơn khi bậc tự do thấp.

### 2.5 Statistical significance + economic materiality

Grade A/B không chỉ yêu cầu interval loại trừ 0. Nó còn yêu cầu:

- effect tối thiểu theo horizon: 0,5% / 1,0% / 2,0% log-return;
- |Hedges’ g| ≥ 0,20;
- pre/post ổn định;
- chất lượng mẫu đạt chuẩn;
- độ đồng thuận giữa các pha thay thế.

Điều này giảm nguy cơ “có ý nghĩa thống kê nhưng vô nghĩa kinh tế”.

### 2.6 Structural break diagnostic

Pre/post-2020 được phân loại:

- `STABLE+` / `STABLE-`: cùng hướng và không có break lớn;
- `SHIFT+` / `SHIFT-`: cùng hướng nhưng độ lớn thay đổi có ý nghĩa xấp xỉ;
- `MIXED`: đảo hướng;
- `NA`: chưa đủ mẫu.

Grade cao chỉ chấp nhận `STABLE`, không chấp nhận `SHIFT`.

### 2.7 Staggered phase robustness

Với mỗi horizon, hệ thống xây năm cohort non-overlap lệch pha. Phase 0 là estimator chính; bốn phase còn lại chỉ dùng làm sensitivity diagnostic và không được pool như dữ liệu độc lập.

`Alt phase agreement` loại phase 0 khỏi mẫu kiểm tra để tránh cơ chế tự xác nhận.

### 2.8 Model reliability thay cho confidence

`Model reliability` là điểm heuristic gồm:

- cross-layer concordance;
- regime persistence;
- data quality;
- specification robustness.

Điểm bị cap nếu layer disagreement hoặc model-weight disagreement quá lớn. Tên gọi mới tránh nhầm lẫn với xác suất hoặc confidence interval.

### 2.9 Drawdown correction

Drawdown được định nghĩa:

`min(horizon_low / entry - 1, 0)`

Do đó không còn drawdown dương.

### 2.10 Sector and transition

- Sector vẫn dùng zero-prior regularization và family-wise conservative bounds.
- Sector critical value cũng được điều chỉnh theo bậc tự do.
- Transition vẫn dùng Jeffreys smoothing α = 0,5 cho từng destination state.
- Ngôn ngữ “Improve / Persist / Worsen” vẫn đúng theo hướng giảm/tăng macro risk.

## 3. Quy tắc Evidence Grade v7.0.0

| Grade | Điều kiện chính |
|---|---|
| A | N regime và N other ≥ 30; pair quality ≥ 85; FWER 95% interval loại trừ 0; effect material; Hedges’ g ≥ 0,20; pre/post stable; alternative-phase agreement ≥ 75% |
| B | N mỗi nhóm ≥ 20; pair quality ≥ 70; FWER 90% interval loại trừ 0; effect material; pre/post stable; alternative-phase agreement ≥ 75% |
| C+ | Pair quality ≥ 70; effect material; pre/post stable; alternative-phase agreement ≥ 50%, nhưng chưa đạt interval/sample gate của A/B |
| C | Có đủ mẫu hiển thị nhưng bằng chứng chưa ổn định hoặc chưa material |
| D | Thiếu mẫu hoặc không đủ điều kiện tính toán |

Grade là thang **độ mạnh của bằng chứng mô tả**, không phải xác suất dự báo đúng.

## 4. Kiểm tra tĩnh đã thực hiện

- 1.509 dòng Pine Script v6.
- Cân bằng `()`, `[]`, `{}`: PASS.
- Arity của toàn bộ user-defined function call: PASS.
- Không còn biến cũ hoặc cấu hình không dùng: PASS.
- Kích thước và chỉ số cố định của bốn bảng: PASS.
- Drawdown clamp: PASS.
- `lookahead_off` giữ nguyên cho toàn bộ request: PASS.
- Invalid-symbol requests tiếp tục trả `NA`: PASS.
- SHA-256: `02906eab87a457d675b7e87cb21f75eca7dc4d133d44a76d7e3624940f934918`.

## 5. Giới hạn còn lại

1. Chưa có Pine compiler trong môi trường hiện tại, nên đây là static validation chứ chưa phải xác nhận compile trực tiếp trong TradingView.
2. Welch inference vẫn giả định mức độc lập xấp xỉ giữa các block non-overlap; clustering regime và serial dependence có thể còn tồn tại.
3. Không có causal identification. Kết quả chỉ là conditional historical association.
4. Split 2020 là một robustness split định trước, không phải structural-break date được ước lượng nội sinh.
5. Materiality floor và model weights là research priors; cần walk-forward calibration ngoài Pine nếu muốn công bố như mô hình dự báo.
6. Rolling empirical rank tạo warm-up dài: component percentiles cần lịch sử, sau đó latent percentile tiếp tục cần cửa sổ hiệu chỉnh.
7. Nguồn TradingView có thể khác về lịch cập nhật, methodology và revision policy; freshness không thay thế source governance.

## 6. Checklist triển khai

1. Dán file `.pine` vào Pine Editor.
2. Compile trên chart Daily trước.
3. Kiểm tra từng symbol `VNINTR`, `VN02Y`, `VN10Y`, `US10Y`, `VNINBR`, `USDVND`, `USINTR`.
4. So sánh panel trên Daily và intraday để xác nhận quy tắc “last completed daily observation”.
5. Kiểm tra warm-up và số mẫu của từng bucket.
6. Chỉ kích hoạt alert khi `DQ ≥ 70`, `Reliability ≥ 55`, `Specification ≥ 60`.
7. Lưu ảnh Evidence panel và Data Window cho ít nhất ba giai đoạn stress lịch sử để thực hiện regression test thủ công.

## 7. Định hướng v7.1 nghiên cứu

Bước tiếp theo hợp lý là tách Pine thành hai tầng:

- **Production indicator:** regime, quality, alert và readout.
- **Offline validation harness:** bootstrap theo block, HAC/Newey–West, walk-forward, placebo tests, sensitivity grid và out-of-sample scoring.

Đây là điều kiện cần nếu muốn nâng mô hình từ “academic-style indicator” thành một research system có thể audit và tái lập.
