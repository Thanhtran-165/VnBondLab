# MacroIndices Map v2.0.1 (Script B)

## 🎯 Tổng quan

**MacroIndices Map v2.0.1** (Script B) là công cụ mapping kết quả phân tích vĩ mô từ Script A (MacroAcademic Engine) sang hiệu suất của các chỉ số thị trường và ngành Việt Nam.

Đây là **Script B** trong hệ thống 2 script:
- **Script A**: MacroAcademic Engine (01_MacroAcademic_Engine) → Tạo Risk Score
- **Script B**: MacroIndices Map → Map Risk Score → Market Performance

Phiên bản: **v2.0.1 (Clean Fixed Build)**
Platform: TradingView Pine Script v5

---

## ✨ Tính năng chính

### 🔄 Macro Engine (Replicated from Script A)
Script B replicate toàn bộ macro engine từ Script A để tính toán:
- **Risk Score (0-100%)**: Tổng hợp 4 trụ cột vĩ mô
- **Risk Bucket (B0-B4)**: Phân loại rủi ro thành 5 mức

4 trụ cột vĩ mô:
1. **Căng thẳng thanh khoản** (Interbank - Policy)
2. **Độ dốc đường cong lợi suất** (10Y - 2Y)
3. **Chênh lệch quốc tế** (VN10Y - US10Y)
4. **Spread ngắn-dài** (10Y - Policy)

### 📊 Mapping Macro → Market Performance
Chuyển đổi Risk Score thành:
- **Average Returns**: R5, R20, R60 cho từng bucket
- **Win Rate**: Tỷ lệ thắng cho từng bucket
- **Max Drawdown**: DD20, DD60 cho từng bucket
- **Sample Size (N)**: Số lượng quan sát

---

## 📊 Dữ liệu đầu vào

### Macro Data (Replicated from Script A)
- `VNINTR`: Lãi suất chính sách
- `VN02Y`: Trái phiếu 2 năm
- `VN10Y`: Trái phiếu 10 năm
- `US10Y`: Trái phiếu Mỹ 10 năm
- `VNINBR`: Lãi suất liên ngân hàng

### Equity Data (HOSE Indices)
**Market Indices (6):**
- VNINDEX, VN30, VN100, VNALLSHARE, VNMIDCAP, VNSMALLCAP

**Sector Indices (11):**
- VNFIN, VNFINSELECT, VNIND, VNIT, VNREAL, VNCONS, VNCOND, VNENE, VNMAT, VNHEAL, VNUTI

---

## ⚙️ Cài đặt tham số

### Macro inputs (Giống Script A)
- **Macro timeframe**: Khung thời gian dữ liệu vĩ mô (khuyến nghị: D)
- **Chế độ ngưỡng**: Static/Dynamic/Percentile-based
- **Robust z-score**: Winsorization với clip_multiplier
- **Trọng số các trụ cột**: w_infl, w_pol, w_grow, w_drv

### Equity mapping & features
- **Equity timeframe**: Khung thời gian dữ liệu cổ phiếu
- **Return calculation**: Simple return hoặc Log return
- **Return clipping**: Giới hạn biên độ để giảm outliers
- **Min N để hiển thị**: Đảm bảo ý nghĩa thống kê

### Academic options
- **Log returns**: Sử dụng log return thay vì simple return
- **Clip returns**: Giới hạn biên độ return
- **Non-overlapping samples**: Mẫu không chồng lấn

---

## 🔧 Hướng dẫn sử dụng

### Workflow khuyến nghị:
1. **Bước 1**: Chạy Script A (MacroAcademic Engine) để hiểu bối cảnh vĩ mô
2. **Bước 2**: Chạy Script B (Indices Research Map) để xem mapping
3. **Bước 3**: Kết hợp thông tin để ra quyết định đầu tư

### Cách add vào TradingView:
1. Mở chart VNINDEX
2. Click "Indicators" → Search "MacroIndices Map"
3. Tùy chỉnh:
   - Chọn bucket để xem (hoặc Auto = bucket hiện tại)
   - Chọn indices/sectors quan tâm
   - Điều chỉnh tham số nếu cần

### Diễn giải kết quả
- **AvgR20 cao**: Bucket này có return trung bình tốt
- **Win20% cao**: Tỷ lệ thắng cao trong bucket này
- **AvgDD20 thấp**: Drawdown trung bình thấp (an toàn hơn)
- **N lớn**: Có đủ dữ liệu để tin cậy

---

## 📈 Ứng dụng thực tế

### 1. Chọn chỉ số phù hợp với regime
- Nếu bucket B0-B1: Tăng tỷ trọng midcap, smallcap
- Nếu bucket B3-B4: Tập trung vào VN30, blue-chip

