count_of_numbers = int(input())
result = 0

for numbers in range(count_of_numbers):
    current_number = int(input())
    result = result + current_number
print(result)