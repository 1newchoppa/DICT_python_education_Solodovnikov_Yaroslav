import random
#Step 1

print('HANGMAN')

#Step 3
word_list = ["php" , "python" , "c#" , "c++"]
word_random = random.choice(word_list)
user_input = input('Guess the word:')
while True:
    if user_input.strip() == word_random:
        print('You survived!')
        break
    else:
        print('You lost!')
        break