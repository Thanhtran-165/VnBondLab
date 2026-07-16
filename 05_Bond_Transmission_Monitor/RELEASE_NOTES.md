# Release Notes — VN Bond Transmission Monitor

## 📅 Version 8.2.2 (Current Release)

**Release Date:** 2026
**Platform:** TradingView Pine Script v6

### Research Precision & Dual Chain Diagnostics

Bản v8.2.2 nâng cấp từ v6.0.1 lên Research Precision & Dual Chain Diagnostics:
- Tinh chỉnh inference và độ chính xác nghiên cứu
- Bổ sung dual chain diagnostics cho chuỗi truyền dẫn
- Nâng cấp Pine Script v5 → v6
- Code: 893 dòng (v6.0.1) → 1206 dòng (v8.2.2)

---

## 📅 Version 6.0.1

**Release Date:** 2025
**Platform:** TradingView Pine Script v5

### Interpretation Upgrade

Bản v6.0.1 nâng cấp lớp diễn giải trên nền v5.2:
- Cải tiến nhãn và cách đọc dashboard cho người dùng cuối
- Tinh chỉnh interpretation logic cho 6 panel

---

## 📅 Version 5.2

**Release Date:** January 2025
**Platform:** TradingView Pine Script v5

---

## ✨ New Features

### 🔍 Mở rộng lên 6 Panel (P1–P6)

Theo dõi truyền dẫn trái phiếu VN theo nhiều kênh:

- **P1 — BOJ → VN**: Kênh Nhật Bản (Bank of Japan)
- **P2 — Toàn cầu → VN**: Global rates (US/DE/GB/AU/CA)
- **P3 — Đường cong → VN**: Yield curve level & slope
- **P4 — Yên carry → VN**: Risk-off channel (JPY strengthen + VIX)
- **P5 — FX & Thanh khoản → VN**: USDVND + VNINBR/IB
- **P6 — Chuỗi truyền dẫn → VN**: Full chain (US2Y+DXY → USDVND → VNINBR/IB → VN10Y)

---

## 🔬 Nâng cấp mô hình học thuật

### 1. Rolling OLS có Intercept

**Trước đây:** Simple regression (y = βx)
**v5.2:** Full OLS với intercept (y = α + βx + ε)

**Lợi ích:**
- Tách được **Expected Component** (α + βx) - phần được giải thích bởi driver
- Tách được **Residual Component** (ε) - phần riêng của VN (decoupling)
- Đo lường chính xác mức độ "bị kéo theo" vs "tự chủ"

**Công thức:**
```pine
// OLS với intercept
beta  = corr * (sdY / sdX)
alpha = my - beta * mx
expY  = alpha + beta * x  // Expected
resY  = y - expY          // Residual (Decoupling)
```

### 2. Phân rã Dự tính & Tách biệt nhất quán

Áp dụng cho **tất cả 6 panel**:
- **Dự tính (Expected)**: Phần biến động VN10Y giải thích được bởi driver
- **Tách biệt (Residual)**: Phần biến động riêng của VN (ngoại lực vs nội lực)

**Diễn giải:**
- Dự tính cao → Driver mạnh → VN dễ bị kéo theo
- Tách biệt cao → VN có nội lực → Ít bị kéo theo

### 3. Đánh giá độ tin cậy (Quality Layer)

**Kết hợp 2 yếu tố:**
1. **R² / Chain Strength** - Độ mạnh truyền dẫn
2. **Coverage** - Độ phủ dữ liệu (không NA)

**Công thức:**
```pine
Quality = 0.6 × R² + 0.4 × Coverage
```

**Gán nhãn:**
- **Tin cậy:** Thấp (<50) / Trung bình (50-70) / Cao (>70)
- **Truyền dẫn:** Yếu (<20%) / Vừa (20-40%) / Mạnh (>40%)

**Quy tắc vàng:**
> Chỉ kết luận cơ chế khi **Tin cậy ≥ Trung bình** và **Truyền dẫn ≥ Vừa**

---

## 🛡️ Cải thiện độ bền vững số

### 1. Robust Z-Score với Winsorization

