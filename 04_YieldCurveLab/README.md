# VN YieldCurveLab

Package này chứa **hai baseline** của chỉ báo Pine Script v6 mô tả đường cong lợi suất trái phiếu chính phủ Việt Nam:

| Baseline | Ngày | Vai trò | Phạm vi dữ liệu |
|---|---|---|---|
| **NEW 2.1** (build `NEW2-20260924-02`) | 24/09/2026 | **Bản vận hành hiện hành** | Chỉ 6 kỳ hạn TPCP (1/2/3/5/7/10Y) |
| **v3.4.0** (build `20260905-V340-EVIDENCE-SEMANTIC`) | 05/09/2026 | Baseline lưu trữ | Dual Engine: 6 kỳ hạn TPCP + lãi suất liên ngân hàng/policy |

---

## NEW 2.1 — bản vận hành hiện hành

- Mã: `src/VN_YieldCurveLab_NEW_2_1.pine`, 808 dòng, SHA-256 `0c64624faa624699d5ce6d8f4af1e1a1712e777e25265e55c45aa10e4b8b8bfe`.
- Chỉ sáu `request.security` đến `TVC:VN01Y/02Y/03Y/05Y/07Y/10Y`. Không có chuỗi tiền tệ, không VNINDEX, không xác suất/dự báo.
- Đã biên dịch và nghiệm thu trên TradingView ngày 24/09/2026 (nguồn chốt 23/09, QA PASS, TEST 58/58). Hai ảnh bằng chứng trong `docs/new_2_1/`.
- Layout tham chiếu: https://www.tradingview.com/chart/pNvdqrGl/ — TVC:VN10Y, 1D, chart chuẩn.

### So với NEW 2.0

Giữ lõi (cổng QA, rank, độ dốc, ba nhóm kỳ hạn, trạng thái S1–S6, nghiên cứu đợt 5/10/20P); bổ sung: độ cong 5Y **có dấu**, độ dốc từng đoạn 2–5Y/5–10Y theo kỳ hạn danh nghĩa, độ phân tán của sáu Δ20P, động học level/slope có hướng khi vượt biên, đối chứng trung vị nhãn lịch sử. Chi tiết: `docs/new_2_1/BENCHMARK_NEW_2_0_VS_NEW_2_1.md`.

### Cách chạy (thủ công, không automation)

1. Mở layout trên, xác nhận TVC:VN10Y, 1D, không Replay, đúng một chỉ báo.
2. Kiểm tra dòng tiêu đề ghi **BUILD 20260924-02** và đầu vào 5P=2bp, 20P=5bp, sàn nhảy=25bp.
3. Mỗi lần chạy kiểm tra cổng dữ liệu: QA PASS, tuổi nguồn ≤5 ngày, 6/6 cửa sổ kỳ hạn, đủ tham chiếu, TEST 58/58, không NA ở số được trích.
4. Chỉ viết bản tin khi có dòng `ĐỦ ĐIỀU KIỆN BẢN TIN TRÁI PHIẾU`. Khuôn bản tin: `docs/new_2_1/FORMAT_VAN_HANH_NEW_2_1.md`.

### ⚠️ Việc phải làm trước lần chạy tay tiếp theo

Bản nháp build `20260924-03` từng được dán vào Pine Editor nhưng trình biên tập ngừng phản hồi — **chưa biết layout hiện đang chạy build 02 hay 03**. Phải kiểm tra build hiển thị; nếu là 03 thì hoặc nghiệm thu nó (so ảnh với bản 02), hoặc dán lại `src/VN_YieldCurveLab_NEW_2_1.pine` để trở về build đã nghiệm thu.

### Gói bàn giao nguyên trạng

`docs/new_2_1/` là bản sao 1:1 của goi bàn giao 24/09/2026 (TRANSIT, benchmark, kiểm toán học thuật, khuôn vận hành, mẫu bản tin, 2 ảnh, và `UNVERIFIED/VN_YieldCurveLab_NEW_2_1_1_DRAFT.pine` — bản nháp build `20260924-03` **chưa biên dịch/nghiệm thu**, chỉ sửa chữ dòng `CONFIRMED S`, không dùng để vận hành).

---

## v3.4.0 — baseline lưu trữ

**Evidence Expansion & Semantic Integrity**
Build: `20260905-V340-EVIDENCE-SEMANTIC`

