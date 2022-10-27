import sys
import random
#Step 3

friends_dict = {}

num = int(input("Enter the number of friends joining (including you): "))
if num < 1:
    print("No one is joining for the party")
    sys.exit()


print("Enter the name of every friend (including you),each on new line: ")
for i in range(num):
    friends_names = input()
    friends_dict[friends_names] = 0

lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
lucky_one = ""
if lucky_feature == 'Yes':
    lucky_one = random.choice(list(friends_dict.keys()))
    print(lucky_one, "is lucky today!")
else:
    print("No one is going to be lucky")

total_price = int(input("Enter the total amount"))
mq = round(total_price/num, 2)
for friends_names in friends_dict:
    friends_dict[friends_names] = mq
#print(friends_dict)