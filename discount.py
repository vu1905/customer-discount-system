def calculate_discount(order_value, total_year_value):
    """
    Hàm tính tỷ lệ giảm giá cho khách hàng thân thiết.
    - order_value: giá trị đơn hàng hiện tại
    - total_year_value: tổng giá trị mua hàng trước đó trong năm
    """
    # Tổng giá trị sau khi cộng đơn hàng hiện tại
    new_total = total_year_value + order_value

    # Nếu trước đó đã đủ 50 triệu hoặc đơn hàng này giúp đạt ngưỡng
    if total_year_value >= 50_000_000 or new_total >= 50_000_000:
        return 0.1  # giảm 10%
    return 0.0  # không giảm
