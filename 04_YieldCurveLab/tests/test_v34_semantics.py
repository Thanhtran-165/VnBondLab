# Reference semantics for the V3.4 taxonomy; mirrors intended Pine branching.
LIQ=25.0

def bond_state(down,up):
    if down>=4 and up<=1: return 'BOND GIẢM RỘNG'
    if up>=4 and down<=1: return 'BOND TĂNG RỘNG'
    if down>=2 and up>=2: return 'BOND PHÂN HÓA'
    if down>=2: return 'BOND GIẢM CỤC BỘ'
    if up>=2: return 'BOND TĂNG CỤC BỘ'
    return 'BOND ÍT THAY ĐỔI'

def gap_driver(dib,dpol,dgap,eps=.5):
    ibd=dib<-eps; ibu=dib>eps; pd=dpol<-eps; pu=dpol>eps
    if abs(dgap)<=eps: return 'GAP ÍT ĐỔI'
    if dgap<0:
        if ibd and pu: return 'THU HẸP · IB GIẢM + POLICY TĂNG'
        if ibd and not pu: return 'THU HẸP · DO IB GIẢM'
        if pu and not ibd: return 'THU HẸP · DO POLICY TĂNG'
        return 'THU HẸP · MIXED'
    if ibu and pd: return 'MỞ RỘNG · IB TĂNG + POLICY GIẢM'
    if ibu and not pd: return 'MỞ RỘNG · DO IB TĂNG'
    if pd and not ibu: return 'MỞ RỘNG · DO POLICY GIẢM'
    return 'MỞ RỘNG · MIXED'

assert bond_state(5,0)=='BOND GIẢM RỘNG'
assert bond_state(0,5)=='BOND TĂNG RỘNG'
assert bond_state(2,2)=='BOND PHÂN HÓA'
assert bond_state(2,0)=='BOND GIẢM CỤC BỘ'
assert gap_driver(-20,0,-20)=='THU HẸP · DO IB GIẢM'
assert gap_driver(0,20,-20)=='THU HẸP · DO POLICY TĂNG'
assert gap_driver(20,0,20)=='MỞ RỘNG · DO IB TĂNG'
assert gap_driver(0,-20,20)=='MỞ RỘNG · DO POLICY GIẢM'
print('semantic_reference_tests=8 PASS')
