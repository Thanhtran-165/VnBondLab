# Macro → VN Indices Research (Script B) - README

## 🎯 Tổng quan

**MacroIndices Map v1.0** là một chỉ báo nghiên cứu chuyên sâu cho thị trường chứng khoán Việt Nam, kết hợp phân tích macro (lãi suất, thanh khoản) với hành vi của các chỉ số thị trường và ngành. Công cụ này giúp nhà đầu tư hiểu rõ mối quan hệ giữa điều kiện vĩ mô và hiệu suất của các nhóm tài sản khác nhau.

## ✨ Tính năng chính

### 1. **Hệ thống Macro Risk Engine**
- Đánh giá 4 trụ cột vĩ mô:
  - **Căng thẳng thanh khoản** (Interbank Rate - Policy Rate)
  - **Độ dốc đường cong lợi suất** (10Y - 2Y)
  - **Chênh lệch lợi suất quốc tế** (VN10Y - US10Y)
  - **Spread ngắn-dài** (10Y - Policy Rate)
- 3 phương pháp xác định ngưỡng:
  - **Percentile-based**: So sánh với phân vị lịch sử
  - **Dynamic (z-score)**: Chuẩn hóa với z-score robust
  - **Static**: Sử dụng ngưỡng cố định

### 2. **Phân vùng Risk Bucket (0-100%)**
- **B0 (0-20)**: Rủi ro rất thấp
- **B1 (20-40)**: Rủi ro thấp/ổn định
- **B2 (40-60)**: Trung lập
- **B3 (60-80)**: Rủi ro cao
- **B4 (80-100)**: Căng thẳng/nguy hiểm

### 3. **4 Panel hiển thị thông minh**

#### **Panel 1 – Macro Weather Summary**
- Tóm tắt tình hình vĩ mô hiện tại
- Trạng thái 4 trụ cột (Bình thường/Cảnh báo)
- Hiệu suất VNINDEX trong bucket hiện tại
- Hướng dẫn chi tiết các bucket

#### **Panel 2 – Market Regime Map**
- Bảng so sánh 6 chỉ số thị trường:
  - VNINDEX, VN30, VN100, VNALLSHARE, VNMIDCAP, VNSMALLCAP
- Số liệu: AvgR20, Win20%, AvgR60, AvgDD20, N20
- Lọc theo bucket được chọn

#### **Panel 3 – Sector Rotation Map**
- Top 3/Bottom 3 ngành outperforming/underperforming
- Dựa trên Relative Return (RR20) so với benchmark VNINDEX
- 11 ngành: Finance, Industrials, IT, Real Estate, Consumer, Energy, Materials, Healthcare, Utilities

#### **Panel 4 – Transition Summary**
- Ma trận chuyển đổi giữa các bucket
- Xác suất tăng/giữ nguyên/giảm bucket
- Lợi nhuận trung bình khi chuyển bucket

## 📊 Dữ liệu đầu vào

### Macro Data (Từ Script A)
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

## ⚙️ Cài đặt tham số

### Nhóm: Macro inputs
- **Macro timeframe**: Khung thời gian dữ liệu vĩ mô (khuyến nghị: D)
- **Chế độ ngưỡng**: Static/Dynamic/Percentile-based
- **Trọng số các trụ cột**: Điều chỉnh ảnh hưởng của từng yếu tố
- **Tham số phân vị/z-score**: Tuỳ chỉnh độ nhạy cảnh báo

### Nhóm: Equity mapping & features
- **Equity timeframe**: Khung thời gian dữ liệu cổ phiếu
- **Tính toán các chỉ số**: R5, R20, R60, DD20, DD60
- **Min N để hiển thị**: Đảm bảo ý nghĩa thống kê

### Nhóm: View / Bucket
- **Bucket view**: Auto current hoặc chọn bucket cụ thể
- **Hiển thị cột**: Tuỳ chọn hiển thị các chỉ số trong bảng

### Nhóm: Academic options
- **Log returns**: Sử dụng log return thay vì simple return
- **Clip returns**: Giới hạn biên độ return để giảm nhiễu
- **Non-overlapping samples**: Mẫu không chồng lấn cho nghiên cứu học thuật

## 🔧 Hướng dẫn sử dụng

### 1. Cài đặt cơ bản
```pinescript
// Thêm script vào biểu đồ TradingView
// Đảm bảo có quyền truy cập dữ liệu VNINTR, VN02Y, VN10Y, US10Y, VNINBR
```

