# VN YieldCurveLab v3.4.0

**Evidence Expansion & Semantic Integrity**  
Build: `20260905-V340-EVIDENCE-SEMANTIC`

VN YieldCurveLab là chỉ báo Pine Script v6 dùng để mô tả môi trường lãi suất Việt Nam theo kiến trúc **Dual Engine + Late Fusion**. Phiên bản 3.4.0 ưu tiên khả năng kiểm định kết quả bởi AI: một screenshot Overview kết hợp với source Pine phải cung cấp đủ bằng chứng để AI đọc số liệu, tái tính các đại lượng quyết định, phân biệt current/history/stale và viết báo cáo mà không vượt quá bằng chứng.

## Kiến trúc

1. **Bond Engine** — chỉ sử dụng 1Y, 2Y, 3Y, 5Y, 7Y, 10Y.
2. **Liquidity Engine** — chỉ sử dụng lãi suất liên ngân hàng, policy reference và gap.
3. **Transmission Engine** — late fusion, read-only; chỉ đối chiếu khi hai engine đủ điều kiện thời gian/dữ liệu.
4. **Presentation / Evidence Surface** — hiển thị đủ evidence cho AI nhưng tách vùng rõ ràng.

Không có VNINDEX, không forecast probability, không combined score và không causal attribution.

## V3.4 bổ sung

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

## Data contract quan trọng

- IB lag `0–5` ngày lịch: accepted as-of.
- Carry-forward không tạo liquidity event mới.
- IB lag `>5` ngày: Liquidity hiện tại không đủ điều kiện cho Late Fusion.
- Bond và Liquidity giữ state độc lập.
- Current Transmission và Last Valid Transmission không được trộn lẫn.
- Source timestamp không phải publication timestamp và provider có thể revise lịch sử.

## Cách chạy

1. Mở `TVC:VN10Y` trên TradingView.
2. Chọn timeframe `1D` và chart chuẩn.
3. Mở Pine Editor.
4. Dán toàn bộ `src/VN_YieldCurveLab_v3_4_0.pine`.
5. Add to chart.

## Trạng thái phát triển

`v3.4.0` hiện là **runtime baseline tạm thời**. Ưu tiên hiện tại là thu thập runtime evidence qua nhiều trạng thái thị trường thay vì tiếp tục thêm feature.

Runtime evidence đầu tiên đã được lưu tại `docs/runtime/`.

## Kiểm tra local

Chạy từ root package/repo:

```bash
python tests/test_v34_contract.py src/VN_YieldCurveLab_v3_4_0.pine
python tests/test_v34_semantics.py
python tests/verify_release.py
```

Các kiểm tra local là static/reference checks; không thay thế TradingView Pine Compiler, Bar Replay hoặc Profiler.

## Tài liệu

- `CHANGELOG.md` — thay đổi của release.
- `docs/QA_STATUS.md` — phạm vi đã/chưa xác minh.
- `docs/AI_BENCHMARK.md` — benchmark đọc evidence cho AI.
- `docs/runtime/RUNTIME_EVIDENCE.md` — bằng chứng chạy thực tế.
- `docs/design/V3_4_IMPLEMENTATION_PLAN.md` — kế hoạch triển khai đã dùng.
- `AGENT_HANDOFF.md` — hướng dẫn cho agent đưa package lên repository.

## License

Package này **không tự gán license**. Repo owner cần chọn license riêng nếu muốn public/open-source.
