hour_init = int(input())
minutes_init = int(input())

total_minutes = (hour_init * 60) + minutes_init + 15

hours = total_minutes // 60
minutes = total_minutes % 60
#121//60= 2 ---- 120 s ostatuk 1 koeto e za minutite
if hours > 23:
    hours = 0
if minutes <= 9:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")
