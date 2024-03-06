count_groups = int(input())

# #•	Група до 5 човека – изкачват Мусала
# •	Група от 6 до 12 човека – изкачват Монблан
# •	Група от 13 до 25 човека – изкачват Килиманджаро
# •	Група от 26 до 40 човека –  изкачват К2
# •	Група от 41 или повече човека – изкачват Еверест
musala_count = 0
montblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0
all_people = 0

for i in range(1, count_groups + 1):
    count_people = int(input())
    all_people = all_people + count_people
    if count_people <= 5:
        musala_count += count_people
    elif count_people <= 12:
        montblan_count += count_people
    elif count_people <= 25:
        kilimanjaro_count += count_people
    elif count_people <= 40:
        k2_count += count_people
    elif count_people >= 41:
        everest_count += count_people

musala_percent = musala_count / all_people * 100
montblan_percent = montblan_count / all_people * 100
kilimanjaro_percent = kilimanjaro_count / all_people * 100
k2_percent = k2_count / all_people * 100
everest_percent = everest_count / all_people * 100

print(f"{musala_percent:.2f}%")
print(f"{montblan_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")