**Vấn đề:** FX/IB và các ngày shock có outliers rất lớn
**Giải pháp:** Clip outliers ở ±3σ trước khi tính mean/std

**Công thức:**
```pine
// Winsorization
mu0 = mean(src)
sd0 = stdev(src)
up = mu0 + 3 * sd0
dn = mu0 - 3 * sd0
xs = clamp(src, dn, up)  // Clip outliers

// Tính mean/std trên data đã clip
mu1 = mean(xs)
sd1 = stdev(xs)
z = (xs - mu1) / sd1
```

**Kết quả:**
- Giảm nhiễu outlier
- Z-score ổn định hơn
- Điểm áp lực nhảy mượt hơn

### 2. Smoothing Options

**smoothN = 3** (mặc định):
- Làm mượt thay đổi ngày bằng EMA(3)
- Giảm nhiễu nhưng giữ kịp thời gian thực

---

## 🐛 Fix quan trọng (P4)

### Vấn đề P4 trước v5.2

**Bug:** P4 đang dùng `scoreDrvShock_JP` (thuộc P1)
**Hậu quả:** P4 bị "nhiễu" bởi driver của P1 → Tín hiệu không chính xác

### Fix trong v5.2

**Đúng code:**
```pine
// P4 (v5.2)
impact_CRY = 0.40 * scoreExp_CRY +              // Dùng đúng CRY
              0.25 * scoreVN_press +
              0.20 * scoreR2_CRY +
              0.15 * scoreDrvShock_CRY              // Dùng CRY shock, KHÔNG phải JP shock
```

**Kết quả:**
- P4 độc lập hoàn toàn
- Không nhiễu từ P1
- Tín hiệu "Yên carry" chính xác

---

## 📊 So sánh v5.1 vs v5.2

| Tính năng | v5.1 | v5.2 |
|-----------|------|------|
| **Số panel** | 4-5 (tùy version) | 6 cố định |
| **OLS model** | Simple (y = βx) | Full (y = α + βx + ε) |
| **Expected/Residual** | Không rõ | Rõ ràng, nhất quán |
| **Quality layer** | Chỉ R² | R² + Coverage |
| **Robust z-score** | Không có | Có (winsorization) |
| **P4 bug** | Có bug | Đã fix |
| **UI** | Tiếng Anh / Lộn | Tiếng Việt 100% |
| **Beginner mode** | Không | Có (bảng đọc nhanh) |

---

## 🎯 Kênh sử dụng từng Panel

### P1 — Nhật (BOJ) → VN
**Khi dùng:**
- BOJ thay đổi chính sách (QQE, YCC, negative rates)
- Dòng vốn JPY đổ/rdòng từ VN
- JPY carry trade hoạt động mạnh

**Driver:** JP02Y hoặc JP10Y (mặc định: JP10Y)

---

### P2 — Toàn cầu → VN
**Khi dùng:**
- FED/ECB thay đổi lãi suất
- Global bonds sell-off (2022, 2023)
- Risk-on global → VN bị kéo lên

**Driver:** Composite 10Y (US + DE + GB + AU + CA)

---

### P3 — Đường cong → VN
**Khi dùng:**
- Flatten/Steepening curve toàn cầu
- Risk premium thay đổi
- Yield curve control (YCC) spread

**2 sub-channels:**
- Level: dG10 → dVN10
- Slope: dsG → dsVN

---

### P4 — Yên carry → VN
**Khi dùng:**
- Risk-off toàn cầu (VIX spike)
- JPY strengthen (flight to safety)
- Carry unwind (USDJPY down)

**Composite:** JPY mạnh + VIX lên + US2Y-JP2Y thu hẹp

---

### P5 — FX & Thanh khoản → VN
**Khi dùng:**
- USDVND biến động mạnh (SBV can thiệp)
- VNINBR lên xuống bất thường
- Thanh khoản thắt/chặt

**Composite:** USDVND (ROC) + VNINBR (bp change)

---

### P6 — Chuỗi truyền dẫn → VN (Mặc định)
**Khi dùng:**
- Mọi lúc (panel tổng hợp nhất)

