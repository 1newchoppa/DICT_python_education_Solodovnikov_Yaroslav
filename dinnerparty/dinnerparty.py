#Step 1
friends_dict = {}
num = int(input("Enter the number of friends joining (including you): "))
if num < 1:
    print("No one is joining for the party")
for i in range(num):
    friends_names = input("Enter the name of every friend (including you),each on new line: ")
    friends_dict[friends_names] = 0
print(friends_dict)