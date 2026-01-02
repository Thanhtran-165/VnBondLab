# VnBondLab - Bộ Công Cụ Nghiên Cứu Thị Trường Việt Nam

## 🎯 Giới thiệu

**VnBondLab** là bộ công cụ phân tích tài chính chuyên sâu cho thị trường Việt Nam, được xây dựng trên TradingView Pine Script v5. Bộ công cụ gồm **4 dự án độc lập**:

- **01_MacroAcademic_Engine**: Phân tích vĩ mô & Risk Score
- **02_Macro_Alert_System**: Hệ thống cảnh báo vĩ mô
- **03_Indices_Research_Map**: Mapping vĩ mô → Thị trường chứng khoán
- **04_YieldCurveLab**: Nghiên cứu đường cong lợi suất trái phiếu

Mỗi dự án được thiết kế độc lập nhưng có thể sử dụng kết hợp để có góc nhìn đa chiều về thị trường.

---

## 📁 Tổng quan các dự án

### 📊 01_MacroAcademic_Engine
**Dashboard phân tích vĩ mô Việt Nam**

Phiên bản: v1.2.8 | Tác giả: MacroAcademic

**Mục đích:** Đánh giá sức khỏe kinh tế Việt Nam qua 4 trụ cột chính:
- Lạm phát (Inflation)
- Lãi suất & Thanh khoản (Interest Rates & Liquidity)
- Tăng trưởng (GDP Growth)
- Yếu tố chi phí & ngoại lực (Cost Push & External Forces)

**Kết quả:** Risk Score (0-100%) và Bucket (B0-B4) để xác định mức độ rủi ro vĩ mô

**Sử dụng khi:**
- Bạn cần đánh giá tổng quan về sức khỏe kinh tế
- Bạn muốn timing cho asset allocation (stocks/bonds/cash)
- Bạn cần hiểu bối cảnh vĩ mô trước khi quyết định đầu tư

**File chính:**
- `MacroAcademic_Engine_v1.2.8_Full.pine` (Bản đầy đủ)
- `MacroAcademic_Engine_v1.2.8_Lite.pine` (Bản tinh gọn)

📖 **Xem chi tiết:** [README MacroAcademic Engine](./01_MacroAcademic_Engine/)

---

### 🔔 02_Macro_Alert_System
**Hệ thống cảnh báo vĩ mô toàn diện**

Phiên bản: v4.4 - Full | Tác giả: Macro Research Team

**Mục đích:** Hệ thống cảnh báo rủi ro vĩ mô với phân tích 4 trụ cột:
- Căng thẳng thanh khoản (Interbank - Policy Rate)
- Độ dốc đường cong lợi suất (VN10Y - VN02Y)
- Chênh lệch quốc tế (VN10Y - US10Y)
- Spread ngắn-dài (VN10Y - Policy Rate)

**4 Panel chuyên biệt:**
- **Panel 1**: Macro Weather Summary
- **Panel 2**: Market Regime Map (so sánh 6 indices)
- **Panel 3**: Sector Rotation Map (top/bottom industries)
- **Panel 4**: Transition Summary (ma trận chuyển đổi regime)

**Sử dụng khi:**
- Bạn cần cảnh báo sớm rủi ro vĩ mô
- Bạn muốn so sánh hiệu suất 6 indices theo regime
- Bạn cần tìm ngành mạnh/yếu theo chu kỳ kinh tế

**File chính:**
- `Macro_Alert_System_v4.4.pine`

📖 **Xem chi tiết:** [README Macro Alert System](./02_Macro_Alert_System/)

---

### 📈 03_Indices_Research_Map
**Mapping vĩ mô → Hiệu suất thị trường (Script B)**

Phiên bản: v1.0 | Tác giả: Macro Research Team

**Mục đích:** Script B trong hệ thống 2 script, map Risk Score từ Script A sang hiệu suất thị trường:
- Replicate Macro Engine từ Script A
- Mapping Risk Score → Average Returns, Win Rate, Drawdown
- Phân tích chi tiết theo bucket (B0-B4)

**Kết hợp với:**
- 6 chỉ số thị trường: VNINDEX, VN30, VN100, VNALLSHARE, VNMIDCAP, VNSMALLCAP
- 11 ngành kinh tế: Finance, Industrials, IT, Real Estate, Consumer, Energy, Materials, Healthcare, Utilities, v.v.

