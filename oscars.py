actor_name = input()
init_point = float(input())
count_people = int(input())

total_points = init_point
for i in range(1, count_people+1):
    name = input()
    current_points = float(input())

    points = (len(name) * current_points) / 2  #с ЛЕН по този начин това ще върне дължината на името, или колко символа се съдържат в него
    total_points = total_points + points
    if total_points >= 1250.5:
        break

if total_points <= 1250.5:
    diff = abs(1250.5 - total_points)
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
