# VN Bond Transmission Monitor — MacroAcademic FULL v5.2

## 🎯 Tổng quan

**VN Bond Transmission Monitor v5.2** là công cụ giám sát truyền dẫn trái phiếu Việt Nam tiên tiến, phân tích tác động từ thị trường nước ngoài (Nhật Bản, Mỹ, EU, Anh, Úc, Canada) sang thị trường trái phiếu VN thông qua 6 kênh truyền dẫn khác nhau.

Phiên bản: **v5.2 (PCTL Complete)**
Platform: TradingView Pine Script v5

---

## ✨ Tính năng chính

### 🔬 6 Panel Phân tích chuyên sâu

#### **P1: Nhật Bản (BOJ) → VN**
- Driver: Lợi suất Nhật Bản (JP02Y hoặc JP10Y)
- Phân tích tác động của chính sách BOJ
- Hồi quy OLS giữa driver Nhật và VN10Y
- Chỉ số: R², Impact Score, Decoupling Score

#### **P2: Trái phiếu toàn cầu → VN**
- Driver: Global 10Y (US + DE + GB + AU + CA)
- Tổng hợp tác động từ 5 nền kinh tế lớn
- Đánh giá áp lực toàn cầu lên VN
- Chỉ số: R², Expected Impact, Shock Score

#### **P3: Đường cong toàn cầu → VN**
- Driver: Level (Global 10Y) + Slope (Global 10Y-2Y)
- Phân tích tác động của flatten/steepening
- Chỉ số: R² curve, Decoupling, Combined Impact

#### **P4: Yên carry (risk-off) → VN**
- Driver: Yên strengthen (USDJPY) + VIX + US2Y-JP2Y spread
- Phân tích kênh "risk-off" toàn cầu
- Chỉ số: Carry index, R², Flight-to-safety score

#### **P5: FX & Thanh khoản → VN**
- Driver: USDVND + VNINBR (Interbank rate)
- Giám sát kênh tỷ giá và thanh khoản
- Chỉ số: Money conditions, Liquidity stress

#### **P6: Chuỗi truyền dẫn → VN (Mặc định)**
- 3 bước truyền dẫn:
  1. **Step A:** (US2Y + DXY) → USDVND
  2. **Step B:** USDVND → VNINBR
  3. **Step C:** VNINBR → VN10Y
- Chain Strength: Độ mạnh của chuỗi truyền dẫn
- Chain Shock: Sốc truyền dẫn qua 3 bước

---

## 📊 Dữ liệu đầu vào

### Việt Nam
- `VN10Y`: Lợi suất trái phiếu Việt Nam 10 năm
- `VN02Y`: Lợi suất trái phiếu Việt Nam 2 năm
- `USDVND`: Tỷ giá USD/VND
- `VNINBR`: Lãi suất liên ngân hàng Việt Nam

### Nhật Bản
- `JP10Y`: Lợi suất Nhật Bản 10 năm
- `JP02Y`: Lợi suất Nhật Bản 2 năm

### Toàn cầu
- `US10Y`, `US02Y`: Lợi suất Mỹ 10Y, 2Y
- `DE10Y`, `DE02Y`: Lợi suất Đức 10Y, 2Y
- `GB10Y`, `GB02Y`: Lợi suất Anh 10Y, 2Y
- `AU10Y`: Lợi suất Úc 10 năm
- `CA10Y`: Lợi suất Canada 10 năm

### FX & Risk
- `DXY`: Dollar Index
- `USDJPY`: Tỷ giá USD/JPY
- `VIX`: Chỉ số sợ (CBOE Volatility Index)

---

## ⚙️ Cấu hình & Tham số

### A) Chọn Panel
- **6 options**: P1-P6 (mỗi panel = 1 indicator instance)
- **Default**: P6 Chuỗi truyền dẫn→VN

### B) Nhật Bản (BOJ)
- **jpDriverChoice**: JP02Y hoặc JP10Y (default: JP10Y)

