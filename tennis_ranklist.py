import math

tournament_count = int(input())
start_points = int(input())
all_points = 0
win_tournament = 0
for i in range(1, tournament_count + 1):
    level = input()
    if level == "W":
        all_points = all_points + 2000
        win_tournament += 1
    elif level == "F":
        all_points = all_points + 1200
    elif level == "SF":
        all_points = all_points + 720


average_points = math.floor(all_points / tournament_count)
all_points = all_points + start_points
win_percent = win_tournament / tournament_count * 100

print(f"Final points: {all_points}")
print(f"Average points: {average_points}")
print(f"{win_percent:.2f}%")

