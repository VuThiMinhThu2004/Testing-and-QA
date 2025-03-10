import pytest
from src.main import calculate_ticket_price

def test_calculate_ticket_price():
    # Test case 1: Giá vé không hợp lệ (x = 0, age = 200, vip = 1)
    assert calculate_ticket_price(0, 200, 1) == "Invalid"

    # Test case 2: Trẻ em dưới 6 tuổi, không chọn ghế VIP (x = 100, age = 5, vip = 0)
    assert calculate_ticket_price(100, 5, 0) == 50

    # Test case 3: Trẻ em dưới 6 tuổi, có chọn ghế VIP (x = 100, age = 5, vip = 1)
    assert calculate_ticket_price(100, 5, 1) == 80

    # Test case 4: Trẻ em dưới 6 tuổi, vip giá trị không hợp lệ (x = 100, age = 5, vip = 2)
    assert calculate_ticket_price(100, 5, 2) == 50  # Giả định hệ thống bỏ qua giá trị vip không hợp lệ

    # Test case 5: Trẻ em từ 6-18 tuổi, không chọn ghế VIP (x = 100, age = 10, vip = 0)
    assert calculate_ticket_price(100, 10, 0) == 70

    # Test case 6: Người lớn trên 18 tuổi, không chọn ghế VIP (x = 100, age = 20, vip = 0)
    assert calculate_ticket_price(100, 20, 0) == 100
