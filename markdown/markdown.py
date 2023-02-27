user_text = ""
edited_text = ""

user_command = ""

print("*******Markdown editor******* \n   Type <help> for show list of possible commands or <done> for save progress")

command_list = ['help', 'done', 'header', "plain", "link", "ordered_list", "unordered_list"]


def help():
    print(
        "Available formatters: plain, bold, italic, header, link, inline-code, ordered_list, unordered_list, new-line" '\n' "Special commands: help , done")


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


def ordered_list():
    global edited_text
    global user_text
    global row_number
    global number_list
    row_number = int(input("Number of rows: "))
    if row_number > 0:
        for i in range(row_number):
            print("Row #", i + 1)
            user_text = input()
            number_list = i + 1
            edited_text += (str(number_list) + "." + user_text + '\n')
        print(edited_text)
    else:
        print("The number of rows should be greather than zero")


def unordered_list():
    global edited_text
    global user_text
    global row_number
    row_number = int(input("Number of rows: "))
    if row_number > 0:
        for j in range(row_number):
            print("Row #", j + 1)
            user_text = input()
            edited_text += ("*" + user_text + '\n')
        print(edited_text)
    else:
        print("The number of rows should be greather than zero")


while user_command != "done":
    user_command = str(input("Choose a formatter: "))
    if user_command in command_list:
        eval(user_command)()
    else:
        print("Unknown formatting type or command")
