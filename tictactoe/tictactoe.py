values = input("Enter cells\n> ")
print("---------")
for n,i in enumerate(values):
    if n % 3 == 0:
       print('|', end="")
    print(i, end='')
    if n % 3 == 2:
        print("|")
print("---------")