# QA Status — VN YieldCurveLab v3.4.0

Build: `20260905-V340-EVIDENCE-SEMANTIC`

## Baseline

- Baseline phát triển: V3.3.1 CALM-WARNING UI.
- Baseline SHA256: `EF87745BB46211E7509870E6DA5DB651705F091A120F9DFE88DD4CC5C9EE075E`.

## Local verification đã có

- 38/38 contract/static/reference checks PASS tại thời điểm build V3.4.
- Source Acquisition + Committed Storage sections (03–04) byte-identical với baseline V3.3.1 tại thời điểm build.
- `request.security()`: 8.
- Không VNINDEX.
- Không `combinedScore` / COMBINED SCORE.
- Delimiter/static lexical checks PASS.
- Không TODO/TBD placeholders.
- Pine self-test declarations: 14 assertions; cần TradingView runtime để chạy thực tế.

## Semantic cases đã kiểm tra bằng reference tests

- Gap thu hẹp do IB giảm.
- Gap thu hẹp do policy tăng.
- Gap mở rộng do IB tăng.
- Gap mở rộng do policy giảm.
- Bond broad down/up/mixed/local taxonomy.
- Opposite-direction Transmission → `PHÂN KỲ NGƯỢC CHIỀU`.
- Gap stable + Bond broad down/up → Bond-leading states.
- Last Valid Transmission tách khỏi Current Transmission.

## Runtime evidence hiện có

User đã chạy V3.4 trên TradingView `TVC:VN10Y`, `1D` và cung cấp screenshot ngày 2026-09-05. Screenshot xác nhận dashboard V3.4 được render với Bond evidence, Liquidity evidence, Current Transmission, Last Valid Transmission, Research Trigger và Active Contract.

Đây là runtime evidence của một trạng thái cụ thể, không phải bằng chứng cho mọi nhánh logic.

## Chưa xác minh đầy đủ

- Bar Replay/reload behavior trên TradingView.
- Profiler/performance.
- Provider feed revision behavior.
- Runtime cases: Liquidity fresh, policy-only change, divergence hai chiều, broad Bond shock.

## Release stance

V3.4.0 được đóng gói như **runtime baseline tạm thời**. Chỉ nâng version tiếp khi runtime evidence cho thấy lỗi logic/semantic, thiếu evidence quan trọng hoặc giới hạn presentation làm AI đọc sai.
