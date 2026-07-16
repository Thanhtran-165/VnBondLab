# MacroAcademic v8.2.2

## Research Precision & Dual Chain Diagnostics

**Trạng thái phát hành:** `FINAL BASELINE — LOCKED`  
**Nền tảng:** TradingView · Pine Script v6  
**Khung thời gian bắt buộc:** `1D`  
**Ngày khóa phiên:** 16/07/2026  
**Mục đích:** giám sát áp lực vĩ mô lên lợi suất Việt Nam và kiểm định xem các kênh truyền dẫn có tạo được **năng lực dự báo ngoài mẫu** hay không.

---

## 1. Tuyên bố phát hành

MacroAcademic v8.2.2 là bản cuối của nhánh V8 và được dùng làm **baseline chính thức để đọc ảnh, vận hành dashboard và đối chiếu các lần kiểm định sau này**.

Bản này đã hoàn tất:

- Pine Script v6 compile thành công;
- chạy ổn định trong giới hạn thời gian của TradingView;
- giao diện Executive được rút gọn và thống nhất;
- Research Mode hiển thị đúng độ chính xác của beta, OOS \(R^2\), Edge và lag gap;
- Evidence Score không còn mang ý nghĩa trái ngược với predictive core;
- P6 tách riêng **Link Gate** và **Direct Gate**;
- hard gate giữ nguyên tính nghiêm ngặt;
- kiểm định ảnh thực tế đã hoàn tất.

> **Không có predictive edge là một kết quả hợp lệ.** Mô hình không có nhiệm vụ phải luôn phát tín hiệu.

---

## 2. Bộ tệp bàn giao

| Tệp | Vai trò |
|---|---|
| `MacroAcademic_v8_2_2_Research_Precision_Dual_Chain_Diagnostics.pine` | Mã nguồn Pine Script hoàn chỉnh |
| `MacroAcademic_v8_2_2_METHOD.md` | Phương pháp luận và phạm vi bản vá |
| `MacroAcademic_v8_2_2_QA.json` | Kết quả static QA |
| `README_MacroAcademic_v8_2_2_FINAL.md` | Hướng dẫn vận hành, đọc ảnh và khóa phiên bản |

### SHA-256

```text
e6db0e36b7870225a9bddfff94303aa4dce19e564a9b17fed88b8cf4f46a56e3  Pine Script
c9519fcc1adc3182146cbf3b42a25afa6e31f94ecc1dc42094718f3f185e344b  Methodology
89713b97db95a7a139aaea6b88df33eaccdf325da5a4a568ec88c8b311c5cb8e  QA report
```

---

## 3. Khởi động nhanh

1. Mở TradingView Pine Editor.
2. Dán toàn bộ mã nguồn V8.2.2.
3. Lưu và thêm indicator vào chart.
4. Chuyển chart sang **1D**.
5. Dùng `Executive` để theo dõi thường xuyên.
6. Dùng `Research` khi cần audit mô hình.

Không chạy trên chart intraday. Mỗi bar của engine phải tương ứng với một quan sát ngày; nếu dùng intraday, các cửa sổ 120/60/40 và lag ngày sẽ mất đúng nghĩa thống kê.

---

## 4. Kiến trúc khái niệm

V8.2.2 tách ba khái niệm không được phép trộn lẫn:

### Observed Pressure

Mức áp lực đang quan sát từ driver vĩ mô và biến động VN10Y. Đây là **trạng thái dữ liệu**, không phải kết quả dự báo.

### Model Forecast

Giá trị dự báo từ rolling regression. Forecast chỉ được xem là có ý nghĩa vận hành khi vượt hard gate.

### Validated Pressure

Forecast đã vượt đồng thời Data Gate và Model Gate. Nếu mô hình chưa đạt `VALID`, trường này hiển thị `N/A`.

Ví dụ:

```text
Observed 68
Forecast chưa xác nhận
Validated N/A
NO SIGNAL
```

Diễn giải đúng: dữ liệu đang có áp lực, nhưng kênh truyền dẫn chưa chứng minh được predictive edge.

---

## 5. Sáu kênh nghiên cứu

| Panel | Giả thuyết kiểm định |
|---|---|
| **P1** | BOJ/JGB → VN10Y |
| **P2** | Lợi suất dài hạn toàn cầu → VN10Y |
| **P3** | Level và thay đổi đường cong toàn cầu → VN10Y |
| **P4** | Yen carry stress → VN10Y |
| **P5** | FX và thanh khoản nội địa → VN10Y |
| **P6** | Global → FX → Interbank → VN10Y |

