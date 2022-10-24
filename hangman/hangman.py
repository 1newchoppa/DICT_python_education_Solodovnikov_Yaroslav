import random
#Step 1

print('HANGMAN')

#Step 5
lifes = 8
word_list = ["php" , "python" , "java" , "javascript"]
word_random = random.choice(word_list)
used = []
letters = list(set(word_random))
word_correct = "".join([i if i in used else "_" for i in word_random])
print(word_correct)
while lifes > 0:
    input_letter = input("Input a letter")
    if input_letter in word_random and input_letter not in used:
        used.append(input_letter)
        letters.remove(input_letter)
    else:
        lifes -= 1
    word_correct = "".join([i if i in used else "_" for i in word_random])
    print(word_correct)
    if len(letters) == 0:
        break
print('Thanks for playing!\n We`ll see how well you did the next stage')