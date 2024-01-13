month = input()
nights = int(input())

price_app = 0
price_studio = 0

if month == "May" or month == "October":
    price_app = nights * 65
    price_studio = nights * 50
    if 7 < nights <= 14:
        price_studio = price_studio * 0.95
    elif nights > 14:
        price_studio = price_studio * 0.7
elif month == "June" or month == "September":
    price_app = nights * 68.70
    price_studio = nights * 75.20
    if nights > 14:
        price_studio = price_studio * 0.8
elif month == "July" or month == "August":
    price_app = nights * 77
    price_studio = nights * 76

if nights > 14:
    price_app = price_app * 0.9
print(f"Apartment: {price_app:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
