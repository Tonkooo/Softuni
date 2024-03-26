needed_money = float(input())
init_money = float(input())
days_counter = 0
count_spent = 0
total_money = init_money


while total_money < needed_money:
    if count_spent == 5:
        break
    days_counter += 1
    action = input()
    amount = float(input())

    if action == "spend":
        count_spent += 1
        total_money = total_money - amount
        if total_money < 0:
            total_money = 0
    elif action == "save":
        count_spent = 0
        total_money = total_money + amount

if count_spent == 5:
    print(f"You can't save the money.")
    print(f"{days_counter}")
else:
    print(f"You saved the money for {days_counter} days.")