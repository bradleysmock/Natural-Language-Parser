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
# TODO needs to be much more robust eventually
abbrev = ["Dr", "Mr", "Mrs"]

def tokenize(text):
        # Maybe slow...
        # For reference: sub = [".", "?", "!", ",", ":", ";", "- ", "'", '"', "(", ")"]
        for x in sub:
            text = text.replace("{}".format(x), " {} ".format(x))

        # Note: returns Mr. as ['Mr', '.']
        return text.split()

# Returns a Text object from a string
def parse(text):
    t = parser_classes.Text()
    tokens = tokenize(text)

    # initialize
    p = parser_classes.Paragraph()
    s = parser_classes.Sentence()
    c = parser_classes.Clause()

    # analyze tokens
    for n in range(0, len(tokens)):
        token = tokens[n]
        # check for last token
        if n == len(tokens) - 1:
            # add token as new clause (assumes end punctuation)
            s.add(c)
            c = parser_classes.Clause()
            c.add(token)
            s.add(c)
            p.add(s)
            t.add(p)
            break
        # check for end of paragraph
        elif token in end_paragraph:
            # add paragraph to Text, omitting token
            s.add(c)
            s.print()
            p.add(s)
            p.print()
            t.add(p)
            # reinitialize p, s, c
            p = parser_classes.Paragraph()
            s = parser_classes.Sentence()
            c = parser_classes.Clause()
        else:
            # check for punctuation
            if token in string.punctuation:
                # check for end of sentence/clause
                if token in end_sentence:
                    # check for abbreviations
                    if tokens[n-1] in abbrev:
                        c.add(token)
                    else:
                        # end sentence
                        c.add(token)
                        s.add(c)
                        p.add(s)
                        # reinitialize s, c
                        s = parser_classes.Sentence()
                        c = parser_classes.Clause()
                elif token in end_clause:
                    # end clause
                    s.add(c)
                    # add token as separate clause in s
                    s.add(parser_classes.Clause().add(token))
                    # reinitialize c
                    c = parser_classes.Clause()
                else:
                    # build clause
                    c.add(token)
            # if word (not punctuation)
            else:
                # build clause
                c.add(token)

    return t


# Tests
def test_tokenize(text):
    print(tokenize(text))


def test_parse(text):
    parsing = parse(text)

    # parsing.print()
    # parsing.printstats()

    pn = 1
    for p in parsing.paragraphs:
        print("\nParagraph {}".format(pn))
        # p.print()
        # p.printstats()

        sn = 1
        for s in p.sentences:
            print("Sentence {} - {}".format(sn, s.string()))
            # s.printstats()

            sn += 1

        pn += 1


# test_tokenize(samples.t2)
test_parse(samples.t1)