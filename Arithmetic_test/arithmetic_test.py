counter = 0

import random

for i in range(5):
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    operator = random.choice(["+", "-", "*"])

    print(num1, operator, num2)
    answer = input(">")

    while not answer.isdigit():
        answer = input("Incorrect format.\n>")

    answer = int(answer)

    if operator == "+":
        if answer == num1 + num2:
            print("Right!")
            counter += 1
        else:
            print("Wrong!")

    elif operator == "-":
        if answer == num1 - num2:
            print("Right!")
            counter += 1
        else:
            print("Wrong!")

    elif operator == "*":
        if answer == num1 * num2:
            print("Right!")
            counter += 1
        else:
            print("Wrong!")

print("Your mark is", counter, "/5")