P1–P5 dùng chung một contract kết quả. P6 có thêm kiểm định từng mắt xích và forecast trực tiếp toàn chuỗi.

---

## 6. Kỷ luật kinh tế lượng

### Nested walk-forward

- `Train`: 120 phiên;
- `Calibration/lag selection`: 60 phiên cũ hơn;
- `Final holdout`: 40 phiên gần nhất;
- lag ứng viên: `0 / 1 / 3 / 5`.

Lag được chọn trên calibration OOS. Holdout gần nhất chỉ dùng để xác nhận, không được dùng lại để chọn lag.

### Benchmark ngoài mẫu

Mô hình được so với benchmark tốt hơn trong hai benchmark:

- dự báo thay đổi bằng 0;
- dự báo bằng trung bình lịch sử rolling.

OOS \(R^2\) dương có nghĩa mô hình đánh bại benchmark. OOS \(R^2\) âm có nghĩa mô hình dự báo kém hơn benchmark.

### Directional Edge

Hit rate không được đọc độc lập. Mô hình phải vượt naive majority benchmark:

```text
Directional Edge = Hit rate − Naive hit rate
```

Một Hit rate 67% không có giá trị nếu naive benchmark cũng đạt 67%.

### Robust scaling

Các biến được chuẩn hóa bằng median/MAD để giảm ảnh hưởng của phiên cực đoan. Engine không sử dụng p-value hay t-stat thiếu hiệu chỉnh HAC để tạo cảm giác chính xác giả.

---

## 7. DataQ, Evidence và hard gate

### DataQ

Đánh giá chất lượng dữ liệu theo nguyên tắc nút thắt:

```text
DataQ = min(Coverage, Freshness, Breadth)
```

DataQ tốt không được phép bù cho predictive skill yếu.

### Evidence Score

Evidence là thước đo chẩn đoán liên tục từ 0–100, kết hợp:

- holdout OOS \(R^2\);
- directional edge;
- stability;
- residual quality;
- generalization;
- directional coverage;
- lag robustness.

Evidence **không thay thế hard gate**.

### Predictive Coherence Cap

Evidence bị giới hạn để không tạo ngữ nghĩa sai:

| Predictive core | Evidence tối đa |
|---|---:|
| OOS ≤ 0 và Edge ≤ 0 | 49 |
| Một trong hai thất bại | 59 |
| Beta trái dấu lý thuyết | 49 |
| OOS và Edge cùng dương, đúng dấu | 100 |

Do đó `Evidence 49` có thể đại diện cho nhiều kiểu thất bại khác nhau. Phải đọc thêm `Gate Diagnostics` để biết nguyên nhân.

### Trạng thái

| Trạng thái | Ý nghĩa |
|---|---|
| `VALID` | Có predictive edge ngoài mẫu và vượt toàn bộ hard gate |
| `WATCH` | Có tín hiệu một phần nhưng chưa đủ chuẩn sử dụng |
| `NO SIGNAL` | Không có bằng chứng dự báo đủ dùng |
| `DATA ISSUE` | Chất lượng hoặc độ mới dữ liệu không đạt |

---

## 8. Cách đọc Executive Mode

Executive Mode là chế độ vận hành mặc định. Dữ liệu hiển thị được làm mượt EMA, nhưng engine và gate vẫn dùng dữ liệu raw.

### Overview

Đọc theo thứ tự:

1. **OBS:** áp lực quan sát tổng hợp;
2. **VALIDATED:** forecast đã được xác nhận hay chưa;
3. **State:** VALID/WATCH/NO SIGNAL;
4. **Driver chính:** kênh có áp lực quan sát cao nhất;
5. **Kênh thấp nhất:** kênh giảm áp lực nhất;
6. **DataQ / Evidence / VALID count:** chất lượng đầu vào và mức bằng chứng;
7. **P6:** nút thắt của chuỗi;
8. **Hàm ý:** câu kết luận hệ thống.

### Quy tắc sử dụng

- `Observed` cao nhưng `NO SIGNAL`: chỉ ghi nhận áp lực, không dùng forecast.
- `Evidence` khá nhưng Gate fail: xem như mô hình gần đạt hoặc ổn định về mặt nào đó, chưa phải tín hiệu.
- Chỉ sử dụng `Validated Pressure` khi state là `VALID`.
- Không suy diễn từ một panel đơn sang quyết định phân bổ tài sản.

---