### C) Hồi quy (Academic)
- **lagDriver**: Độ trễ driver (0-20 ngày, default: 1)
- **LEN_REG**: Độ dài cửa sổ hồi quy (default: 60 ngày)

### D) Giảm nhiễu
- **smoothN**: EMA smoothing (1-20, default: 3)

### E) Hiển thị (UI)
- **beginnerMode**: Chế độ người mới (bảng đọc nhanh, default: true)
- **showComponents**: Hiện thêm 2 đường phụ (Dự tính/Tách biệt)
- **showBg**: Tô nền theo trạng thái
- **tablePos**: Vị trí bảng (4 options)

---

## 📈 Cách hoạt động

### 1️⃣ Thu thập dữ liệu
```pine
// Dữ liệu lợi suất (Daily)
yVN10, yVN02, yJP10, yJP02, yUS10, yUS02...
yG10 = mean(US10Y, DE10Y, GB10Y, AU10Y, CA10Y)  // Global composite
```

### 2️⃣ Tính toán thay đổi (bp/day)
```pine
dVN10  = change(VN10Y) * 100    // bp change
dJP10  = change(JP10Y) * 100
dUS02  = change(US02Y) * 100
dG10   = change(Global10Y) * 100
```

### 3️⃣ Hồi quy OLS
```pine
// Ví dụ: JP → VN
[corr, beta, alpha, r2, expY, resY] = f_reg_ols(dJP10, dVN10, LEN_REG)

// Trong đó:
- corr: Hệ số tương quan
- beta: Độ nhạy (slope)
- alpha: Intercept
- r2: Hệ số xác định (R²)
- expY: Giá trị dự tính (expected)
- resY: Phần dư (residual = decoupling)
```

### 4️⃣ Tính Impact Score
```pine
impact = 0.40 * scoreExp +         // Giá trị dự tính
          0.25 * scoreVN_press +    // Áp lực nội tại VN
          0.20 * scoreR2 +          // Độ mạnh truyền dẫn
          0.15 * scoreDrvShock      // Sốc từ driver
```

### 5️⃣ Phân loại trạng thái
- **B0 (0-35)**: Thuận lợi - Dễ hạ/nới lãi suất
- **B1 (35-50)**: Bình thường - Khả năng giữ ổn định
- **B2 (50-65)**: Cảnh giác - Khó hạ nhanh
- **B3 (65-80)**: Căng thẳng - Áp lực tăng mặt bằng
- **B4 (80-100)**: Sốc - Rất căng (rủi ro tăng mạnh)

---

## 🔧 Hướng dẫn sử dụng

### Cách add vào TradingView

1. **Mở chart** bất kỳ (khuyến nghị: VN10Y hoặc VNINDEX)
2. **Add indicator 6 lần** (để có 6 panel P1-P6)
3. **Mỗi instance chọn panel khác nhau**:
   - Instance 1: "P1 BOJ→VN"
   - Instance 2: "P2 Toàn cầu→VN"
   - Instance 3: "P3 Đường cong→VN"
   - Instance 4: "P4 Yên carry→VN"
   - Instance 5: "P5 FX & Thanh khoản→VN"
   - Instance 6: "P6 Chuỗi truyền dẫn→VN"

### Đọc bảng (Chế độ người mới)

#### Hàng "Kết luận"
- **Lãi suất**: Dễ hạ/nới / Giữ ổn định / Khó hạ / Áp lực tăng / Rất căng
- **Bị kéo theo**: Thấp / Vừa / Cao

#### Hàng "Bạn nên làm"
- **B0**: Có thể tăng rủi ro vừa phải
- **B1**: Quan sát thêm, chưa vội
- **B2**: Giữ kỷ luật, giảm rủi ro
- **B3**: Ưu tiên phòng thủ
- **B4**: Ưu tiên bảo toàn

#### Hàng "Số liệu nhanh"
- VN10Y hôm nay: +X bp (tăng) / -X bp (giảm)
- Driver hôm nay: +Y bp / -Y bp

