# VnBondLab — Bộ công cụ nghiên cứu vĩ mô & trái phiếu Việt Nam

## 🎯 Giới thiệu

**VnBondLab** là bộ 5 chỉ báo TradingView (Pine Script v6) dành cho **nghiên cứu vĩ mô, đường cong lợi suất và truyền dẫn trái phiếu Việt Nam**. Mỗi dự án giải một bài toán riêng, nhưng liên kết với nhau qua Risk Score.

> ⚠️ **Định vị:** Đây là công cụ **nghiên cứu định lượng** (validated predictive monitors), không phải hệ thống giao dịch tự động, không phải mô hình nhân quả, không thay thế pipeline econometric chuyên dụng.

---

## 📦 Phiên bản hiện tại

| # | Dự án | Version | Trọng tâm | Code |
|---|---|---|---|---:|
| **01** | MacroAcademic Engine | **v3.2.1** | Semantic Clarity Patch — 4 trụ cột vĩ mô → Risk Score B0–B4 | 944 dòng |
| **02** | Macro Alert System | **v7.0.0** | Academic Robustness — vá 9 điểm yếu audit (Welch df, empirical percentile, freshness) | 1.509 dòng |
| **03** | Indices Research Map | **v3.1.3e** | Bounded Global Buffer Fix — map Risk Score → indices/sectors với Wilson CI, OOS | 2.434 dòng |
| **04** | YieldCurveLab | **v2.3.0** | Horizon Separation — Tactical 1W + Strategic 4W, episode-aware sampling, Dev/Val | 1.180 dòng |
| **05** | Bond Transmission Monitor | **v8.2.2** | Research Precision + Dual Chain — 6 kênh truyền dẫn, **FINAL BASELINE LOCKED** 16/07/2026 | 1.206 dòng |

**Tổng:** 7.273 dòng Pine Script v6.

---

## 🗺️ Kiến trúc hệ thống

```
┌─────────────────────────────────────────────┐
│  01_MacroAcademic Engine (Script A)         │
│  4 trụ cột vĩ mô → Risk Score B0–B4         │
└──────────────┬──────────────────────────────┘
               │ Risk Score (output dùng chung)
       ├───────┴────────┐
       ▼                ▼
  02_Macro Alert   03_Indices Map (Script B)
  (7.0.0 robust)   (3.1.3e Wilson CI / OOS)

  04_YieldCurveLab (2.3.0)     05_Bond Transmission (8.2.2)
  Độc lập — YC regime          Độc lập — 6 kênh quốc tế → VN
```

---

## 🔬 Năm bản nâng cấp chính trong đợt này

### 01 MacroAcademic Engine → v3.2.1
- Semantic Clarity Patch: làm rõ ngữ nghĩa nhãn và diễn giải.
- Vẫn giữ 4 trụ cột: Lạm phát, Lãi suất/Thanh khoản, Tăng trưởng, Chi phí/Ngoại lực.

### 02 Macro Alert System → v7.0.0 (Academic Robustness)
Bản vá **9 điểm yếu** audit phát hiện ở v6.0.1:

| Điểm yếu | Fix v7.0.0 |
|---|---|
| Bucket nén (avg percentile mất đều) | Empirical percentile calibration + equal-weight spec |
| `gaps_off` carry-forward | Freshness-aware quality (timestamp tolerance 5/14 ngày) |
| Grade dùng DQ hiện tại cho mẫu cũ | Entry-time sample quality |
| Welch không chỉnh df | Welch-Satterthwaite df + Cornish-Fisher critical value |
| "Ý nghĩa thống kê nhưng vô nghĩa kinh tế" | Economic materiality floor + Hedges' g ≥ 0.20 |
| Pre/post chỉ cùng dấu | Structural break diagnostic: STABLE/SHIFT/MIXED |
| 1 pha non-overlap nhạy start date | Staggered 5 cohort + alt-phase agreement |
| "Confidence" dễ nhầm xác suất | Đổi tên → Model reliability |
| Drawdown có thể dương | Drawdown correction: `min(..., 0)` |