## 9. Cách đọc Research Mode

Research Mode dùng cho audit, không cần mở hằng ngày.

### Các chỉ tiêu chính

| Chỉ tiêu | Cách đọc |
|---|---|
| `Select R²` | Hiệu quả OOS tại cửa sổ dùng chọn lag |
| `Holdout R²` | Hiệu quả OOS gần nhất, là bằng chứng chính |
| `Hit / Naive / Edge` | Khả năng dự báo hướng sau khi trừ benchmark |
| `Lag / gap` | Lag tốt nhất và khoảng cách với ứng viên thứ hai |
| `Beta` | Dấu và độ lớn của liên hệ dự báo |
| `Stability` | Độ ổn định tham số giữa các cửa sổ |
| `ResidualQ` | Chẩn đoán phần dư, không phải predictive edge |
| `Dir coverage` | Tỷ lệ phiên đủ điều kiện đánh giá hướng |
| `Coverage/Fresh/Breadth` | Chất lượng dữ liệu |
| `Gate Diagnostics` | Lý do trực tiếp khiến mô hình không đạt |

### Độ chính xác số

| Chỉ tiêu | Hiển thị |
|---|---:|
| Observed, Forecast, Evidence | 1 chữ số |
| Edge, lag gap | 2 chữ số |
| Beta, OOS \(R^2\) | 3 chữ số |

Giá trị quanh 0 có thể bị làm tròn. Hard gate luôn dùng giá trị đầy đủ, không dùng số đã làm tròn trên bảng.

---

## 10. P6 — Dual Chain Diagnostics

P6 kiểm định ba mắt xích:

```text
A: Global rates/DXY → USDVND
B: USDVND → Interbank
C: Interbank → VN10Y
```

### Link Gate

Đánh giá riêng A/B/C. Trạng thái toàn chuỗi không được phép vượt qua mắt xích yếu nhất.

### Direct Gate

Đánh giá forecast trực tiếp của toàn chuỗi với VN10Y bằng OOS \(R^2\), Edge, directional coverage, stability và residual diagnostics.

### Overall Gate

```text
VALID = A, B, C strict-pass và direct forecast strict-pass
WATCH = A, B, C ít nhất WATCH và direct forecast đạt watch gate
NO SIGNAL = còn lại
```

Link Gate và Direct Gate là hai lớp độc lập. Một chuỗi có thể vừa đứt ở một link, vừa thất bại ở direct forecast.

---

## 11. Snapshot xác nhận khi khóa phiên

**Thời điểm ảnh kiểm định:** 16/07/2026, khoảng 17:25–17:26 UTC+7.  
Các số dưới đây là snapshot tại thời điểm kiểm định, không phải hằng số của mô hình.

### Overview

```text
Observed Pressure    49,8
Evidence hệ thống    47,5
DataQ               100,0
VALID                 0/5
State                 NO SIGNAL
P6 bottleneck         Link B
```

### Kết quả từng kênh

| Kênh | Select R² | Holdout R² | Beta | Edge | Stability | Kết luận |
|---|---:|---:|---:|---:|---:|---|
| P1 | +0,011 | −0,050 | −0,006 | 0,00 pp | 4,9 | OOS, Edge, Sign, Unstable |
| P2 | −0,017 | −0,008 | +0,012 | 0,00 pp | 4,1 | OOS, Edge, Unstable |
| P3 | −0,010 | +0,005 | −0,166 | 0,00 pp | 52,3 | Edge, Sign |
| P4 | +0,005 | +0,005 | −0,388 | +3,45 pp | 49,0 | Sign, Lag gap |
| P5 | +0,062 | −0,040 | −0,133 | 0,00 pp | 70,1 | OOS, Edge, Sign |
| P6 direct | −0,001 | ≈0,000 | +0,003 | 0,00 pp | 12,3 | Edge, Unstable; Link B fail |

### Diễn giải snapshot

- P1 và P2 bị bác rõ do OOS yếu và stability rất thấp.
- P3 có Holdout R² hơi dương nhưng không có directional edge và beta trái dấu giả thuyết.
- P4 là kênh gần đạt nhất, nhưng dấu beta và lag robustness chưa đạt.
- P5 ổn định về tham số nhưng không duy trì được predictive edge từ calibration sang holdout.
- P6 đứt ở mắt xích B; direct forecast cũng không có Edge và thiếu ổn định.

Kết luận tại thời điểm khóa phiên:

