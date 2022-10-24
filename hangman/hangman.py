import random
#Step 1

print('HANGMAN')

#Step 7
word_list = ["kotlin", "java", "php", "python"]
random_word = random.choice(word_list)
used_letters = []
used_letters_second = []
letters = list(set(random_word))
word_correct = "".join([i if i in used_letters else "_" for i in random_word])
print(word_correct)
lifes = 8
while lifes > 0:
    letter = input("Input a letter:")
    if letter == letter.lower() and len(letter) == 1:
        if letter in random_word and letter not in used_letters and letter not in used_letters_second:
            used_letters.append(letter)
            letters.remove(letter)
        elif letter in used_letters or letter in used_letters_second:
            print("You've already guessed this letter")
        else:
            print("That letter doesn't appear in the word")
            lifes -= 1
        word_correct = "".join([i if i in used_letters else "_" for i in random_word])
        print(word_correct)
        if len(letters) == 0:
            print("You guessed the word\nCongratulations you survived!")
            break
    elif letter != letter.lower():
        print("Please enter a lowercase English letter")
    elif len(letter) != 1:
        print("You should input a single letter")
if len(letters) > 0:
    print("You lost!")