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
# Future expansion: abbrev list needs to be much more robust
abbrev = ["Dr.", "Mr.", "Mrs.", "etc.", "e.g.", "i.e."]


# Breaks a text (string) into tokens.
def tokenize(text):
        # Future expansion: revise for better speed and efficiency
        for x in abbrev:
            text = text.replace("{}".format(x), "{}".format(x[:-1]))

        for x in sub:
            text = text.replace("{}".format(x), " {} ".format(x))

        return text.split()


def splitby(tokens, splitlist):
    returnlist = []
    part = []
    for n in range(0, len(tokens)):
        token = tokens[n]
        if n == len(tokens) - 1:
            part.append(token)
            returnlist.append(part)
        elif token in splitlist:
            part.append(token)
            returnlist.append(part)
            part = []
        else:
            part.append(token)
            
    return returnlist


def splitintosentences(tokens):
    return splitby(tokens, end_sentence)


def splitintoparagraphs(tokens):
    return splitby(tokens, end_paragraph)


# Returns a Text object from a string
def parse(text):
    newText = parser_classes.Text()
    tokens = tokenize(text)
    paragraphs = splitintoparagraphs(tokens)
    for paragraph in paragraphs:
        newParagraph = parser_classes.Paragraph()
        sentences = splitintosentences(paragraph)
        for sentence in sentences:
            # remove paragraph ends
            if sentence[0] in end_paragraph:
                continue
            else:
                newSentence = parser_classes.Sentence()
                newSentence.build(sentence)
                newParagraph.add(newSentence)

        newText.add(newParagraph)

    return newText

# Tests
def test_tokenize(text):
    print(tokenize(text))


def test_parse(text):
    parsing = parse(text)

    parsing.print()
    parsing.printstats()

    pn = 1
    for p in parsing.paragraphs:
        print("\nParagraph {}".format(pn))
        p.print()
        p.printstats()
        print("")

        sn = 1
        for s in p.sentences:
            print("Sentence {} - {}".format(sn, s.string()))
            print(s.structurestring())
            s.printstats()
            print("")

            sn += 1

        pn += 1


# test_tokenize(samples.t2)
test_parse(samples.t1)