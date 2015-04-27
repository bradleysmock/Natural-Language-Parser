__author__ = 'bradleyt79'

import re
import string
import parser_classes
import lexicon
import samples

# Global Constants
end_paragraph = ["\n", "||"]
end_sentence = [".", "?", "!"]
end_clause = [",", ":", ";", "- ", "' ", " '", '"', "(", ")"]
sub = end_sentence + end_clause

def tokenize(text):
        # Maybe slow...
        # For reference: sub = [".", "?", "!", ",", ":", ";", "- ", "'", '"', "(", ")"]
        for x in sub:
            text = text.replace("{}".format(x), " {} ".format(x))

        # Note: returns Mr. as ['Mr', '.']
        return text.split()

def parse(text):
    t = parser_classes.Text()
    tokens = tokenize(text)

    # initialize
    p = parser_classes.Paragraph()
    s = parser_classes.Sentence()
    c = parser_classes.Clause()

    # analyze tokens
    for token in tokens:
        # check for end of paragraph
        if token in end_paragraph:
            # add paragraph to Text, omitting token
            t.add(p.add(s.add(c.add)))
        else:
            # check for punctuation
            if token in string.punctuation:
                # check for end of sentence/clause
                if token in end_sentence:
                    # end sentence
                    s.add(c)
                    s.add(token)
                    p.add(s)
                    s = parser_classes.Sentence()
                elif token in end_clause:
                    # end clause
                    s.add(c)
                    s.add(token)
                    c = parser_classes.Clause()
                else:
                    # build clause
                    c.add(token)
            else:
                # build clause
                c.add(lexicon.wordtype(token))

    return t


def test_parse(text):
    print(parse(text).string())


test_parse(samples.t1)