**Sử dụng khi:**
- Bạn đã chạy Script A và có Risk Score
- Bạn muốn chọn indices/sectors phù hợp với regime hiện tại
- Bạn cần backtest chiến lược theo bucket

**File chính:**
- `Indices_Research_Map_v1.0.pine`

📖 **Xem chi tiết:** [README Indices Research Map](./03_Indices_Research_Map/)

---

### 💰 04_YieldCurveLab
**Laboratory nghiên cứu đường cong lợi suất trái phiếu**

Phiên bản: v1.6.9 | Tác giả: VnBondLab

**Mục đích:** Phân tích sâu đường cong lợi suất Việt Nam (1Y/2Y/3Y/5Y/7Y/10Y)

**3 khối phân tích chính:**
1. **Shape & Regime:** Level, Slope, Curve, Classification (YC0-YC4)
2. **Quality & Distortion:** Đánh giá độ "khỏe" của dữ liệu (HIGHQ/MEDQ/LOWQ)
3. **Research vs VNINDEX:** Tương quan, Beta, R² giữa Stress và thị trường cổ phiếu

**3 Panel:**
- Panel 1: Shape Dashboard (tổng quan YC)
- Panel 2: Grid (bảng lưới theo kỳ hạn)
- Panel 3: Diagnostics + Research (thống kê học thuật)

**Sử dụng khi:**
- Bạn là bond trader hoặc quan tâm đến thị trường trái phiếu
- Bạn muốn dự báo rủi ro hệ thống từ YC inversion
- Bạn cần nghiên cứu mối quan hệ bond → equity

**File chính:**
- `VN_YieldCurveLab_v1.6.9.pine`

📖 **Xem chi tiết:** [README YieldCurveLab](./04_YieldCurveLab/)

---

## 🔄 Mối quan hệ giữa các dự án

```
┌──────────────────────────────────────┐
│   01_MacroAcademic Engine (Script A) │
│   Kinh tế vĩ mô → Risk Score         │
└──────────────┬───────────────────────┘
               │
               ├──────────────────────────┐
               ▼                          ▼
    ┌────────────────────────┐  ┌───────────────────────────┐
    │ 02_Macro Alert System  │  │ 03_Indices Research Map   │
    │ Cảnh báo vĩ mô 4 panel │  │ (Script B) Map→Indices    │
    └────────────────────────┘  └───────────────────────────┘

              04_YieldCurveLab (Standalone)
         Phân tích chuyên sâu trái phiếu
```

**Cách sử dụng kết hợp:**

**Workflow 1: TỔNG QUAN VĨ MÔ + CẢNH BÁO**
1. **Bước 1:** Dùng **01_MacroAcademic Engine** để đánh giá bối cảnh vĩ mô
   - Kết quả: Risk Score B0-B4 (Ví dụ: B1 = Rủi ro thấp)
2. **Bước 2:** Dùng **02_Macro Alert System** để có cảnh báo chi tiết
   - 4 Panel: Tổng quan, Market Map, Sector Rotation, Transition
   - Nếu B1: Tăng tỷ trọng cyclical sectors (Finance, Industrials)
   - Nếu B4: Ưu tiên defensive sectors (Utilities, Healthcare)

**Workflow 2: MAPPING VĨ MÔ → THỊ TRƯỜNG**
1. **Bước 1:** Dùng **01_MacroAcademic Engine** (Script A) → Risk Score
2. **Bước 2:** Dùng **03_Indices Research Map** (Script B) → Map Risk Score → Indices performance
   - Xem AvgR, Win%, DD cho từng bucket
   - Chọn indices/sectors phù hợp với regime hiện tại

**Workflow 3: PHÂN TÍCH SÂU TRÁI PHIẾU**
1. Dùng **04_YieldCurveLab** độc lập hoặc kết hợp với 01
   - Nếu YC4 + Slope inverted → Cảnh báo rủi ro chu kỳ cao
   - Nếu Stress High → Giảm đòn bẩy, tăng phòng thủ

---

## 🚀 Quick Start (Bắt đầu nhanh)

