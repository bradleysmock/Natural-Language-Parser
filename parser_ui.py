__author__ = 'bradleyt79'

import parser

# menu parts and UI strings
welcome = "\n*** Welcome to Bradley's Natural Language Parser ***"
farewell = "Have a great day!"
header = "\nPlease choose from these available options:"
menuitems = [
    ("Parse Text to Screen", "Analyze syntax of a text you type in and display the results on screen",
     lambda: parse_input()),
    ("Parse Text to File", "Analyze syntax of a text you type in and store the results in a file",
     lambda: print("2 TODO")),
    ("Parse File to Screen", "Analyze syntax of a text file and display the results on screen",
     lambda: print("3 TODO")),
    ("Parse File to File", "Analyze syntax of a text you type in and store the results in a file",
     lambda: print("4 TODO")),
    ("Exit", "", "")
    ]
prompt_menu = "\nWhat would you like to do today? "
prompt_text = "\nPlease enter the text you would like to process below:\n"
prompt_file = "\nPlease enter the path (directory/filename) to the file you would like to process below:\n"


def parse_input():
    text = input(prompt_text)
    parser.parse(text)

# setup menu
menulines = []
count = 1
for item in menuitems:
    menulines.append("\t{}. {:25}{}".format(count, item[0], item[1]))
    count += 1

menustring = "\n".join(menulines)

# output welcome and loop menu/prompt
print(welcome)
while True:
    print(header, menustring, sep="\n")
    choice = int(input(prompt_menu))
    if choice == len(menulines):
        print(farewell)
        break
    else:
        menuitems[choice-1][2]()