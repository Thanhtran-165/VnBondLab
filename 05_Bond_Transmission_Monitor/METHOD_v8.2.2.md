# MacroAcademic v8.2.2 — Research Precision & Dual Chain Diagnostics

## Mục tiêu bản vá

V8.2.2 là bản vá kiểm định và trình bày cho V8.2.1. Bản này **không thay đổi** công thức mô hình, trọng số Evidence, nested walk-forward, lag selection, Data Gate, Model Gate, ngưỡng VALID/WATCH hay weakest-link discipline.

Bản vá xử lý hai lỗi đã được Research Mode phát hiện:

1. Các format mask `"#.1"` và `"#.3"` khiến Pine in `1` và `3` như ký tự literal sau dấu thập phân, làm sai cách hiển thị beta, OOS R², Edge, Hit, lag gap và các delta.
2. P6 ghi đè lý do của direct forecast gate bằng `FAIL: LINK x`, khiến người dùng không thể phân biệt lỗi của mắt xích với lỗi của forecast toàn chuỗi.

---

## 1. Research Precision

### Quy tắc format mới

V8.2.2 định nghĩa ba mask dùng chung:

```pine
string FMT_1 = "#.0"
string FMT_2 = "#.00"
string FMT_3 = "#.000"
```

Trong Pine, `0` là placeholder chữ số. Vì vậy:

| Chỉ tiêu | Mask | Mục đích |
|---|---|---|
| Observed, Forecast, Evidence, delta | `#.0` | Một chữ số thập phân |
| Hit, Naive, Stability, ResidualQ, coverage | `#.0` | Một chữ số thập phân |
| Directional Edge | `#.00` | Phân biệt chính xác quanh ngưỡng hard gate bằng 0 |
| Lag gap | `#.00` | Đánh giá khoảng cách với ngưỡng 2,50 |
| Beta | `#.000` | Giữ dấu và độ lớn hệ số |
| Selection OOS R² | `#.000` | Đọc đúng calibration evidence |
| Holdout OOS R² | `#.000` | Đọc đúng predictive performance gần nhất |

### Lý do Edge cần hai chữ số

Hard gate kiểm tra trực tiếp:

```text
Directional Edge > 0
```

Một giá trị nhỏ như `-0,04 pp` không được hiển thị thành `0,0 pp`, vì điều đó làm bảng số liệu mâu thuẫn với thông báo `EDGE≤0`.

### Lý do OOS R² cần ba chữ số

Đối với daily yield changes, OOS R² thường nằm rất gần 0. Ba chữ số giúp phân biệt:

- `-0,004`: kém benchmark nhẹ;
- `-0,080`: thất bại đáng kể;
- `+0,012`: predictive edge dương nhưng nhỏ.

---

## 2. Dual Chain Diagnostics cho P6

P6 hiện giữ ba kết luận riêng:

### Link Gate

Đánh giá A/B/C theo CoreModel riêng:

```text
A: Global rates/DXY → USDVND
B: USDVND → Interbank
C: Interbank → VN10Y
```

Nếu chưa đủ cả ba strict-pass, bảng Research hiển thị mắt xích thất bại yếu nhất và gate reason của chính mắt xích đó.

### Direct Forecast Gate

Đánh giá forecast trực tiếp của toàn chuỗi bằng:

- direct holdout OOS R²;
- Hit / Naive / Edge;
- directional coverage;
- residual quality;
- generalization;
- chain stability/sign/lag constraints đang dùng trong hard gate.

Direct reason được lưu độc lập và không còn bị ghi đè bởi Link Gate.

### Overall State

Trạng thái P6 vẫn giữ logic cũ:

```text
VALID = tất cả link strict-pass AND direct forecast strict-pass
WATCH = tất cả link ít nhất WATCH AND direct forecast đạt watch gate
NO SIGNAL = còn lại
```

Không có sự nới lỏng ngưỡng.

---

## 3. Giao diện Research P6

P6 Research Mode dùng 10 hàng:

1. Header: Observed / Validated / State
2. Pressure và forecast
3. DataQ / Evidence / diagnostic
4. Xu hướng 1d / 7d
5. Overall Gate note
6. Chain model: lag, lag gap, beta, selection OOS R²
7. Direct holdout: R², Hit, Naive, Edge
8. Chain diagnostics: min stability, ResidualQ, directional coverage
9. **Link Gate và Direct Gate đặt cạnh nhau**
10. Evidence và diagnostic của A/B/C

Overview Research cũng hiển thị hai P6 gate riêng ở hàng cuối.

---

## 4. Phạm vi không thay đổi

- Pine Script v6.
- Chỉ chạy chart 1D.
- `calc_bars_count=800`, `max_bars_back=800`.
- 17 static `request.security()`.
- Tất cả request dùng `lookahead_off`.
- Train 120 / calibration 60 / holdout 40.
- Lag candidates 0/1/3/5.
- Benchmark tốt hơn giữa zero-change và rolling historical mean.
- Median/MAD robust scaling.
- Predictive coherence cap.
- DataQ độc lập Evidence.
- Hard VALID/WATCH gates.
- UNSTABLE / GEN FAIL / BREAK WARNING.
- Executive unified display.

---

## 5. Protocol kiểm tra TradingView

Sau khi compile, chỉ cần chụp lại bốn màn hình Research Mode:

1. Overview
2. P1
3. P4
4. P6

### PASS criteria

- Không còn số liệu kiểu `.1` hoặc `.3` lặp máy móc.
- Beta và R² hiển thị ba chữ số thực.
- Edge hiển thị hai chữ số và nhất quán với `EDGE≤0` hoặc `PASS`.
- Lag gap hiển thị hai chữ số và nhất quán với ngưỡng 2,50.
- P6 hiển thị đồng thời `LINK GATE` và `DIRECT GATE`.
- `FAIL: LINK x` không che mất lỗi direct forecast.
- Model state và hard gate không thay đổi chỉ vì bản vá định dạng.

## Trạng thái xác nhận

- Static QA: PASS.
- Live Pine Editor compile: cần xác nhận trên TradingView.
- Live Research precision audit: cần bốn ảnh theo protocol trên.