### Bạn là ai? Chọn dự án phù hợp:

#### 👤 Nhà đầu tư chứng khoán (Stock Investor)
**Bắt đầu với:** `02_Macro_Alert_System`
- Xem nhanh: Panel 1 (Macro Weather)
- Quyết định: Panel 3 (Sector Rotation)
- Sau đó dùng `03_Indices_Research_Map` để chọn chỉ số phù hợp

#### 👨‍💼 Quản lý danh mục (Portfolio Manager)
**Bắt đầu với:** `01_MacroAcademic_Engine`
- Sử dụng Risk Score để điều chỉnh asset allocation
- Kết hợp `02_Macro_Alert_System` cho cảnh báo chi tiết
- Dùng `03_Indices_Research_Map` để chọn indices/sectors

#### 📊 Bond Trader / Analyst
**Bắt đầu với:** `04_YieldCurveLab`
- Theo dõi YC regime (YC1-YC4)
- Research Panel 3 để hiểu mối quan hệ bond → equity
- Kết hợp với `01_MacroAcademic_Engine` để hiểu bối cảnh vĩ mô

#### 🎓 Researcher / Academic
**Dùng cả 4 dự án** để nghiên cứu:
- Macro-finance linkage (01 + 03)
- Regime-based investing (01 + 02 + 03)
- Sector rotation strategies (02 + 03)
- Yield curve theory (04)

---

## 📋 Cài đặt cơ bản (TradingView)

### Yêu cầu:
- **TradingView:** Tài khoản Free (cơ bản) hoặc Premium (để truy cập dữ liệu Economics)
- **Dữ liệu:** Các ticker Economics và HOSE indices
- **Timeframe:** Khuyến nghị D (Daily)

### Cách sử dụng:

1. **Mở chart** bất kỳ trên TradingView (khuyến nghị: VNINDEX)
2. **Add indicator:** Click "Indicators" → Search tên script
3. **Thêm nhiều instance:** Để xem nhiều panel, add cùng indicator nhiều lần
4. **Chọn panel:** Mỗi instance chọn 1 panel khác nhau (1, 2, 3...)

---

## 📊 So sánh nhanh 4 dự án

| Tiêu chí | 01_MacroAcademic Engine | 02_Macro Alert System | 03_Indices Research Map | 04_YieldCurveLab |
|----------|------------------------|----------------------|------------------------|------------------|
| **Phạm vi** | Kinh tế vĩ mô | Cảnh báo vĩ mô | Mapping vĩ mô → CK | Trái phiếu |
| **Input chính** | CPI, GDP, Rates, FX, Oil | Macro + Indices + Sectors | Macro + 6 indices + 11 sectors | 1Y-10Y yields |
| **Output** | Risk Score (0-100) | 4 Panel cảnh báo | AvgR, Win%, DD by bucket | Stress, Correlation |
| **Số panel** | 7 | 4 | 1 | 3 |
| **User case** | Asset allocation | Cảnh báo rủi ro | Chọn indices/sectors | Bond trading |
| **Độ phức tạp** | Trung bình - Cao | Trung bình | Trung bình | Cao (Academic) |
| **Thời gian** | Hàng tuần/tháng | Hàng ngày/tuần | Khi có Risk Score | Hàng ngày |

---

## ⚠️ Lưu ý quan trọng

### Giới hạn:
- Dữ liệu lịch sử hạn chế cho thị trường Việt Nam
- Mô hình dựa trên tương quan lịch sử, không đảm bảo kết quả tương lai
- Độ trễ trong dữ liệu vĩ mô (CPI: tháng, GDP: quý)
- Cần TradingView Premium để truy cập đầy đủ dữ liệu Economics

### Best Practices:
1. **Kết hợp nhiều phương pháp:** Không chỉ dựa vào một tín hiệu duy nhất
2. **Backtest:** Kiểm tra hiệu quả với dữ liệu lịch sử trước khi dùng real money
3. **Quản lý rủi ro:** Luôn có stop-loss, không all-in
4. **Cập nhật:** Theo dõi và điều chỉnh tham số theo thị trường

---

## 🔬 Tính năng học thuật (Academic Features)

Tất cả các dự án đều được xây dựng với các chuẩn mực học thuật:

