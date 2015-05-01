from builtins import print

__author__ = 'bradleyt79'

import parser

# menu parts and UI strings
welcome = "\n*** Welcome to Bradley's Natural Language Parser ***"
farewell = "Have a great day!"
header = "\nPlease choose from these available options:"
menu_items = [
    ("Parse Text to Screen", "Analyze syntax of a text you type in and display the results on screen",
     lambda: parse_input(True, True)),
    ("Parse Text to File", "Analyze syntax of a text you type in and store the results in a file",
     lambda: parse_input(True, False)),
    ("Parse File to Screen", "Analyze syntax of a text file and display the results on screen",
     lambda: parse_input(False, True)),
    ("Parse File to File", "Analyze syntax of a text you type in and store the results in a file",
     lambda: parse_input(False, False)),
    ("Exit", "", "")
]
prompt_menu = "\nWhat would you like to do today? "
prompt_text = "\nPlease enter the text you would like to process below. Use || to designate paragraph breaks.\n"
prompt_file = "\nPlease enter the filename (including the path) of the file you would like to process below:\n"
prompt_fileout = "\nPlease enter the filename (including the path) of the file you would like to save to:\n"
pause = "\nPress enter to continue.\n"
invalid = "\nInvalid entry. Please try again.\n"
file_written = "\nFile written successfully.\n"
file_read = "\nFile read successfully.\n"
file_error = "\nSorry, could not write to/read from file.\n"
output_header = "\nParser Results:"
output_footer = "\nRemember, parsing natural language isn't an exact science!"


def parse_input(from_screen, to_screen):
    # get text to parse
    if from_screen is True:
        text_to_parse = input(prompt_text)
    else:
        file_path = input(prompt_file)
        with open(file_path) as file:
            text_to_parse = file.read()

    # parse text
    parsed = parser.parse(text_to_parse)

    # output parsed text
    output = "\n\n".join([output_header,
                          parsed.filled_structure_string(),
                          parsed.get_stats(),
                          output_footer])
    if to_screen is True:
        print(output)
    else:
        file_path = input(prompt_fileout)
        with open(file_path, 'w') as file:
            success = file.write(output)
            if success:
                print(file_written)
            else:
                print(file_error)

    # pause before continuing
    input(pause)


# setup menu
menu_lines = []
count = 1
for item in menu_items:
    menu_lines.append("\t{}. {:25}{}".format(count, item[0], item[1]))
    count += 1

menu_string = "\n".join(menu_lines)

# output welcome and loop menu/prompt
print(welcome)
while True:
    print(header, menu_string, sep="\n")
    choice = input(prompt_menu)
    try:
        choice = int(choice)
    except ValueError:
        print(invalid)
        continue
    if choice > len(menu_lines):
        print(invalid)
        continue
    elif choice == len(menu_lines):
        print(farewell)
        break
    else:
        menu_items[choice - 1][2]()