### 03 Indices Research Map → v3.1.3e (Bounded Global Buffer Fix)
- **MAE / MFE / Close-MDD** path risk đầy đủ.
- **Wilson interval** cho win rate + transition probability.
- **OOS calibration/validation** + negative control (forward-minus-backward).
- **Outcome-quality gate**: CLEAN / CAUTION / CONTAMINATED / UNUSABLE.
- **Internal consistency invariant**: khoá inference là `INTERNAL-FAIL` nếu mismatch.
- **Bonferroni family-wise correction** cho 11 ngành.
- Fix lỗi compile **RE10067 / RE10143 / CE10013** (bounded global buffer `max_bars_back=120`).

### 04 YieldCurveLab → v2.3.0 (Horizon Separation & Sample Power)
- Tách **Macro State** khỏi **Predictive Evidence**.
- **Tactical 1W** + **Strategic 4W** với outcome không chồng lấn.
- **Episode-aware sampling** (regime-entry + cooldown) chống pseudo-replication.
- **Development/Validation** + hard gate (Welch t ≥ 1.96, CI 95%).
- **Adaptive Sample Power**: STANDARD (52w) hoặc HIGH (104w).
- `NO SIGNAL` / `INCONCLUSIVE` / `EPISODE N LOW` là **output hợp lệ**, không phải lỗi.

### 05 Bond Transmission Monitor → v8.2.2 (FINAL BASELINE LOCKED)
- **Patch v8.2.1** vá 2 bug: format mask (`#.1`/`#.3`) + P6 ghi đè direct gate.
- **Dual Chain Diagnostics**: Link Gate + Direct Gate + Overall (3 lớp độc lập).
- Nested walk-forward (120/60/40), Directional Edge, Median/MAD robust scaling.
- SHA-256 verified: `e6db0e36b7870225a9bddfff94303aa4dce19e564a9b17fed88b8cf4f46a56e3`.
- Snapshot 16/07/2026: **VALID 0/5, State NO SIGNAL** — "không có predictive edge là kết quả hợp lệ".

---

## 🔄 Workflow sử dụng kết hợp

### Workflow 1 — Tổng quan vĩ mô + cảnh báo
1. **01 MacroAcademic Engine** → Risk Score B0–B4
2. **02 Macro Alert System** → 3 panel (Macro / Risk / Equity) với Evidence Grade

### Workflow 2 — Mapping vĩ mô → thị trường
1. **01 MacroAcademic Engine** (Script A) → Risk Score
2. **03 Indices Research Map** (Script B) → AvgR / Win% / DD theo bucket × indices/sectors

### Workflow 3 — Nghiên cứu trái phiếu
1. **04 YieldCurveLab** → YC regime + Tactical/Strategic Bias
2. **05 Bond Transmission Monitor** → 6 kênh truyền dẫn quốc tế → VN10Y

---

## 🚀 Bắt đầu nhanh

### Theo vai trò

| Vai trò | Bắt đầu với | Mục đích chính |
|---|---|---|
| Nhà đầu tư chứng khoán | **02 Macro Alert System** | Panel Macro Weather + Sector Rotation |
| Quản lý danh mục | **01 MacroAcademic Engine** | Risk Score → asset allocation |
| Bond trader | **05 Bond Transmission Monitor** + **04 YieldCurveLab** | Timing TPCP + YC regime |
| Researcher | Cả 5 dự án | Macro-finance linkage, regime-based, sector rotation |

### Cài đặt (mỗi indicator)

1. Mở TradingView → **Pine Editor**.
2. Xóa code mặc định, dán toàn bộ file `.pine` của dự án.
3. **Save** → **Add to chart**.
4. Chuyển chart sang khung **1D** (bắt buộc cho mọi script).
5. (Tuỳ chọn) Mở **Settings** để chọn panel / chế độ (Executive / Research).

> Cần gói TradingView có quyền truy cập dữ liệu Economics (`ECONOMICS:*`) và HOSE indices.

---

## ⚠️ Giới hạn tính toán của TradingView Pine Script

Đây là phần quan trọng mà người dùng mô hình phức tạp cần biết. Pine Script là ngôn ngữ chạy trong sandbox của TradingView, **không phải môi trường econometric**. Các giới hạn sau ảnh hưởng trực tiếp đến độ tin cậy của mô hình:

### 1. Giới hạn thực thi (runtime budget)

