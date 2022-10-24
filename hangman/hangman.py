import random
#Step 1

print('HANGMAN')

#Step 5
word_list = ["kotlin", "java", "php", "python"]
random_word = random.choice(word_list)
used_letters = []
letters = list(set(random_word))
word_correct = "".join([i if i in used_letters else "_" for i in random_word])
print(word_correct)
lifes = 8
while lifes > 0:
    letter = input("Input a letter:")
    if letter not in random_word:
        lifes -= 1
        print("That letter doesn't appear in the word")
    if letter in used_letters:
        lifes -= 1
        print("No improvements")
    if letter in random_word and letter not in used_letters:
        used_letters.append(letter)
        letters.remove(letter)
    word_correct = "".join([i if i in used_letters else "_" for i in random_word])
    print(word_correct)
    if lifes == 0 and len(letters) != 0:
        print("You lose!")
    if len(letters) == 0:
        print("You win!")
        break

print("thanks for playing\nWe'll see how well you did in the next stage")