**3 bước truyền dẫn:**
1. **Step A:** (US2Y + DXY) → USDVND
2. **Step B:** USDVND → VNINBR/IB
3. **Step C:** VNINBR/IB → VN10Y

**Metrics:**
- **Chain Strength:** Độ mạnh chuỗi (0-100)
- **Chain Shock:** Cường độ shock truyền qua chuỗi

---

## 📈 Performance Improvements

### Tính ổn định
- **Giảm nhiễu:** SmoothN = 3 (EMA)
- **Giảm outlier:** Winsorization ±3σ
- **Giảm nhảy dòng:** Stable z-score computation

### Độ tin cậy
- **Coverage check:** Tránh ảo giác khi thiếu data
- **Quality score:** Kết hợp R² + Coverage
- **Warning labels:** Thấp/TB/Cao

---

## 🔧 Technical Details

### Parameters (Mặc định - đã tối ưu)

```
Data:           Daily
LEN_Z:          252   // Lookback z-score
LEN_REG:        60    // Regression window
CLIP_Z:         3.0   // Winsorization threshold
smoothN:        3     // EMA smoothing
lagDriver:      1     // Lag driver (days)
```

### Tickers required

**VN:**
- TVC:VN10Y, TVC:VN02Y
- FX_IDC:USDVND
- ECONOMICS:VNINBR

**Nhật:**
- TVC:JP10Y, TVC:JP02Y
- FX_IDC:USDJPY

**Toàn cầu:**
- TVC:US10Y, TVC:US02Y
- TVC:DE10Y, TVC:DE02Y
- TVC:GB10Y, TVC:GB02Y
- TVC:AU10Y, TVC:CA10Y

**Risk:**
- TVC:DXY
- CBOE:VIX

---

## ⚠️ Known Limitations

1. **Endogeneity:** VN cũng tác động ngược lại global (hai chiều)
2. **Ticker availability:** Một số ticker có thể thiếu data theo vùng
3. **VNINBR proxy:** Không thay thế dữ liệu interbank chính thức
4. **Lag data:** Global data có thể nhanh hơn VN data

---

## 🚀 Migration Guide (từ v5.x → v5.2)

### Bước 1: Remove old version
```
Delete indicator: "Macro TP VN v5.1" (hoặc v5.0)
```

### Bước 2: Add new version
```
Add indicator: "Macro TP VN v5.2"
```

### Bước 3: Setup 6 panels
```
Add 6 lần, mỗi lần chọn panel khác:
- Instance 1: P1 BOJ→VN
- Instance 2: P2 Toàn cầu→VN
- Instance 3: P3 Đường cong→VN
- Instance 4: P4 Yên carry→VN
- Instance 5: P5 FX & Thanh khoản→VN
- Instance 6: P6 Chuỗi truyền dẫn→VN (default)
```

### Bước 4: Verify
```
Kiểm tra:
- Bảng hiển thị đủ 3 cột
- Điểm áp lực (0-100) running
- Background màu theo bucket
- Alerts hoạt động
```

---

## 📚 Documentation

- **README.md:** Hướng dẫn sử dụng chi tiết
- **RELEASE_NOTES.md:** File này (lịch sử phiên bản)
- **Pine Script Source:** Bond_Transmission_Monitor_v8.2.2.pine

---

## 🙏 Acknowledgments

- **MacroAcademic Framework:** Base regression và z-score methodology
- **TradingView Pine Script:** Platform thực thi
- **Global Finance Community:** Research về yield curve transmission

---

## 🔮 Roadmap (Future versions)

**v5.3 (Planned):**
- Thêm kênh commodities (gold, oil)
- Machine learning để optimize weights
- Backtest module

**v6.0 (Long-term):**
- Real-time alerts
- Cloud-based data storage
- Multi-market support

---

## 📞 Support & Feedback

Nếu bạn gặp bugs hoặc có đề xuất tính năng:
1. Kiểm tra **Troubleshooting** section trong README
2. Verify tickers có đủ data không
3. Report qua GitHub Issues

---

**Current Version:** v8.2.2
**Last Updated:** January 2025
**Status:** ✅ Stable & Production Ready

*Happy Monitoring! 📊🚀*
