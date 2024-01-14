exam_hour = int(input())
exam_min = int(input())
hour_of_arrival = int(input())
min_of_arrival = int(input())

exam_time_min = (exam_hour * 60) + exam_min
arrival_time_min = (hour_of_arrival * 60) + min_of_arrival

diff_minutes = abs(exam_time_min - arrival_time_min)

if exam_time_min < arrival_time_min:
    print("Late")
    if diff_minutes >= 60:
        hour = diff_minutes // 60
        minutes = diff_minutes % 60
        if minutes < 10:
            print(f"{hour}:0{minutes} hours after the start")
        else:
            print(f"{hour}:{minutes} hours after the start")
    else:
        print(f"{diff_minutes} minutes after the start")
elif exam_time_min == arrival_time_min or diff_minutes <= 30:
    print("On time")
    if diff_minutes >= 1 and diff_minutes <= 30:
        print(f"{diff_minutes} minutes before the start")
else:
    print("Early")
    if diff_minutes >= 60:
        hour = diff_minutes // 60
        minutes = diff_minutes % 60
        if minutes < 10:
            print(f"{hour}:0{minutes} hours before the start")
        else:
            print(f"{hour}:{minutes} hours before the start")
    else:
        print(f"{diff_minutes} minutes before the start")