#### Hàng "Tin cậy / Truyền dẫn"
- **Tin cậy**: Cao / Trung bình / Thấp
- **Truyền dẫn**: Mạnh / Vừa / Yếu

---

## 📊 Ứng dụng thực tế

### 1. Phát hiện tác động nước ngoài

**Ví dụ P1 (Nhật → VN):**
- Nếu JP10Y tăng 10bp → VN10Y dự tính tăng 5bp
- Nếu VN chỉ tăng 2bp → Decoupling (VN không bị kéo theo)
- Nếu VN tăng 8bp → Coupling (VN bị kéo theo mạnh)

**Ví dụ P6 (Chuỗi truyền dẫn):**
```
US2Y ↑ 10bp → DXY ↑ → USDVND ↑ → VNINBR ↑ → VN10Y ↑
   ↓            ↓         ↓          ↓          ↓
Step A       Step A     Step B     Step B     Step C
```

### 2. Timing giao dịch trái phiếu

**Khi B0-B1 (Thuận lợi/Bình thường):**
- Có thể mua TPCP trái phiếu dài hạn
- Lợi suất thấp → Giá trái phiếu cao

**Khi B3-B4 (Căng thẳng/Sốc):**
- Cân nhắc bán hoặc giảm duration
- Lợi suất cao → Giá trái phiếu thấp
- Chờ cơ hội mua lại khi降压

### 3. Dự báo chính sách SBV

**Khi P5 (FX & Thanh khoản) báo đỏ:**
- USDVND tăng mạnh + VNINBR tăng
- SBV có thể:
  - Hóa đơn USD vào thị trường (đập giá USDVND)
  - Tăng lãi suất (hút vốn về VND)
  - Cắt giảm room tín dụng

**Khi P6 (Chuỗi truyền dẫn) báo đỏ:**
- Áp lực từ FED (US2Y) truyền sang VN
- SBV có thể phải điều chỉnh lãi suất để giữ ổn định

### 4. So sánh độ nhạy của VN

**Độ nhạy với các driver:**
- R² cao (>40%) → Rất nhạy, bị kéo theo mạnh
- R² trung bình (20-40%) → Vừa phải
- R² thấp (<20%) → Ít bị ảnh hưởng

**Decoupling Score:**
- Cao (>75) → Nội lực trội, ít bị kéo theo
- Trung bình (60-75) → Pha trộn nội lực + ngoại lực
- Thấp (<60) → Ngoại lực trội, bị kéo theo mạnh

---

## 🔬 Tính năng học thuật (Academic Features)

### 1. OLS Regression với Intercept
```pine
y = α + βx + ε

Trong đó:
- α (alpha): Intercept
- β (beta): Slope (độ nhạy)
- ε (epsilon): Residual (decoupling)
- R²: Hệ số xác định
```

### 2. Robust Z-Score (Winsorization)
- Clip outliers ở ±3σ
- Tính mean/std trên data đã clip
- Giảm ảnh hưởng của các ngày biến động bất thường

### 3. Coverage (Độ phủ dữ liệu)
```pine
coverage = % ngày có dữ liệu không NA
```
- Tránh ảo giác thống kê khi thiếu dữ liệu
- Quality score = 0.6 × R² + 0.4 × Coverage

### 4. Chain Strength (P6)
```pine
ChainStrength = 0.33 × R²(A) + 0.33 × R²(B) + 0.34 × R²(C)
```
- Đo lường độ mạnh của chuỗi 3 bước
- Chuỗi mạnh → Truyền dẫn tốt
- Chuỗi yếu → Truyền dẫn kém

---

## 📈 Ví dụ thực tế

### Ví dụ 1: FED tăng lãi suất (P6)

**Kịch bản:**
- US2Y tăng 15bp → DXY tăng → USDVND tăng 0.5% → VNINBR tăng 10bp → VN10Y tăng 8bp

