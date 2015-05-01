from builtins import print

__author__ = 'bradleyt79'

import parser
import lexical

# menu parts and UI strings
welcome = "\n*** Welcome to Bradley's Natural Language Parser ***"
farewell = "Have a great day!"
header = "\nPlease choose from these available options:"
menuitems = [
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


def parse_input(fromscreen, toscreen):
    # get text to parse
    if fromscreen is True:
        text_to_parse = input(prompt_text)
    else:
        filepath = input(prompt_file)
        with open(filepath) as file:
            text_to_parse = file.read()

    # parse text
    parsed = parser.parse(text_to_parse)

    # output parsed text
    output = "\n\n".join([output_header,
                        parsed.filledstructurestring(),
                        parsed.getstats(),
                        output_footer])
    if toscreen is True:
        print(output)
    else:
        filepath = input(prompt_fileout)
        with open(filepath, 'w') as file:
            success = file.write(output)
            if success:
                print(file_written)
            else:
                print(file_error)

    # pause before continuing
    input(pause)


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
    choice = input(prompt_menu)
    try:
        choice = int(choice)
    except ValueError:
        print(invalid)
        continue
    if choice > len(menulines):
        print(invalid)
        continue
    elif choice == len(menulines):
        print(farewell)
        break
    else:
        menuitems[choice-1][2]()