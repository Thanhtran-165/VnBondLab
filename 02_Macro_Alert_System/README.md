# Macro Alert System v5.0.1 - Validated Regime Engine

## 🎯 Tổng quan

**Macro Alert System v5.0.1** là hệ thống cảnh báo vĩ mô toàn diện cho thị trường Việt Nam, kết hợp phân tích macro (lãi suất, thanh khoản, đường cong lợi suất) với nghiên cứu hành vi thị trường chứng khoán.

Phiên bản: **v5.0.1 - Validated Regime Engine (Clean)**
Platform: TradingView Pine Script v6

---

## ✨ Tính năng chính

### 🔔 Hệ thống cảnh báo 4 trụ cột vĩ mô

1. **Căng thẳng thanh khoản** (Interbank Rate - Policy Rate)
   - Phát hiện thanh khoản thắt/chặt
   - Cảnh báo rủi ro funding stress

2. **Độ dốc đường cong lợi suất** (VN10Y - VN02Y)
   - Theo dõi slope để dự báo chu kỳ
   - Cảnh báo inversion (đảo ngược)

3. **Chênh lệch lợi suất quốc tế** (VN10Y - US10Y)
   - Đánh giá áp lực từ dòng vốn ngoại
   - Cảnh báo rủi ro capital flight

4. **Spread ngắn-dài** (VN10Y - Policy Rate)
   - Đo lường độ thắt/chặt của chính sách
   - Taylor rule approximation

### 🎛️ 3 phương pháp xác định ngưỡng

- **Percentile-based**: So sánh với phân vị lịch sử (không giả định phân phối)
- **Dynamic (z-score)**: Chuẩn hóa với robust z-score (winsorized)
- **Static**: Sử dụng ngưỡng cố định (tùy chỉnh)

### 📊 Phân vùng Risk Bucket (0-100%)

- **B0 (0-20)**: Rủi ro rất thấp - Ease
- **B1 (20-40)**: Rủi ro thấp - Stable
- **B2 (40-60)**: Trung lập - Neutral
- **B3 (60-80)**: Rủi ro cao - Tightening
- **B4 (80-100)**: Căng thẳng - Danger

---

## 🖥️ 4 Panel hiển thị

### Panel 1 – Macro Weather Summary
- Tóm tắt tình hình vĩ mô hiện tại
- Trạng thái 4 trụ cột (Normal/Warning)
- Hiệu suất VNINDEX trong bucket hiện tại
- Hướng dẫn chi tiết từng bucket

### Panel 2 – Market Regime Map
- Bảng so sánh 6 chỉ số thị trường:
  - VNINDEX, VN30, VN100, VNALLSHARE, VNMIDCAP, VNSMALLCAP
- Số liệu thống kê:
  - AvgR20, Win20%, AvgR60
  - AvgDD20, N20
- Lọc theo bucket được chọn

### Panel 3 – Sector Rotation Map
- **Top 3** ngành outperforming (RR20 cao nhất)
- **Bottom 3** ngành underperforming (RR20 thấp nhất)
- Dựa trên Relative Return so với VNINDEX
- 11 ngành: Finance, Industrials, IT, Real Estate, Consumer, Energy, Materials, Healthcare, Utilities, Consumer Discretionary, Construction

### Panel 4 – Transition Summary
- Ma trận chuyển đổi giữa các bucket
- Xác suất: Tăng / Giữ nguyên / Giảm bucket
- Lợi nhuận trung bình khi chuyển bucket
- History tracking

---

## 📊 Dữ liệu đầu vào

### Macro Data (Source từ Script A)
- `VNINTR`: Lãi suất chính sách (ECONOMICS:VNINTR)
- `VN02Y`: Trái phiếu 2 năm (TVC:VN02Y)
- `VN10Y`: Trái phiếu 10 năm (TVC:VN10Y)
- `US10Y`: Trái phiếu Mỹ 10 năm (TVC:US10Y)
- `VNINBR`: Lãi suất liên ngân hàng (ECONOMICS:VNINBR)

### Equity Data (HOSE Indices)
**Market Indices (6):**
- VNINDEX, VN30, VN100, VNALLSHARE, VNMIDCAP, VNSMALLCAP

**Sector Indices (11):**
- VNFIN, VNFINSELECT, VNIND, VNIT, VNREAL, VNCONS, VNCOND, VNENE, VNMAT, VNHEAL, VNUTI

---

## ⚙️ Cài đặt tham số

### Macro inputs
- **Macro timeframe**: Khung thời gian dữ liệu vĩ mô (khuyến nghị: D)
- **Chế độ ngưỡng**: Static/Dynamic/Percentile-based
- **Robust mode**: Shock-sensitive / Fully-robust MAD
- **Trọng số các trụ cột**: Điều chỉnh influence của từng yếu tố

### Equity mapping & features
- **Equity timeframe**: Khung thời gian dữ liệu cổ phiếu
- **Tính toán các chỉ số**: R5, R20, R60, DD20, DD60
- **Min N để hiển thị**: Đảm bảo ý nghĩa thống kê