**Kết quả:**
- Chain Strength: 75% (Cao)
- Impact Score: 82 (B4 - Sốc)
- Kết luận: Rất căng, rủi ro tăng mạnh

**Hành động:**
- Giảm duration danh mục trái phiếu
- Chờ VN10Y tăng xong rồi mua lại
- Hoặc mua TPCP ngắn hạn

### Ví dụ 2: BOJ nới lãi suất (P1)

**Kịch bản:**
- JP10Y giảm 5bp → VN10Y dự tính giảm 2bp
- VN10Y thực tế giảm 1bp → Decoupling nhẹ

**Kết quả:**
- R²: 30% (Vừa)
- Decoupling Score: 65 (Vừa bị kéo theo)
- Impact: 45 (B1 - Bình thường)

**Hành động:**
- Không cần vội goldng
- Quan sát thêm P2, P6

---

## ⚠️ Lưu ý quan trọng

### Giới hạn
- **Lag dữ liệu:** Dữ liệu nước ngoài có thể nhanh hơn VN
- **Gap trading:** Có thể arbitrage tạm thời
- **R² không cao:** Không phải lúc nào truyền dẫn cũng mạnh

### Best Practices
1. **Xem cả 6 panel:** Không chỉ dựa vào 1 kênh
2. **Kiểm tra Quality:** Tin cậy phải ≥50%
3. **So sánh cross-check:** P1 vs P2, P3 vs P5
4. **Theo dõi xu hướng:** Hôm nay tốt hơn/xấu hơn hôm qua

---

## 📚 Tài liệu tham khảo

### Lý thuyết nền tảng
1. **Yield curve transmission**: Cơ chế truyền dẫn lợi suất giữa các quốc gia
2. **Interest rate parity:** Mối quan hệ lãi suất - tỷ giá
3. **Global financial cycle:** Chu kỳ tài chính toàn cầu
4. **Spillover effects:** Hiệu ứng lan truyền từ thị trường developed → emerging

### Ứng dụng tại Việt Nam
- VN là thị trường **frontier** → Nhạy với global flows
- SBV quản lý tỷ giá → Có biên độ điều chỉnh
- Thanh khoản nội địa → Có thể buffer bớt external shocks

---

## 🆘 Troubleshooting

### Vấn đề 1: Không hiển thị dữ liệu
- **Nguyên nhân:** Ticker không có quyền truy cập
- **Khắc phục:** Kiểm tra TradingView Premium, đổi ticker tương đương

### Vấn đề 2: R² quá thấp (<10%)
- **Nguyên nhân:** Không có mối quan hệ trong giai đoạn này
- **Khắc phục:** Đừng buộc phải dùng kênh đó, chuyển sang kênh khác

### Vấn đề 3: Impact Score nhảy liên tục
- **Nguyên nhân:** Dữ liệu nhiễu, smoothN quá thấp
- **Khắc phục:** Tăng smoothN lên 5-10

---

## 📝 Version History

- **v5.2** (2025): Full edition với 6 panels, default tối ưu
- Trước đó: Các bản beta v4.x, v5.0, v5.1

---

## 🔗 Liên kết với các dự án khác

- **01_MacroAcademic_Engine**: Phân tích vĩ mô VN
- **04_YieldCurveLab**: Đường cong lợi suất VN
- **05_Bond_Transmission_Monitor** (Dự án này): Truyền dẫn nước ngoài → VN

**Gợi ý sử dụng:**
1. Dùng **01** để hiểu bối cảnh vĩ mô VN
2. Dùng **04** để hiểu YC VN
3. Dùng **05 (P1-P6)** để hiểu tác động nước ngoài lên VN

---

**Tác giả:** MacroAcademic Team
**Platform:** TradingView Pine Script v5
**Thị trường:** HOSE - Việt Nam
**Last updated:** January 2025

*Disclaimer: Công cụ này chỉ phục vụ mục đích nghiên cứu, không phải là lời khuyên đầu tư.*
