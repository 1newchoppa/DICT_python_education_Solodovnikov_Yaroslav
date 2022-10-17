#Step 1
print('HANGMAN')
print('The game will be available soon.')

#Step 2
word = ("php")
user_input = input('Guess the word:')
while True:
    if user_input.strip() == word:
        print('You survived!')
        break
    else:
        print('You lost!')
        break