- **Robust statistics:** Z-score có winsorization, Percentile-based (phi tham số)
- **Sample adequacy:** EffN (Effective Sample Size) để tránh ảo giác thống kê
- **Regime analysis:** Phân tích theo chế độ (YC4, B0-B4, v.v.)
- **Multiple-testing control:** Lag Stability check để tránh overfit
- **Quality gating:** Loại bỏ giai đoạn dữ liệu nhiễu (LOWQ)

---

## 📚 Tài liệu & Hướng dẫn

### Documentation:
- 📖 [01_MacroAcademic_Engine README](./01_MacroAcademic_Engine/)
- 📖 [02_Macro_Alert_System README](./02_Macro_Alert_System/)
- 📖 [03_Indices_Research_Map README](./03_Indices_Research_Map/)
- 📖 [04_YieldCurveLab README](./04_YieldCurveLab/)

### Tài liệu tham khảo:
- **Macro-finance linkage:** Mối quan hệ giữa biến số vĩ mô và thị trường tài sản
- **Regime-based investing:** Đầu tư theo chế độ thay vì market timing
- **Sector rotation:** Luân chuyển ngành theo chu kỳ kinh tế
- **Yield curve analysis:** Đường cong lợi suất như chỉ báo dự báo

---

## 🆘 Hỗ trợ & Đóng góp

### Xử lý sự cố thường gặp:
1. **Không hiển thị dữ liệu:** Kiểm tra ticker và quyền truy cập TradingView Premium
2. **Kết quả bất thường:** Reset statistics, kiểm tra lại tham số
3. **Hiệu suất chậm:** Tắt bớt panel hoặc giảm window length

### Đóng góp:
- Report bugs và đề xuất tính năng
- Chia sẻ backtest results
- Cộng tác nghiên cứu các mô hình mới

---

## 📝 Version History

### Main Repository:
- **2025-01-02:** Reorganize into 4 independent projects
- **2025-01-02:** Add comprehensive README and documentation
- **Phiên bản hiện tại:** v2.0 (4 Projects Structure)

### Sub-projects:
- **01_MacroAcademic_Engine:** v1.2.8 (PCTL Complete)
- **02_Macro_Alert_System:** v4.4 (Full Edition)
- **03_Indices_Research_Map:** v1.0 (Script B)
- **04_YieldCurveLab:** v1.6.9 (Academic Research Mode)

---

## 👥 Tác giả & Liên hệ

**Tác giả:** Macro Research Team & VnBondLab
**Nền tảng:** TradingView Pine Script v5
**Thị trường:** HOSE - Việt Nam
**Ngày cập nhật:** January 2025

---

## 📜 License

*Disclaimer: Công cụ này chỉ phục vụ mục đích nghiên cứu và giáo dục, không phải là lời khuyên đầu tư. Nhà đầu tư cần tự chịu trách nhiệm với quyết định của mình.*

---

## 💖 Donate / Ủng hộ

Nếu bạn tìm thấy các công cụ này hữu ích và muốn ủng hộ dự án, tôi rất trân trọng sự đóng góp của bạn!

### 📱 Momo / QR Code

![Donate QR Code](assets/donate_qr.jpg)

**Hoặc quét mã QR:**

```
┌─────────────────────┐
│                     │
│   [QR CODE HERE]    │
│                     │
└─────────────────────┘
```

### 💳 Thông tin chuyển khoản

- **Ngân hàng:** [Tên ngân hàng]
- **Số tài khoản:** [Số tài khoản]
- **Chủ tài khoản:** [Tên chủ tài khoản]

### 🎁 Mục đích Donate

Ủng hộ của bạn sẽ được sử dụng để:
- Phí维护 và phát triển thêm tính năng mới
- Nâng cấp server và tài nguyên
- Cập nhật dữ liệu định kỳ
- Phát triển thêm các công cụ phân tích khác

### 🙏 Cảm ơn

Cảm ơn bạn đã sử dụng và ủng hộ VnBondLab! Mọi sự đóng góp dù nhỏ đều rất quý giá! 💝

---

**🎯 Bắt đầu ngay:** Chọn dự án phù hợp với nhu cầu của bạn và xem README chi tiết trong từng thư mục!

*Happy Trading & Research!* 📊🚀