### Academic options (v5.0.1)
- **Log returns**: Sử dụng log return thay vì simple return
- **Clip returns**: Giới hạn biên độ return để giảm nhiễu
- **Non-overlapping samples**: Mẫu không chồng lấn cho research

---

## 🔧 Hướng dẫn sử dụng

### Cách add vào TradingView:
1. Mở chart VNINDEX hoặc bất kỳ chart nào
2. Click "Indicators" → Search "Macro Alert System v5.0.1"
3. Add indicator 4 lần (để có 4 panel)
4. Mỗi instance chọn panel khác nhau (1, 2, 3, 4)

### Lựa chọn Panel
- **Panel 1**: Tổng quan vĩ mô - phù hợp cho đánh giá nhanh
- **Panel 2**: Phân tích thị trường - so sánh các chỉ số
- **Panel 3**: Luân chuyển ngành - tìm ngành mạnh/yếu
- **Panel 4**: Phân tích chuyển đổi - dự báo xu hướng

### Diễn giải kết quả
- **Risk_pct cao (>60)**: Thận trọng, tăng tỷ trọng phòng thủ
- **Bucket ổn định**: Chiến lược momentum
- **Bucket chuyển đổi**: Điều chỉnh danh mục theo hướng chuyển
- **Sector RR cao**: Ngành có khả năng outperform

---

## 📈 Ứng dụng thực tế

### 1. Quản lý rủi ro vĩ mô
- Theo dõi risk_pct để điều chỉnh mức độ rủi ro danh mục
- Cảnh báo sớm khi các trụ cột vĩ mô chuyển xấu

### 2. Phân bổ tài sản
- Bucket 0-20: Tăng tỷ trọng cổ phiếu, cyclical sectors
- Bucket 80-100: Giảm tỷ trọng cổ phiếu, tăng defensive

### 3. Stock picking theo ngành
- Bucket rủi ro cao: Ưu tiên defensive (Utilities, Healthcare)
- Bucket rủi ro thấp: Ưu tiên cyclical (Finance, Industrials)

### 4. Timing thị trường
- Theo dõi transition matrix để dự báo chuyển đổi regime
- Kết hợp với phân tích kỹ thuật để xác định entry/exit

---

## ⚠️ Lưu ý quan trọng

### Giới hạn
- Dữ liệu lịch sử hạn chế cho thị trường VN
- Mô hình dựa trên tương quan lịch sử
- Độ trễ trong dữ liệu vĩ mô (CPI: tháng, GDP: quý)

### Best Practices
1. **Kết hợp nhiều phương pháp**: Không chỉ dựa vào một tín hiệu
2. **Backtest chiến lược**: Kiểm tra hiệu quả với dữ liệu lịch sử
3. **Quản lý rủi ro**: Luôn có stop-loss, không all-in
4. **Cập nhật thường xuyên**: Theo dõi và điều chỉnh tham số

---

## 🔬 Tính năng học thuật (Academic Features)

### 1. Robust z-score với winsorization
- Loại bỏ ảnh hưởng của outliers
- Clip multiplier để kiểm soát độ nhạy

### 2. Multiple threshold methods
- Percentile-based (phi tham số)
- Z-score (robust)
- Static (tùy chỉnh)

### 3. Log returns & return clipping
- Xử lý return distribution phù hợp hơn
- Giảm ảnh hưởng của các phiên biến động mạnh

---

## 📚 Tài liệu tham khảo

### Lý thuyết nền tảng
1. **Macro-finance linkage**: Mối quan hệ giữa biến số vĩ mô và thị trường chứng khoán
2. **Regime-based investing**: Đầu tư theo regime thay vì market timing
3. **Sector rotation**: Luân chuyển ngành theo chu kỳ kinh tế

### Ứng dụng tại Việt Nam
- Đặc thù thị trường VN: Độ nhạy cao với lãi suất và thanh khoản
- Cấu trúc ngành: Tập trung vào Banking, Real Estate
- Chu kỳ kinh tế: Gắn với chu kỳ tín dụng và bất động sản

---

## 🆘 Hỗ trợ và Troubleshooting

### Xử lý sự cố
1. **Không hiển thị dữ liệu**: Kiểm tra quyền truy cập dữ liệu (TradingView Premium)
2. **Kết quả bất thường**: Reset statistics, kiểm tra lại tham số
3. **Hiệu suất chậm**: Tắt các tính năng không cần thiết (R60, DD60)

---

## 📝 Version History

- **v5.0.1**: Validated Regime Engine (Clean) — Pine Script v6
- **v4.4**: Full edition với academic options, robust z-score, 4 panels
- **v4.3**: Beta version

---

**Tác giả**: Macro Research Team
**Platform**: TradingView Pine Script v5
**Thị trường**: HOSE - Việt Nam
**Last updated**: January 2025

*Disclaimer: Công cụ này chỉ phục vụ mục đích nghiên cứu, không phải là lời khuyên đầu tư.*
