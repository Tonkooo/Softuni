day_of_the_week = input()

if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Wednesday"\
        or day_of_the_week == "Thursday" or day_of_the_week == "Friday":
    print(f"Working day")
elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
    print(f"Weekend")
else:
    print('Error')
