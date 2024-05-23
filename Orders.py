order = int(input())
total_price = 0
for n in range(order):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if price < 0.01 or price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules < 1 or capsules > 2000:
        continue
    price_per_day = days * capsules * price
    total_price += price_per_day
    print(f"The price for the coffee is: ${price_per_day:.2f}")
print(f"Total: ${total_price:.2f}")