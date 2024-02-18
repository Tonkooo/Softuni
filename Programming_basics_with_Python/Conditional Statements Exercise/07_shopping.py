budget = float(input())
videocard_count = int(input())
processor_count = int(input())
ram_count = int(input())

videocard_price = videocard_count * 250
processor_price = (videocard_price * 0.35) * processor_count
ram_price = (videocard_price * 0.1) * ram_count

price_all = videocard_price + processor_price + ram_price

if videocard_count > processor_count:
    price_all = price_all * 0.85
diff = abs(budget - price_all)
if budget >= price_all:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
