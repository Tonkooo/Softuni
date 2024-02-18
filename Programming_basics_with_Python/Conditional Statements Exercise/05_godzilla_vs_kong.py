budget = float(input())
statists = int(input())
dress_per_statist = float(input())

all_dress = statists * dress_per_statist
decor = budget * 0.1

if statists > 150:
    all_dress = all_dress * 0.9

money = all_dress + decor
final_sum = abs(budget - money)

if money > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {final_sum:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {final_sum:.2f} leva left.")