# VnBondLab - Bộ Công Cụ Nghiên Cứu Thị Trường Việt Nam

## 🎯 Giới thiệu

**VnBondLab** là bộ công cụ phân tích tài chính chuyên sâu cho thị trường Việt Nam, được xây dựng trên TradingView Pine Script v5. Bộ công cụ tập trung vào 3 mảng chính:

- **Kinh tế vĩ mô** (Macro Economy)
- **Thị trường chứng khoán** (Equity Indices & Sectors)
- **Thị trường trái phiếu** (Bond Yield Curve)

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
- `MacroAcademic - VN Economy Engine v1.2.8` (Bản đầy đủ)
- `MacroAcademic_v4_4_Academic_Lite` (Bản tinh gọn)

📖 **Xem chi tiết:** [README MacroAcademic Engine](./01_MacroAcademic_Engine/)

---

### 📈 02_Indices_Research
**Chỉ báo nghiên cứu thị trường chứng khoán**

Phiên bản: v4.3 - v4.4 | Tác giả: Macro Research Team

**Mục đích:** Kết hợp phân tích vĩ mô với hành vi của:
- 6 chỉ số thị trường (VNINDEX, VN30, VN100, VNALLSHARE, VNMIDCAP, VNSMALLCAP)
- 11 ngành kinh tế (Finance, Industrials, IT, Real Estate, Consumer, Energy, Materials, Healthcare, Utilities, v.v.)

**2 dự án con:**

#### A. Macro Alert System v4.4 - Full
Hệ thống cảnh báo vĩ mô với 4 panel:
- Panel 1: Macro Weather Summary
- Panel 2: Market Regime Map (so sánh 6 indices)
- Panel 3: Sector Rotation Map (top/bottom industries)
- Panel 4: Transition Summary (ma trận chuyển đổi regime)

#### B. MacroAcademic_v4_3_Indices_Research_B.pine
Script B kết quả từ Script A (MacroAcademic Engine)
- Map Risk Score → hiệu suất indices theo regime
- Phân tích chi tiết từng bucket rủi ro

**Sử dụng khi:**
- Bạn muốn chọn chỉ số thị trường phù hợp với regime vĩ mô
- Bạn cần tìm ngành mạnh/yếu theo chu kỳ kinh tế
- Bạn muốn xây dựng chiến lược sector rotation

**File chính:**
- `Macro Alert System v4.4 - Full (Macro + Indices Research`
- `MacroAcademic_v4_3_Indices_Research_B.pine`

📖 **Xem chi tiết:** [README Indices Research](./02_Indices_Research/)

---

### 💰 03_YieldCurveLab
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
- `VN YieldCurveLab` (v1.6.9)

📖 **Xem chi tiết:** [README YieldCurveLab](./03_YieldCurveLab/)

---

## 🔄 Mối quan hệ giữa các dự án

```
┌──────────────────────────────────────┐
│   MacroAcademic Engine (Script A)    │
│   Kinh tế vĩ mô → Risk Score         │
└──────────────┬───────────────────────┘
               │
               ▼ Input
    ┌────────────────────────────────────┐
    │  Indices Research (Script B)        │
    │  Macro → Market/Sector Performance │
    └────────────────────────────────────┘

              YieldCurveLab (Standalone)
         Phân tích chuyên sâu trái phiếu
```

**Cách sử dụng kết hợp:**

1. **Bước 1:** Dùng **MacroAcademic Engine** để đánh giá bối cảnh vĩ mô
   - Kết quả: Risk Score B0-B4 (Ví dụ: B1 = Rủi ro thấp)

2. **Bước 2:** Dùng **Indices Research** để chọn chỉ số & ngành phù hợp
   - Nếu B1: Tăng tỷ trọng cyclical sectors (Finance, Industrials)
   - Nếu B4: Ưu tiên defensive sectors (Utilities, Healthcare)

3. **Bước 3:** Dùng **YieldCurveLab** để kiểm tra rủi ro hệ thống
   - Nếu YC4 + Slope inverted → Cảnh báo rủi ro chu kỳ cao
   - Nếu Stress High → Giảm đòn bẩy, tăng phòng thủ

---

## 🚀 Quick Start (Bắt đầu nhanh)

### Bạn là ai? Chọn dự án phù hợp:

#### 👤 Nhà đầu tư chứng khoán (Stock Investor)
**Bắt đầu với:** `02_Indices_Research/Macro Alert System v4.4`
- Xem nhanh: Panel 1 (Macro Weather)
- Quyết định: Panel 3 (Sector Rotation)

#### 👨‍💼 Quản lý danh mục (Portfolio Manager)
**Bắt đầu với:** `01_MacroAcademic_Engine/MacroAcademic v1.2.8`
- Sử dụng Risk Score để điều chỉnh asset allocation
- Kết hợp với Indices Research cho sector rotation

#### 📊 Bond Trader / Analyst
**Bắt đầu với:** `03_YieldCurveLab/VN YieldCurveLab`
- Theo dõi YC regime (YC1-YC4)
- Research Panel 3 để hiểu mối quan hệ bond → equity

#### 🎓 Researcher / Academic
**Dùng cả 3 dự án** để nghiên cứu:
- Macro-finance linkage
- Regime-based investing
- Sector rotation strategies

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

## 📊 So sánh nhanh các dự án

| Tiêu chí | MacroAcademic Engine | Indices Research | YieldCurveLab |
|----------|---------------------|------------------|---------------|
| **Phạm vi** | Kinh tế vĩ mô | Chứng khoán (indices + sectors) | Trái phiếu (yield curve) |
| **Input chính** | CPI, GDP, Policy rate, PPI, FX, Oil | Macro + 6 indices + 11 sectors | 1Y-10Y yields, Interbank |
| **Output** | Risk Score (B0-B4) | Market performance by regime | Stress indices, Correlation |
| **Số panel** | 7 | 4 | 3 |
| **User case** | Macro timing, Asset allocation | Sector rotation, Stock picking | Bond trading, Risk management |
| **Độ phức tạp** | Trung bình - Cao | Trung bình | Cao (Academic-focused) |
| **Thời gian sử dụng** | Hàng tuần/hàng tháng | Hàng ngày/hàng tuần | Hàng ngày |

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
- 📖 [MacroAcademic Engine README](./01_MacroAcademic_Engine/)
- 📖 [Indices Research README](./02_Indices_Research/)
- 📖 [YieldCurveLab README](./03_YieldCurveLab/)

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
- **2025-01-02:** Reorganize project structure into 3 main folders
- **Phiên bản hiện tại:** v1.0 (Initial release)

### Sub-projects:
- **MacroAcademic Engine:** v1.2.8 (PCTL Complete)
- **Indices Research:** v4.3 - v4.4 (Macro + Indices)
- **YieldCurveLab:** v1.6.9 (Academic Research Mode)

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

**🎯 Bắt đầu ngay:** Chọn dự án phù hợp với nhu cầu của bạn và xem README chi tiết trong từng thư mục!

*Happy Trading & Research!* 📊🚀
