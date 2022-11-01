import sys
import random
#Step 3

friends_dict = {}

y_or_n = {'Yes': True, 'No': False}

num = int(input("Enter the number of friends joining (including you): "))
if num < 1:
    print("No one is joining for the party")
    sys.exit()

print("Enter the name of every friend (including you),each on new line: ")
for i in range(num):
    friends_names = input()
    friends_dict[friends_names] = 0

#lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
lucky_one = y_or_n[input()]
lucky_name = ""

bill = int(input("Enter the total amount:"))

if lucky_one:
    lucky_name = random.choice(list(friends_dict.keys()))
    print(lucky_name, "is the lucky one!")
else:
    print("No one is going to be lucky")

total_price = round(bill / (num - int(lucky_one)), 2)

for p in friends_dict.keys():
    friends_dict[p] = total_price
if lucky_one:
    friends_dict[lucky_name] = 0
print(friends_dict)
