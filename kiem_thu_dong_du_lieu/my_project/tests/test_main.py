import pytest
from src.main import calculate_ticket_price

@pytest.mark.parametrize(
    "x, age, vip, expected",
    [
        # 1. x=300, age=20, vip=0 => "Invalid"
        (300, 20, 0, "Invalid"),
        
        # 2. x=100, age=20, vip=2 => 100
        (100, 20, 2, 100),
        
        # 3. x=100, age=5, vip=0 => 50
        (100, 5, 0, 50),
        
        # 4. x=100, age=10, vip=0 => 70
        (100, 10, 0, 70),
        
        # 5. x=100, age=25, vip=0 => 100
        (100, 25, 0, 100),
        
        # 6. x=100, age=5, vip=1 => 80
        (100, 5, 1, 80),
        
        # 7. x=100, age=5, vip=2 => 50
        (100, 5, 2, 50),
        
        # 8. x=120, age=5, vip=0 => 60
        (120, 5, 0, 60),
    ]
)
def test_calculate_ticket_price(x, age, vip, expected):
    result = calculate_ticket_price(x, age, vip)
    assert result == expected
