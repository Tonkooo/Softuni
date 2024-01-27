n1 = int(input())
n2 = int(input())
operator = input()
sumа = 0
if operator == "+":
    sumа = (n1 + n2)
    if sumа % 2 == 0:
        answer = "even"
    else:
        answer = "odd"
    print(f'{n1} + {n2} = {sumа} - {answer}')
elif operator == "-":
    sumа = (n1 - n2)
    if sumа % 2 == 0:
        answer = "even"
    else:
        answer = "odd"
    print(f'{n1} - {n2} = {sumа} - {answer}')
elif operator == "*":
    sumа = (n1 * n2)
    if sumа % 2 == 0:
        answer = "even"
    else:
        answer = "odd"
    print(f'{n1} * {n2} = {sumа} - {answer}')
elif operator == "/":
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    elif n2 != 0:
        sumа = (n1 / n2)
        print(f'{n1} / {n2} = {sumа:.2f}')
elif operator == "%":
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    elif n2 != 0:
        sumа = (n1 % n2)
        print(f'{n1} % {n2} = {sumа}')
