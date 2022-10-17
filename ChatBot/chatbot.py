#Taking user name and printing it
print("Hello! My name is Katafalk_Bot")
print("I was created in 2022")
print("Please, remind me your name")
user_name = input()
print("What a great name you have,", user_name)

#Guessing user age
print("Let me guess your age")
print("Enter remainders of dividing your age by 3, 5 and 7")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is", age, "that's a good time to start programming!")

#Counting from 1 to user number
print("Now I will prove to you that I can count to any number you want")
number = int(input())
for i in range(1,number+1):
    print(i,"!")
print("Completed, have a nice day!")

#Little Quiz
print("Let's test your programming knowledge")
print("Why do we use methods?")
print("""
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.
""")
while True:
    n = int(input())
    if n == 2:
        print("Completed, have a nice day!")
        break
    else:
        print("Please, try again")

#Ending
print("Congratulations, have a nice day!")