| Giới hạn | Tác động |
|---|---|
| **Thời gian thực thi mỗi bar** (~40ms软弱) | Script nặng (regression, matrix) có thể timeout, đặc biệt khi warm-up dài. 02 và 05 phải tối ưu: chỉ chạy regression từ kỳ kiểm định trở đi. |
| **`max_bars_back`** | Bounded buffer. 03 từng bị **RE10067/RE10143/CE10013** vì dùng 5000/series → fix bằng `max_bars_back=120`. |
| **`calc_bars_count`** | Giới hạn số bar tính toán. 05 dùng `calc_bars_count=800`. |
| **Số `request.security()` call** | Mỗi script giới hạn ~40 call. 05 dùng 17, 01–04 dùng 6–10. |

### 2. Không có thư viện thống kê chuyên dụng

Pine **không có sẵn**:

- **HAC / Newey–West standard errors** (cho serial correlation).
- **Bootstrap** (block bootstrap, moving block).
- **Walk-forward rolling calibration** đầy đủ (chỉ approximated).
- **Structural break test** chính thức (Bai-Perron, Chow).
- **PCA / dynamic factor model**.
- **GARCH / volatility modeling**.
- **Vector autoregression (VAR)**.

Mô hình phải **tự implement** (vd: 02 tự viết Welch-Satterthwaite, 04 tự viết episode sampling) → xấp xỉ, không phải implementation chuẩn.

### 3. Khoảng tin cậy (confidence interval) là xấp xỉ

- CI dùng **t-approximation** hoặc **normal approximation**, không phải HAC-adjusted.
- Wilson interval (03, 04) tốt hơn normal cho tỷ lệ nhưng vẫn approximate cho dependent samples.
- **Không có p-value hiệu chỉnh** cho multiple testing ngoài Bonferroni (thủ công).
- **Không có clustered standard errors** cho panel/stratified data.

### 4. Non-overlap giảm nhưng không loại bỏ serial dependence

- Non-overlapping windows giảm phụ thuộc cơ học giữa các quan sát.
- Nhưng **regime persistence** và **clustering** vẫn còn → effective sample size nhỏ hơn N weekly.
- Cần đọc `EffN` (effective sample size) thay vì N raw để tránh ảo giác thống kê.

### 5. Dữ liệu TradingView có đặc thù

| Vấn đề | Hệ quả |
|---|---|
| **Lịch sử hạn chế** cho VN yields, interbank | Sample ngắn → warm-up dài, episode N thấp |
| **Độ trễ cập nhật** giữa các chuỗi | Mixed vintage → 01/04 có gate kiểm tra |
| **`barmerge.gaps_off`** carry-forward | Giá trị cũ có vẻ "mới" → 02 v7.0.0 thêm freshness-aware quality |
| **Quyền truy cập theo gói** | `ECONOMICS:*` cần Premium/Enterprise |
| **Revision policy** không minh bạch | Data có thể sửa hồi tố mà không báo |

### 6. Endogeneity & causal identification

- **Không có** instrumental variable (IV), difference-in-differences, hay synthetic control.
- Kết quả chỉ là **conditional historical association**, không phải nhân quả.
- Reverse causality (VN tác động ngược lại global) không được xử lý.

### 7. Warm-up dài

- Rolling percentile cần history, rồi latent percentile cần thêm cửa sổ hiệu chỉnh.
- **Regime warm-up**: có thể mất 504–1260 ngày trước khi model readiness = 100.
- Trong warm-up, script trả `WARMUP` / `DATA INSUFFICIENT` — không phải lỗi.

### 8. Limitations tổng kết

| Mô hình | Không có trong Pine | Cách script xử lý |
|---|---|---|
| **01 Risk Score** | — | Percentile + hysteresis (đơn giản, phù hợp) |
| **02 Evidence** | HAC SE, bootstrap | Welch-Satterthwaite + materiality floor |
| **03 Sector** | Clustered SE | Bonferroni + shrinkage |
| **04 Horizon** | Block bootstrap | Episode-aware + Dev/Val split |
| **05 Transmission** | VAR, IV | OLS per channel + nested walk-forward |

