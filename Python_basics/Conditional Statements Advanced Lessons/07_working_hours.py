hour = int(input())
week_day = input()

if 10 <= hour <= 18 and week_day != "Sunday":
    print("open")
else:
    print("closed")