### 2. Sector rotation
- So sánh AvgR20 giữa các sectors trong cùng bucket
- Chọn sector có:
  - AvgR20 cao
  - Win20% cao
  - AvgDD20 thấp

### 3. Risk management
- Tránh các indices có drawdown quá cao trong bucket hiện tại
- Điều chỉnh position size dựa trên historical performance

### 4. Backtest chiến lược
- Dùng historical data để test:
  - "Nếu tôi chỉ invest khi bucket = B0, return sẽ như thế nào?"
  - "Sector nào outperform trong từng bucket?"

---

## ⚠️ Lưu ý quan trọng

### Giới hạn
- Script B replicate macro engine từ Script A → có thể có sự khác biệt nhỏ
- Dữ liệu lịch sử hạn chế
- Past performance ≠ Future results

### Best Practices
1. **Luôn kết hợp với Script A**: Script B chỉ mapping, không thay thế Script A
2. **Check sample size (N)**: Tránh các bucket có N quá nhỏ
3. **Cross-validate**: So sánh với các phương pháp khác
4. **Forward testing**: Test trên dữ liệu real-time trước khi dùng real money

---

## 🔬 Tính năng học thuật

### 1. Robust z-score với winsorization
- Loại bỏ ảnh hưởng của outliers
- Clip_multiplier để kiểm soát độ nhạy

### 2. Return calculation options
- **Simple return**: Rt = (Pt - Pt-1) / Pt-1
- **Log return**: Rt = ln(Pt / Pt-1)
- **Clipped returns**: Giới hạn biên độ để giảm nhiễu

### 3. Sample adequacy
- Min N để đảm bảo ý nghĩa thống kê
- Cảnh báo khi N quá nhỏ

---

## 📊 So sánh Script A vs Script B

| Tiêu chí | Script A (MacroAcademic Engine) | Script B (Indices Map) |
|----------|-------------------------------|------------------------|
| **Mục tiêu** | Tạo Risk Score từ macro data | Map Risk Score → Market performance |
| **Input chính** | CPI, GDP, Policy rate, FX, Oil, PPI | Macro data + Indices + Sectors |
| **Output** | Risk Score (0-100%), Bucket (B0-B4) | AvgR, Win%, DD, N cho từng bucket |
| **Số panel** | 7 (P1-P7) | 1 (Market Regime Map) |
| **Use case** | Hiểu bối cảnh vĩ mô | Chọn indices/sectors phù hợp |

---

## 🔄 Workflow với Script A

```
┌─────────────────────────────────┐
│  Script A: MacroAcademic Engine │
│  - Input: CPI, GDP, Rates, FX   │
│  - Output: Risk Score (0-100)   │
│  - Bucket: B0, B1, B2, B3, B4   │
└──────────────┬──────────────────┘
               │ Risk Score
               ▼
┌─────────────────────────────────┐
│  Script B: Indices Research Map │
│  - Input: Risk Score + Indices  │
│  - Output: AvgR, Win%, DD by B  │
│  - Use: Select best indices     │
└─────────────────────────────────┘
```

---

## 📚 Tài liệu tham khảo

### Lý thuyết nền tảng
1. **Macro-finance linkage**: Mối quan hệ giữa biến số vĩ mô và thị trường chứng khoán
2. **Regime-based investing**: Đầu tư theo regime
3. **Conditional performance**: Hiệu suất có điều kiện theo regime

### Ứng dụng tại Việt Nam
- Độ nhạy của VN indices với lãi suất và thanh khoản
- Sector rotation theo chu kỳ tín dụng
- Impact of global factors (US10Y, USDVND)

---

## 🆘 Hỗ trợ và Troubleshooting

### Xử lý sự cố
1. **Không hiển thị dữ liệu**: Kiểm tra ticker và quyền truy cập
2. **Kết quả khác với Script A**: Normal (do replicate), có sự khác biệt nhỏ
3. **N quá nhỏ**: Cần nhiều dữ liệu lịch sử hơn

---

## 📝 Version History

- **v2.0.1**: Clean Fixed Build
- **v1.0**: Initial release - Script B với macro engine replication

---

## 🔗 Liên kết với các script khác

- **Script A**: [01_MacroAcademic_Engine](../01_MacroAcademic_Engine/)
- **Related**: [02_Macro_Alert_System](../02_Macro_Alert_System/)

---

**Tác giả**: Macro Research Team
**Platform**: TradingView Pine Script v5
**Thị trường**: HOSE - Việt Nam
**Last updated**: January 2025

*Disclaimer: Công cụ này chỉ phục vụ mục đích nghiên cứu, không phải là lời khuyên đầu tư.*