> **Nguyên tắc:** Pine mô hình hoá được khối lượng đáng kinh ngạc cho một sandbox, nhưng **không thay thế R/Python pipeline** khi cần publication-grade inference. Muốn nâng từ "academic-style indicator" thành "research system audit được", cần tách tầng production (Pine) khỏi tầng validation (Python/R bootstrap + HAC).

---

## 📊 So sánh nhanh 5 dự án

| Tiêu chí | 01 Engine | 02 Alert | 03 Indices | 04 YieldCurve | 05 Transmission |
|---|---|---|---|---|---|
| **Phạm vi** | Vĩ mô tổng hợp | Cảnh báo vĩ mô | Map vĩ mô → CK | Đường cong lợi suất | Truyền dẫn quốc tế |
| **Input** | CPI, GDP, Rates, FX, Oil | Rates, spreads, indices | Risk Score + indices + sectors | 1Y–10Y yields + VNINDEX | Global bonds + FX + VN10Y |
| **Output** | Risk Score B0–B4 | Evidence Grade + Tactical Bias | AvgR, Win%, DD, MAE/MFE | Curve Stress + Tac/Strat Bias | Impact Score + OOS R² |
| **Panel** | Multi-dashboard | 3 (Macro/Risk/Equity) | 4 (Macro/Market/Sector/Transition) | 4 (Macro/Tac/Strat/Diagnostics) | 6 (P1–P6) + Executive/Research |
| **Validation** | Percentile + hysteresis | Welch + Dev/Val + staggered | OOS + negative control + Wilson | Episode-aware + hard gate | Nested walk-forward + dual gate |
| **Timeframe** | 1D | 1D | 1D | 1D | 1D |

---

## 📝 Version History

### Sub-projects (phiên bản hiện tại):
- **01_MacroAcademic_Engine:** v3.2.1 (Semantic Clarity Patch)
- **02_Macro_Alert_System:** v7.0.0 (Academic Robustness)
- **03_Indices_Research_Map:** v3.1.3e (Bounded Global Buffer Fix)
- **04_YieldCurveLab:** v2.3.0 (Horizon Separation & Sample Power)
- **05_Bond_Transmission_Monitor:** v8.2.2 (Research Precision & Dual Chain Diagnostics — **FINAL BASELINE LOCKED** 16/07/2026)

---

## 📚 Tài liệu chi tiết

- 📖 [01_MacroAcademic_Engine README](./01_MacroAcademic_Engine/)
- 📖 [02_Macro_Alert_System README](./02_Macro_Alert_System/) — Review Methodology (9 điểm vá)
- 📖 [03_Indices_Research_Map README](./03_Indices_Research_Map/) — 13 mục đầy đủ
- 📖 [04_YieldCurveLab README](./04_YieldCurveLab/) — 19 mục chính thức
- 📖 [05_Bond_Transmission_Monitor README](./05_Bond_Transmission_Monitor/) — FINAL v8.2.2 (16 mục)
- 📄 [05 METHOD_v8.2.2.md](./05_Bond_Transmission_Monitor/METHOD_v8.2.2.md)
- 📄 [05 QA_v8.2.2.json](./05_Bond_Transmission_Monitor/QA_v8.2.2.json)
- 📄 [05 RELEASE_MANIFEST_v7.0.0.txt](./02_Macro_Alert_System/RELEASE_MANIFEST_v7.0.0.txt) (02)

---

## 👥 Tác giả & Liên hệ

**Tác giả:** Macro Research Team & VnBondLab  
**Nền tảng:** TradingView Pine Script v6  
**Thị trường:** HOSE — Việt Nam  
**Cập nhật:** 16/07/2026

---

## 📜 Disclaimer

Công cụ này chỉ phục vụ mục đích **nghiên cứu và giáo dục**. Đây không phải lời khuyên đầu tư, không phải mô hình nhân quả, không thay thế pipeline econometric chuyên dụng. Kết quả lịch sử không đảm bảo kết quả tương lai. Người sử dụng chịu trách nhiệm với mọi quyết định đầu tư.

> **Nguyên tắc cốt lõi:** Dữ liệu tốt không thay thế predictive edge. Áp lực quan sát không đồng nghĩa truyền dẫn đã xác nhận. Không có tín hiệu là một kết quả hợp lệ.
