command = input()

total_sum = 0


while command != "NoMoreMoney":
    current_sum = float(command) #създаваме си нова променлива която да може да работи с флоат и стринг
    if current_sum < 0:
        print(f"Invalid operation!")
        break
    else:
        print(f"Increase: {current_sum:.2f}")
    total_sum = total_sum + current_sum #пресмятането се случа в while цикъла, не в IF/ELSE
    command = input()
print(f"Total: {total_sum:.2f}")