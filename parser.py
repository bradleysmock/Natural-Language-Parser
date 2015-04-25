__author__ = 'bradleyt79'

import string as S
import parser_classes as P
import lexicon as L
import samples

# Parser globals
end = [".", "?", "!"]
sub = [".", "?", "!", ",", ":", ";", "- ", "' ", " '", '"', "(", ")"]

def tokenize(string):
        # Maybe slow...
        for x in sub:
            string = string.replace("{}".format(x), " {} ".format(x))

        return string.split()


def parse(text):
    # convert to Text
    # TODO throws error "module has no attribute X" when run parse.py but not parse_ui
    # t = P.new_text(text)
    t = P.Text(text)
    for p in t.paragraphs:
        for s in p.sentences:
            print(s.tokens)
            structure = []
            for token in s.tokens:
                # TODO still very unfinished
                if token not in end:
                    structure.append(L.wordtype(token))


            print(structure)


# Parser tests
parse(samples.t1)