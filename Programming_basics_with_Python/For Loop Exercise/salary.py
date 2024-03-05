# tab = int(input())
# salary = int(input())
# copy_salary = salary
# for i in range(1, tab + 1):
#     tab_name = input()
#
#     if tab_name == "Facebook":
#         copy_salary = copy_salary - 150
#     elif tab_name == "Instagram":
#         copy_salary = copy_salary - 100
#     elif tab_name == "Reddit":
#         copy_salary = copy_salary - 50
#
#     if copy_salary <= 0:
#         break
# if copy_salary > 0:
#     print(copy_salary)
# else:
#     print("You have lost your salary.")


tab = int(input())
salary = int(input())

for i in range(1, tab + 1):
    tab_name = input()

    if tab_name == "Facebook":
        salary = salary - 150
    elif tab_name == "Instagram":
        salary = salary - 100
    elif tab_name == "Reddit":
        salary = salary - 50

    if salary <= 0:
        break
if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")
