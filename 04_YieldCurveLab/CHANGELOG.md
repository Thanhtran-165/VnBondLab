# Changelog

## NEW 2.1 — 2026-09-24

### Added (so với NEW 2.0)
- Độ cong 5Y **có dấu**: `100 × [y5 − (0,625×y2 + 0,375×y10)]` bp, kèm Δ20P.
- Độ dốc từng đoạn 2–5Y và 5–10Y theo kỳ hạn danh nghĩa (bp/năm).
- Độ lệch chuẩn dân số của sáu Δ20P (độ phân tán biến động).
- Nhãn động học level/slope có hướng chỉ khi cả hai trị tuyệt đối ≥ biên 20P.
- Đối chứng trung vị đợt của nhãn hiện tại so với nhãn khác, cùng quy tắc chọn đợt.
- TEST fixture nội bộ 53 → 58.

### Preserved
- Lõi sáu kỳ hạn TPCP, cổng QA, rank, độ dốc, trạng thái S1–S6, nghiên cứu đợt 5/10/20P giữ từ NEW 2.0.
- Không chuỗi tiền tệ (đã bỏ từ NEW 2.0), không VNINDEX, không xác suất/dự báo.

### Packaging / vận hành
- Bản vận hành: `src/VN_YieldCurveLab_NEW_2_1.pine`, build `NEW2-20260924-02`, SHA-256 `0c64624faa624699d5ce6d8f4af1e1a1712e777e25265e55c45aa10e4b8b8bfe`.
- Gói bàn giao 24/09 lưu nguyên trạng tại `docs/new_2_1/` (gồm 2 ảnh bằng chứng nghiệm thu).
- `docs/new_2_1/UNVERIFIED/VN_YieldCurveLab_NEW_2_1_1_DRAFT.pine` (build `20260924-03`) chỉ sửa chữ dòng `CONFIRMED S`; **chưa biên dịch/nghiệm thu** — không dùng vận hành.
- ⚠️ Bản nháp 03 từng dán vào Pine Editor không rõ kết quả → trước lần chạy tay tiếp theo phải kiểm build hiển thị trên layout (02 hay 03).

## v3.4.0 — 2026-09-05

### Added
- Evidence package cho Bond Engine: component ranks, Pressure decomposition và 1W/1M/3M windows.
- Per-tenor evidence: Yield + 1D + 1W + 1M + 3M cho 1Y/2Y/3Y/5Y/7Y/10Y.
- Liquidity semantics tách IB trend khỏi relative-gap state.
- Gap Driver (`ΔGap = ΔIB - ΔPolicy`) cho 5/20 liquidity events.
- Liquidity event windows và range.
- Full Transmission direction matrix với trạng thái đồng thuận/phân kỳ/Bond-leading.
- Alignment quality và Last Valid Transmission.
- Early Observation, Active Contract và Research Trigger.
- AI benchmark và runtime evidence package.

### Preserved
- Dual Engine + Late Fusion architecture.
- IB lag contract 0–5 ngày.
- No VNINDEX.
- No forecast probability.
- No combined score.
- No causal attribution.

### Known limitations / runtime findings
- Pressure decomposition trên UI có thể có sai khác cộng trừ 0.1 do rounding khi hiển thị một chữ số; backend dùng precision đầy đủ.
- Trạng thái dưới ngưỡng Transmission có thể đi cùng một Gap Driver có hướng rõ; report cần phân biệt raw move với threshold classification.
- Overview đã gần giới hạn chiều cao; ưu tiên thay thế/đóng gói evidence thay vì tiếp tục thêm hàng vô hạn.
- Cần thêm runtime evidence cho Liquidity fresh, policy-only update, divergence và broad Bond shock.
