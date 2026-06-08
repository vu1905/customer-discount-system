from discount import calculate_discount

def test_vip_customer():
    # TC01: Tổng trước = 60 triệu, đơn hàng = 2 triệu
    assert calculate_discount(2_000_000, 60_000_000) == 0.1

def test_normal_customer():
    # TC02: Tổng trước = 30 triệu, đơn hàng = 2 triệu => tổng 32 triệu < 50 triệu
    assert calculate_discount(2_000_000, 30_000_000) == 0.0

def test_reaching_threshold():
    # TC03: Tổng trước = 49 triệu, đơn hàng = 2 triệu => tổng 51 triệu >= 50 triệu
    assert calculate_discount(2_000_000, 49_000_000) == 0.1
