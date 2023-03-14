import random

num1 = random.randint(2,9)
num2 = random.randint(2,9)

operation = random.choice(["+", "-", "*"])

print(num1, operation, num2,"\n>")
user_answer = int(input())
answer = None

if operation == "+":
    answer = num1 + num2
    if answer == user_answer:
        print("Right!")
    else:
        print("Wrong!")

elif operation == "-":
    answer = num1 - num2
    if answer == user_answer:
        print("Right!")
    else:
        print("Wrong")

elif operation == "*":
    answer = num1 * num2
    if answer == user_answer:
        print("Right!")
    else:
        print("Wrong!")