> **Áp lực quan sát trung tính. Dữ liệu có chất lượng cao, nhưng chưa kênh nào chứng minh được khả năng dự báo VN10Y vượt benchmark trên holdout gần nhất.**

---

## 12. Mô hình được phép và không được phép kết luận gì

### Được phép

- mô tả áp lực quan sát;
- xác định kênh nào đang tăng hoặc giảm áp lực;
- đánh giá chất lượng dữ liệu;
- kiểm tra predictive edge ngoài mẫu;
- chỉ ra lý do gate thất bại;
- phát hiện bottleneck trong chuỗi truyền dẫn;
- theo dõi sự thay đổi của Evidence và trạng thái theo thời gian.

### Không được phép

- tuyên bố quan hệ nhân quả;
- diễn giải beta thành tác động chính sách chắc chắn;
- dùng residual như bằng chứng “nội lực” hoặc “tách biệt”;
- coi Evidence là xác suất;
- coi forecast chưa VALID là tín hiệu giao dịch;
- đổi dấu kỳ vọng hoặc threshold sau khi nhìn kết quả chỉ để cứu mô hình;
- dùng một snapshot để tối ưu mô hình.

---

## 13. Kỷ luật vận hành

### Hằng ngày

- dùng Executive Mode;
- quan sát State, Observed, Evidence, Driver chính và P6 bottleneck;
- không hành động theo forecast nếu `Validated N/A`.

### Khi nào mở Research Mode

- phiên bản mới;
- đổi symbol hoặc nguồn dữ liệu;
- thay đổi dấu kỳ vọng;
- thay đổi train/select/holdout hoặc lag;
- panel chuyển sang WATCH/VALID;
- Evidence tăng/giảm bất thường;
- P6 thay bottleneck;
- nghi ngờ dữ liệu cũ hoặc thiếu.

### Không thay đổi tùy tiện

- dấu kỳ vọng;
- ngưỡng DataQ;
- Stability threshold;
- Lag-gap threshold;
- Evidence weights;
- cửa sổ 120/60/40;
- lag candidates.

Mọi thay đổi logic mô hình phải bắt đầu ở một version mới, không sửa ngầm V8.2.2.

---

## 14. Giới hạn học thuật

V8.2.2 là một **validated predictive monitor**, không phải mô hình nhận dạng nhân quả hoặc nghiên cứu publication-grade.

Các giới hạn còn lại:

- chưa có HAC/Newey–West standard errors;
- chưa có confidence interval hoặc p-value hiệu chỉnh;
- chưa có kiểm định structural break chính thức;
- chưa xử lý endogeneity;
- global factor vẫn là composite được định nghĩa trước, không phải dynamic factor/PCA đầy đủ;
- hệ thống đang đánh giá một horizon ngày và tập lag hữu hạn;
- kết quả phụ thuộc chất lượng symbol và lịch cập nhật của TradingView.

Các giới hạn này phải được giữ nguyên trong mọi báo cáo sử dụng V8.2.2.

---

## 15. Chính sách phiên bản

- `v8.2.2` được khóa làm baseline cuối của nhánh V8.
- Không sửa công thức hoặc threshold dưới cùng version.
- Sửa chính tả/tài liệu không ảnh hưởng engine có thể ghi nhận là documentation-only.
- Thay đổi mô hình, panel, gate, dữ liệu hoặc phương pháp kiểm định phải mở version mới.
- Không hồi tố chỉnh dấu hoặc lag sau khi xem holdout hiện tại.

---

## 16. Final Readiness Check

| Hạng mục | Trạng thái |
|---|---|
| Pine v6 compile | PASS |
| Runtime TradingView | PASS |
| Chart 1D discipline | PASS |
| Static requests / lookahead off | PASS |
| Executive information architecture | PASS |
| Unified display | PASS |
| Research numeric precision | PASS |
| Continuous Evidence + coherence cap | PASS |
| Hard gate integrity | PASS |
| P6 weakest-link gate | PASS |
| P6 dual diagnostics | PASS |
| Live screenshot audit | PASS |
| Release baseline | **LOCKED** |

---

## Kết phiên

MacroAcademic v8.2.2 được chốt làm **bản cuối để đọc ảnh và baseline vận hành chính thức**.

Nguyên tắc cuối cùng của hệ thống:

> **Dữ liệu tốt không thay thế được predictive edge. Áp lực quan sát không đồng nghĩa với truyền dẫn đã được xác nhận. Không có tín hiệu là một kết quả hợp lệ.**

**End of MacroAcademic v8.2.2 Final README.**
