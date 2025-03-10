def calculate_ticket_price(x, age, vip):
    # Kiểm tra điều kiện đầu vào hợp lệ
    if not (100 <= x <= 200) or not (0 <= age <= 100):
        return "Invalid"
    price = x
    # Xác định giá vé dựa trên độ tuổi
    if age < 6:
        price -= 0.5 * x
    elif 6 <= age <= 18:
        price -= 0.3 * x
    else:
        price -= 0 * x

    # Nếu chọn ghế VIP, cộng thêm 30% giá vé cơ bản
    if vip == 0:
        price -= 0 
    elif vip == 1:
        price += 0.3 * x

    return price
