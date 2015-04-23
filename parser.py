__author__ = 'bradleyt79'

import parser_classes as P


def tokenize(string):
        # Maybe slow...
        sub = [".", "?", "!", ",", ":", ";", "- ", "' ", " '", '"', "(", ")"]
        for x in sub:
            string = string.replace("{}".format(x), " {} ".format(x))

        return string.split()


def parse(text):
    # for now, separate text into one paragraph and multiple sentences
    p1 = P.Text(text)

    #p1.print()