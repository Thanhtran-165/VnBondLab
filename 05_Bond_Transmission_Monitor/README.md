# Giám sát truyền dẫn trái phiếu Việt Nam (P1–P6) — MacroAcademic FULL

**VN Bond Transmission Monitor v5.2**

---

## 1) Mục tiêu của chỉ báo

Chỉ báo này dùng để giám sát cơ chế truyền dẫn (transmission monitoring) từ:

- Lợi suất toàn cầu / Nhật
- Trạng thái risk-off (carry unwind)
- Kênh USD & thanh khoản (USDVND, VNINBR/IB)

Sang lợi suất Việt Nam (VN10Y).

Chỉ báo **không** nhằm chứng minh nhân quả tuyệt đối; nó được thiết kế để:

- Phát hiện kênh nào đang "mở"/"đóng" theo thời gian
- Tách phần biến động VN10Y "đi theo kênh" vs "lệch kênh"
- Cung cấp bảng đọc nhanh **10 giây** cho người dùng phổ thông

---

## 2) Dữ liệu sử dụng (TradingView tickers)

**Mặc định** (có thể thay trong input nếu cần):

**VN yields:** `TVC:VN10Y`, `TVC:VN02Y`

**JP yields:** `TVC:JP10Y`, `TVC:JP02Y`

**Global yields:** `TVC:US10Y`, `TVC:US02Y`, `TVC:DE10Y`, `TVC:DE02Y`, `TVC:GB10Y`, `TVC:GB02Y`, `TVC:AU10Y`, `TVC:CA10Y`

**FX & risk:** `FX_IDC:USDVND`, `FX_IDC:USDJPY`, `CBOE:VIX`, `TVC:DXY`

**Interbank proxy:** `ECONOMICS:VNINBR`

**Lưu ý:** Một số ticker có thể bị thiếu dữ liệu theo vùng/tài khoản; khi đó "Tin cậy" sẽ giảm.

---

## 3) Khái niệm cốt lõi (đọc đúng để không hiểu sai)

### 3.1. "Điểm áp lực (0–100)"

Điểm tổng hợp để biểu diễn mức áp lực tăng lợi suất VN10Y theo panel đang chọn.

**Ngưỵ màu:**
- **B0 (<35)**: Thuận lợi
- **B1 (35–50)**: Bình thường
- **B2 (50–65)**: Cảnh giác
- **B3 (65–80)**: Căng thẳng
- **B4 (≥80)**: Sốc

### 3.2. "Dự tính" (Expected)

Phần biến động VN10Y được mô hình panel giải thích (expected component).

### 3.3. "Tách biệt" (Residual)

Phần biến động VN10Y không giải thích được bởi driver panel.

**Hiểu đơn giản:**
- **Tách biệt cao**: VN có yếu tố nội sinh/đặc thù mạnh, ít bị kéo theo bởi driver panel.
- **Tách biệt thấp**: VN đi "đúng kênh" theo driver panel.

### 3.4. "Truyền dẫn" & "Tin cậy"

**Truyền dẫn:** Dựa trên sức mạnh hồi quy (R²) của panel hoặc chain strength (P6).
Nhãn: Yếu / Vừa / Mạnh

**Tin cậy:** Kết hợp R² và độ phủ dữ liệu (coverage).
Nhãn: Thấp / Trung bình / Cao

**Quy tắc vận hành:**
> Chỉ kết luận cơ chế khi **Tin cậy ≥ Trung bình** (và lý tưởng là **Truyền dẫn ≥ Vừa**).

---

## 4) Cách dùng nhanh (workflow 30 giây)

### Bước 1 — Mở panel mặc định: **P6 Chuỗi truyền dẫn→VN**

Đọc theo thứ tự trong bảng:
1. Trạng thái (B0–B4) + "Hôm nay tốt/xấu hơn"
2. Tin cậy
3. Truyền dẫn
4. Bị kéo theo

**Kết luận nhanh:**
- Nếu Tin cậy thấp → tránh kết luận cơ chế, chuyển P5/P2.
- Nếu Tin cậy TB/Cao và Truyền dẫn Vừa/Mạnh → chuỗi đang hoạt động.

### Bước 2 — Xác nhận bằng **P5 FX & Thanh khoản→VN**

