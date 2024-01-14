days = int(input())
room = (input())
rating = (input())

nights = days - 1
price_per_night = 0

if nights < 10:
    if room == "room for one person":
        price_per_night = 18
    elif room == "apartment":
        price_per_night = 25 * 0.7
    elif room == "president apartment":
        price_per_night = 35 * 0.9
elif 10 <= nights <= 15:
    if room == "room for one person":
        price_per_night = 18
    elif room == "apartment":
        price_per_night = 25 * 0.65
    elif room == "president apartment":
        price_per_night = 35 * 0.85
elif nights > 15:
    if room == "room for one person":
        price_per_night = 18
    elif room == "apartment":
        price_per_night = 25 * 0.5
    elif room == "president apartment":
        price_per_night = 35 * 0.8

final_price = price_per_night * nights
after_review_price = 0
if rating == "positive":
    after_review_price = final_price + (final_price * 0.25)
elif rating == "negative":
    after_review_price = final_price - (final_price * 0.1)

print(f"{after_review_price:.2f}")

