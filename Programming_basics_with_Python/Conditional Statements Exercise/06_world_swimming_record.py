import math

record_seconds = float(input())
distance_meters = float(input())
time_for_one_metter_seconds = float(input())

total_time = distance_meters * time_for_one_metter_seconds

resistance_time = math.floor(distance_meters / 15) * 12.5
total_time = total_time + resistance_time


if total_time  < record_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    diff = total_time - record_seconds
    print(f'No, he failed! He was {diff:.2f} seconds slower.')