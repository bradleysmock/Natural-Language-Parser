__author__ = 'bradleyt79'

import re
import parser
import string
import samples


class Text:
    """group of paragraphs"""

    para_count = 0
    sentence_count = 0
    word_count = 0

    def __init__(self, string):
        self.paragraphs = Text.findparagraphs(self, string)

    def findparagraphs(self, string):
        plst = []
        for p in filter(None, re.split("[\n|]", str(string))):
            plst.append(Paragraph(p.strip()))

        return plst

    def string(self):
        output = ""
        for p in self.paragraphs:
            output = "\n".join([output, p.string()])

        return output

    def print(self):
        print(self.string())

    def printstats(self):
        print("\nText Stats:")
        print("\tParagraphs: {}".format(self.para_count))
        print("\tSentences: {}".format(self.sentence_count))


class Paragraph:
    """group of sentences"""

    def __init__(self, s):
        Text.para_count += 1
        self.order = Text.para_count
        # TODO throws error "module has no attribute tokenize" when pulling from parser
        #self.tokens = parser.tokenize(s)
        self.tokens = self.tokenize(s)
        self.sentences = self.findsentences(self.tokens)
        self.sentence_count = len(self.sentences)
        self.word_count = len(self.words())
        self.unique_count = len(self.wordset())

    def tokenize(self, s):
        # Maybe slow...
        sub = [".", "?", "!", ",", ":", ";", "- ", "' ", " '", '"', "(", ")"]
        for x in sub:
            s = s.replace("{}".format(x), " {} ".format(x))

        return s.split()

    def words(self):
        return [x for x in self.tokens if x not in string.punctuation]

    def wordset(self):
        return set(self.words())

    def findsentences(self, tokens):
        # TODO better to send sentence as string or token list?
        sentencelist = []
        tokenlist = []
        endpunctuation = [".", "?", "!"]
        for x in tokens:
            if x in endpunctuation:
                tokenlist.append(x)
                sentencelist.append(Sentence(tokenlist))
                tokenlist = []
            else:
                tokenlist.append(x)

        return sentencelist

    def string(self):
        output = ""
        for s in self.sentences:
            output = " ".join([output, s.string])

        return output

    def print(self):
        print(self.string())

    def printsentences(self):
        n = 0
        for s in self.sentences:
            print("{:2}. {}".format(n, s.string))
            n += 1

    def printstats(self):
        print("\nParagraph Stats for Paragraph {}:".format(self.order))
        print("\tSentences: {}".format(self.sentence_count))


class Sentence:
    """basic unit of written language"""

    def __init__(self, tokens):
        Text.sentence_count += 1
        self.order = Text.sentence_count

        #TODO which base structure to use?
        #self.structure = ()
        #self.clauses =
        self.tokens = tokens

        # TODO change to functions to save memory?
        self.punct = [x for x in tokens if x in string.punctuation]
        # TODO lower except I and proper nouns
        self.words = sorted([x.lower() for x in tokens if x not in string.punctuation])

        self.length = len(self.words)
        self.wordset = sorted(list(set(self.words)))
        self.uniquelength = len(self.wordset)

    def string(self):
        " ".join(self.tokens)  # TODO remove space before punctuation?

    def print(self):
        print(self.string())

    def printstats(self):
        print("Sentence Stats for Sentence {:3}:".format(self.order))
        col1 = 12
        col2 = 6
        print("\t{:{col1}}{:>{col2}}".format("Words:", self.length, col1=col1, col2=col2))
        print("\t{:{col1}}{:>{col2}}".format("Unique:", self.uniquelength, col1=col1, col2=col2))
        print("\t{:{col1}}{:>{col2}.2%}".format("% Unique:", self.uniquelength / self.length, col1=col1, col2=col2))
        print("\t{:{col1}}{:>{col2}}".format("Punctuation:", len(self.punct), col1=col1, col2=col2))


# Class Tests

def runtests():
    t = Text(samples.t1)

    t.print()
    t.printstats()

    for p in t.paragraphs:
        p.printstats()
        p.print()

        for s in p.sentences:
            print(s.string)
            print(s.words)
            print(s.wordset)
            s.printstats()

# runtests()


# Outside Functions
def new_text(text):
    return Text(text)