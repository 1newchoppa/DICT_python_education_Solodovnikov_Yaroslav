import sys
#Step 2

friends_dict = {}

num = int(input("Enter the number of friends joining (including you): "))
if num < 1:
    print("No one is joining for the party")
    sys.exit()


print("Enter the name of every friend (including you),each on new line: ")
for i in range(num):
    friends_names = input()
    friends_dict[friends_names] = 0

total_price = int(input("Enter the total amount"))
mq = round(total_price/num, 2)
for friends_names in friends_dict:
    friends_dict[friends_names] = mq
print(friends_dict)