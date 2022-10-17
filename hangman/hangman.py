import random
#Step 1

print('HANGMAN')

#Step 4
word_list = ["php" , "python" , "java" , "javascript"]
word_random = random.choice(word_list)
tire = (len(word_random)-3) * '-'
user_input = input('Guess the word: ' + word_random[0:2] + tire + "-\n")
while True:
    if user_input.strip() == word_random:
        print('You survived!')
        break
    else:
        print('You lost!')
        break