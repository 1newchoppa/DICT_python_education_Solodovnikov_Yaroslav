user_command = ""

print("*******Markdown editor******* \n   Type <help> for show list of possible commands or <done> for save progress")

command_list = ['help', 'done']

def help():
    print("Available formatters: plain, bold, italic, header, link, inline-code, ordered-list, unordered-list, new-line" '\n' "Special commands: help , done")

def done():
    print("Thanks for using, all text saved to 'text.txt'!")

while user_command != "done":
    user_command = str(input("Choose a formatter: "))
    if user_command in command_list:
        eval(user_command)()
    else:
        print("Unknown formatting type or command")