Nếu P5 mạnh nhưng P6 yếu:
- Kênh nội địa (USDVND/IB) đang quan trọng hơn "chuỗi quốc tế" trong ngày đó.

### Bước 3 — Đặt bối cảnh bằng **P2/P3**

- **P2**: Cú sốc rates toàn cầu "đè" VN.
- **P3**: Câu chuyện đường cong (level/slope) và risk premium theo chu kỳ.

### Bước 4 — Chỉ xem khi cần chẩn đoán nhánh

- **P1**: Nhật/BOJ → VN
- **P4**: Yên carry / risk-off → VN

---

## 5) Ý nghĩa các panel

### **P1 — BOJ → VN**
- **Driver:** JP02Y hoặc JP10Y (mặc định JP10Y)
- **Dùng khi:** Thị trường tập trung vào Nhật/BOJ, dòng vốn JPY

### **P2 — Toàn cầu → VN**
- **Driver:** Biến động composite 10Y toàn cầu (US/DE/GB/AU/CA)
- **Dùng để:** Đọc "global rates shock"

### **P3 — Đường cong → VN**
**Kết hợp:**
- Level: dG10 → dVN10
- Slope change: dsG → dsVN
- **Dùng để:** Đọc regime đường cong và risk premium

### **P4 — Yên carry → VN**
- **Composite:** JPY mạnh lên + VIX tăng + thu hẹp chênh US2Y–JP2Y
- **Dùng khi:** Có risk-off/carry unwind

### **P5 — FX & Thanh khoản → VN**
- **Composite:** USDVND (ROC) + VNINBR/IB (bp change)
- **Dùng để:** Đọc "nút nội địa trung gian"

### **P6 — Chuỗi truyền dẫn → VN (mặc định)**

**Chuỗi 3 bước:**
- **A:** (US2Y + DXY) → USDVND
- **B:** USDVND → VNINBR/IB
- **C:** VNINBR/IB → VN10Y

Có **chainStrength** và **chainShock** để đọc "chuỗi chạy" và "cường độ cú sốc".

---

## 6) Mặc định "phổ quát" (đề xuất cho người không chỉnh)

Các mặc định đã đặt theo hướng ổn định/đọc regime:

- **Data:** Daily
- **LEN_Z:** 252
- **LEN_REG:** 60
- **CLIP_Z:** 3.0
- **smoothN:** 3
- **lagDriver:** 1
- **Panel mặc định:** P6

---

## 7) Giới hạn & lưu ý

1. **Không phải mô hình nhân quả tuyệt đối:**
   Rolling OLS là công cụ monitoring cơ chế, không giải quyết triệt để endogeneity hai chiều.

2. **Ticker phụ thuộc TradingView:**
   Nếu thiếu data, "Tin cậy" sẽ giảm.

3. **VNINBR là proxy cho interbank:**
   Phù hợp monitoring, không thay thế dữ liệu liên ngân hàng chuẩn theo cấu phần (ON/1W/2W/1M…).

---

## 8) Troubleshooting (lỗi thường gặp)

| Vấn đề | Khắc phục |
|--------|-----------|
| Bảng/đường bị NA nhiều | Kiểm tra ticker (USDVND/VNINBR/DE02Y…) có dữ liệu không |
| Tín hiệu giật mạnh | Tăng smoothN (nếu cần) nhưng mặc định đã cân bằng |
| P4 "lạ" | Đảm bảo dòng impact_CRY dùng scoreDrvShock_CRY (đã fix trong bản v5.2) |

---

## 9) Gợi ý vận hành sau khi triển khai

Trong **2–6 tuần**, bạn chỉ cần lưu ảnh ở **3–5 ngày tiêu biểu**:

1 ngày stress FX/IB
1 ngày bình thường
1 ngày "nội sinh VN"
1 ngày risk-off toàn cầu

Để đánh giá: panel nào thực sự hữu ích và có cần nâng cấp "nhân quả hơn" hay chỉ tối ưu proxy/ticker.

---

## 📝 Phiên bản

**v5.2** (2025) - MacroAcademic FULL Edition với 6 panels (P1–P6)

---

**Tác giả:** MacroAcademic Team
**Platform:** TradingView Pine Script v5
**Thị trường:** HOSE - Việt Nam
**Last updated:** January 2025

*Disclaimer: Công cụ này chỉ phục vụ mục đích nghiên cứu, không phải là lời khuyên đầu tư.*