### 2. Lựa ch Panel hiển thị
- **Panel 1**: Tổng quan vĩ mô - phù hợp cho đánh giá nhanh
- **Panel 2**: Phân tích thị trường - so sánh các chỉ số
- **Panel 3**: Luân chuyển ngành - tìm ngành mạnh/yếu
- **Panel 4**: Phân tích chuyển đổi - dự báo xu hướng

### 3. Diễn giải kết quả
- **Risk_pct cao (>60)**: Thận trọng, tăng tỷ trọng phòng thủ
- **Bucket ổn định**: Chiến lược momentum
- **Bucket chuyển đổi**: Điều chỉnh danh mục theo hướng chuyển
- **Sector RR cao**: Ngành có khả năng outperform

## 📈 Ứng dụng thực tế

### 1. **Quản lý rủi ro vĩ mô**
- Theo dõi risk_pct để điều chỉnh mức độ rủi ro danh mục
- Cảnh báo sớm khi các trụ cột vĩ mô chuyển sang trạng thái xấu

### 2. **Phân bổ tài sản**
- Bucket 0-20: Tăng tỷ trọng cổ phiếu, tập trung vào cyclical sectors
- Bucket 80-100: Giảm tỷ trọng cổ phiếu, tăng phòng thủ

### 3. **Stock picking theo ngành**
- Trong bucket rủi ro cao: Ưu tiên defensive sectors (Utilities, Healthcare)
- Trong bucket rủi ro thấp: Ưu tiên cyclical sectors (Finance, Industrials)

### 4. **Timing thị trường**
- Theo dõi transition matrix để dự báo chuyển đổi regime
- Kết hợp với phân tích kỹ thuật để xác định điểm vào/lệnh

## ⚠️ Lưu ý quan trọng

### Giới hạn
- Dữ liệu lịch sử hạn chế cho thị trường Việt Nam
- Mô hình dựa trên tương quan lịch sử, không đảm bảo tương lai
- Độ trễ trong dữ liệu vĩ mô

### Best Practices
1. **Kết hợp với phân tích khác**: Sử dụng cùng với phân tích cơ bản, kỹ thuật
2. **Backtest chiến lược**: Kiểm tra hiệu quả với dữ liệu lịch sử
3. **Quản lý rủi ro**: Luôn có stop-loss, không đầu tư toàn bộ vốn
4. **Cập nhật thường xuyên**: Theo dõi thay đổi tham số phù hợp với thị trường

## 🔬 Tính năng học thuật (Academic Features)

### 1. **Robust z-score với winsorization**
- Loại bỏ ảnh hưởng của outliers
- Sử dụng clip_multiplier để kiểm soát độ nhạy

### 2. **Non-overlapping samples**
- Tránh hiện tượng look-ahead bias
- Phù hợp cho nghiên cứu backtest nghiêm ngặt

### 3. **Log returns & return clipping**
- Xử lý return distribution phù hợp hơn
- Giảm ảnh hưởng của các phiên biến động mạnh

## 📚 Tài liệu tham khảo

### Lý thuyết nền tảng
1. **Macro-finance linkage**: Mối quan hệ giữa biến số vĩ mô và thị trường chứng khoán
2. **Regime-based investing**: Đầu tư theo regime thay vì market timing
3. **Sector rotation**: Luân chuyển ngành theo chu kỳ kinh tế

### Ứng dụng tại Việt Nam
- Đặc thù thị trường VN: Độ nhạy cao với lãi suất và thanh khoản
- Cấu trúc ngành: Tập trung vào Banking, Real Estate
- Chu kỳ kinh tế: Gắn với chu kỳ tín dụng và bất động sản

## 🆘 Hỗ trợ và đóng góp

### Xử lý sự cố
1. **Không hiển thị dữ liệu**: Kiểm tra quyền truy cập dữ liệu (TradingView Premium)
2. **Kết quả bất thường**: Reset statistics và kiểm tra lại tham số
3. **Hiệu suất chậm**: Tắt các tính năng không cần thiết (R60, DD60)

### Đóng góp phát triển
- Báo cáo lỗi và đề xuất tính năng
- Chia sẻ backtest results và improvement ideas
- Cộng tác nghiên cứu các mô hình mới

---

**Phiên bản**: 1.0  
**Tác giả**: Macro Research Team  
**Ngày cập nhật**: [Current Date]  
**Tương thích**: TradingView Pine Script v5  
**Thị trường**: HOSE - Việt Nam  

*Lưu ý: Công cụ này chỉ phục vụ mục đích nghiên cứu, không phải là lời khuyên đầu tư. Nhà đầu tư cần tự chịu trách nhiệm với quyết định của mình.*
