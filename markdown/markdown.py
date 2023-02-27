user_text = ""
edited_text = ""

user_command = ""

print("*******Markdown editor******* \n   Type <help> for show list of possible commands or <done> for save progress")

command_list = ['help', 'done', 'header', "plain", "link"]


def help():
    print(
        "Available formatters: plain, bold, italic, header, link, inline-code, ordered-list, unordered-list, new-line" '\n' "Special commands: help , done")


def done():
    print("Thanks for using, all text saved to 'text.txt'!")


def header():
    global edited_text
    global user_text
    global header_level
    header_level = int(input("Header level: "))
    if header_level < 7 and header_level > 0:
        user_text = input("Text: ")
        user_text = (str("#" * int(header_level) + " " + str(user_text)))
        edited_text += user_text + "\n"
        print(edited_text)
    else:
        print("The level sould be within the range of 1 to 6.")


def plain():
    global edited_text
    user_text = input("Enter plain text: ")
    edited_text += user_text + "\n"
    print(edited_text)


def link():
    global edited_text
    user_text = input("Label: ")
    edited_text += ("[" + (user_text) + "]")
    user_text = input("URL: ")
    edited_text += ("(" + (user_text) + ")" + "\n")
    print(edited_text)


while user_command != "done":
    user_command = str(input("Choose a formatter: "))
    if user_command in command_list:
        eval(user_command)()
    else:
        print("Unknown formatting type or command")