VN YieldCurveLab v3.4.0 mô tả môi trường lãi suất Việt Nam theo kiến trúc **Dual Engine + Late Fusion**. Ưu tiên khả năng kiểm định kết quả bởi AI: một screenshot Overview kết hợp source Pine cung cấp đủ bằng chứng để AI đọc số liệu, tái tính các đại lượng quyết định, phân biệt current/history/stale và viết báo cáo mà không vượt quá bằng chứng.

### Kiến trúc

1. **Bond Engine** — chỉ sử dụng 1Y, 2Y, 3Y, 5Y, 7Y, 10Y.
2. **Liquidity Engine** — chỉ sử dụng lãi suất liên ngân hàng, policy reference và gap.
3. **Transmission Engine** — late fusion, read-only; chỉ đối chiếu khi hai engine đủ điều kiện thời gian/dữ liệu.
4. **Presentation / Evidence Surface** — hiển thị đủ evidence cho AI nhưng tách vùng rõ ràng.

Không có VNINDEX, không forecast probability, không combined score và không causal attribution.

### V3.4 bổ sung

- Rank Level / Slope / Belly / Long để kiểm tra Pressure.
- Pressure decomposition: `VALUE + REF = TOTAL`.
- Sáu tenor với Yield + 1D + 1W + 1M + 3M.
- Bond window dates 1W / 1M / 3M.
- Liquidity market-rate state tách khỏi relative-gap state.
- Gap Driver: phân rã `ΔGap = ΔIB - ΔPolicy`.
- Liquidity 5-event / 20-event windows và range.
- Transmission taxonomy đầy đủ: đồng thuận, phân kỳ ngược chiều, Bond dẫn, mixed/partial.
- Alignment quality: `EXACT` hoặc `AS-OF ≤Nd`.
- Last Valid Transmission tách tuyệt đối khỏi Current Transmission.
- Early Observation không thay thế confirmed state.
- Active Contract để AI biết ngưỡng/runtime settings đang áp dụng.
- Research Trigger là gợi ý dữ liệu cần tìm thêm, không phải kết luận nguyên nhân.

### Data contract quan trọng

- IB lag `0–5` ngày lịch: accepted as-of.
- Carry-forward không tạo liquidity event mới.
- IB lag `>5` ngày: Liquidity hiện tại không đủ điều kiện cho Late Fusion.
- Bond và Liquidity giữ state độc lập.
- Current Transmission và Last Valid Transmission không được trộn lẫn.
- Source timestamp không phải publication timestamp và provider có thể revise lịch sử.

### Cách chạy v3.4.0

1. Mở `TVC:VN10Y` trên TradingView, timeframe `1D`, chart chuẩn.
2. Mở Pine Editor, dán toàn bộ `src/VN_YieldCurveLab_v3_4_0.pine`, Add to chart.

### Kiểm tra local

Chạy từ root package/repo:

```bash
python tests/test_v34_contract.py src/VN_YieldCurveLab_v3_4_0.pine
python tests/test_v34_semantics.py
python tests/verify_release.py
```

Các kiểm tra local là static/reference checks; không thay thế TradingView Pine Compiler, Bar Replay hoặc Profiler.

---

## Tài liệu

- `CHANGELOG.md` — thay đổi của từng release.
- `docs/new_2_1/TRANSIT_NEW_2_1_MAIN_SESSION.md` — tài liệu bàn giao NEW 2.1 cho session chính.
- `docs/new_2_1/BENCHMARK_NEW_2_0_VS_NEW_2_1.md` — đối chiếu NEW 2.0 → NEW 2.1.
- `docs/new_2_1/KIEM_TOAN_HOC_THUAT_NEW_2_1_2026-09-24.md` — kiểm toán học thuật + phép tính lại độc lập.
- `docs/new_2_1/FORMAT_VAN_HANH_NEW_2_1.md` — cách đọc ảnh và khuôn bản tin.
- `docs/QA_STATUS.md`, `docs/AI_BENCHMARK.md`, `docs/runtime/RUNTIME_EVIDENCE.md`, `docs/design/V3_4_IMPLEMENTATION_PLAN.md` — tài liệu v3.4.0.
- `AGENT_HANDOFF.md` — hướng dẫn (v3.4.0) cho agent đưa package lên repository.

## License

Package này **không tự gán license**. Repo owner cần chọn license riêng nếu muốn public/open-source.
