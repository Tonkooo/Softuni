type_tickets = input()
rows = int(input())
cols = int(input())

all_seats = rows * cols

price = 0
if type_tickets == "Premiere":
    price = 12
elif type_tickets == "Normal":
    price = 7.5
elif type_tickets == "Discount":
    price = 5

suma = price * all_seats
print(f"{suma:.2f} leva")