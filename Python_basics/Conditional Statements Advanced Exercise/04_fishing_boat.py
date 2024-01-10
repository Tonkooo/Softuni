budget = int(input())
season = input()
count_people = int(input())

price_per_season = 0
if season == "Spring":
    price_per_season = 3000
elif season == "Summer" or season == "Autumn":
    price_per_season = 4200
elif season == "Winter":
    price_per_season = 2600

if count_people <= 6:
    price_per_season = price_per_season * 0.9
elif count_people <= 11:
    price_per_season = price_per_season * 0.85
elif count_people > 11:
    price_per_season = price_per_season * 0.75

if count_people % 2 == 0:
    if season != "Autumn":
        price_per_season = price_per_season * 0.95

diff = abs(budget-price_per_season)
if budget >= price_per_season:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
