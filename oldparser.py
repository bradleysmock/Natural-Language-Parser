__author__ = 'bradleyt79'

import re
import string
import lexicon
import samples

# Global Constants
end = [".", "?", "!"]
sub = [".", "?", "!", ",", ":", ";", "- ", "' ", " '", '"', "(", ")"]

def tokenize(text):
        # Maybe slow...
        # For reference: sub = [".", "?", "!", ",", ":", ";", "- ", "' ", " '", '"', "(", ")"]
        for x in sub:
            text = text.replace("{}".format(x), " {} ".format(x))

        return text.split()


class Text:
    """group of paragraphs"""

    para_count = 0
    sentence_count = 0
    word_count = 0

    def __init__(self, text):
        self.paragraphs = Text.find_paragraphs(self, text)

    def find_paragraphs(self, text):
        plst = []
        for p in filter(None, re.split("[\n|]", str(text))):
            plst.append(Paragraph(p.strip()))

        return plst

    def string(self):
        output = ""
        for paragraph in self.paragraphs:
            output = "\n".join([output, paragraph.string()])

        return output

    def print(self):
        print(self.string())

    def printstats(self):
        print("\nText Stats:")
        print("\tParagraphs: {}".format(self.para_count))
        print("\tSentences: {}".format(self.sentence_count))


class Paragraph:
    """group of sentences"""

    def __init__(self, text):
        Text.para_count += 1
        self.order = Text.para_count
        self.parsing = self.parse(text)
        self.sentences = self.split_sentences(text)
        self.sentence_count = len(self.sentences)
        self.word_count = len(self.words())
        # TODO FIX this: self.unique_count = len(self.wordset())

    def words(self):
        wordlist = []
        for sentence in self.sentences:
            wordlist.append(sentence.words())

        return sorted(wordlist)

    def wordset(self):
        return sorted(set(self.words()))

    def parse(self, text):
        sentencelist = []
        # tokenize
        tokens = tokenize(text)
        # analyze tokens
        for token in tokens:
            if lexicon.wordtype(token)
            # create sentences
        return

    def split_sentences(self, text):
        sentencelist = []
        # ignorelist = ["Mr.", "Dr.", "Mrs.", "Sr.", "Jr.", "e.g.", "i.e.", "etc."]
        # TODO fails at Mr. etc. and deletes end punctuation
        for sentence in filter(None, re.split(r' *[\.\?!][\'"\)\]]* *', text)):
            sentencelist.append(Sentence(sentence))

        return sentencelist

    def string(self):
        output = ""
        for sentence in self.sentences:
            output = " ".join([output, sentence.string()])

        return output

    def print(self):
        print(self.string())

    def printsentences(self):
        n = 0
        for sentence in self.sentences:
            print("{:2}. {}".format(n, sentence.string))
            n += 1

    def printstats(self):
        print("\nParagraph Stats for Paragraph {}:".format(self.order))
        print("\tSentences: {}".format(self.sentence_count))


class Sentence:
    """basic unit of written language"""

    def __init__(self, text):
        Text.sentence_count += 1
        self.order = Text.sentence_count
        self.tokens = self.tokenize(text)
        self.clauses = self.parse()
        self.length = len(self.words())
        self.word_count = self.length
        self.unique_count = len(self.wordset())

    def tokenize(self, string):
        # Maybe slow...
        # For reference: sub = [".", "?", "!", ",", ":", ";", "- ", "' ", " '", '"', "(", ")"]
        for x in sub:
            string = string.replace("{}".format(x), " {} ".format(x))

        return string.split()

    def parse(self):
        # TODO
        return []

    def punctuation(self):
        return [x for x in self.tokens if x in string.punctuation]

    def words(self):
        # TODO exempt I and proper nouns from lower()
        return sorted([x.lower() for x in self.tokens if x not in string.punctuation])

    def wordset(self):
        return sorted(set(self.words()))

    def string(self):
        return " ".join(self.tokens)

    def print(self):
        print(self.string())

    def printstats(self):
        print("\nSentence Stats for Sentence {}:".format(self.order))
        col1 = 12
        col2 = 6
        print("\t{:{col1}}{:>{col2}}".format("Words:", self.length, col1=col1, col2=col2))
        print("\t{:{col1}}{:>{col2}}".format("Unique:", self.unique_count, col1=col1, col2=col2))
        print("\t{:{col1}}{:>{col2}.2%}".format("% Unique:", self.unique_count / self.length, col1=col1, col2=col2))
        print("\t{:{col1}}{:>{col2}}".format("Punctuation:", len(self.punctuation()), col1=col1, col2=col2))


# Class Tests

def runtests():
    t = Text(samples.t1)

    t.print()
    t.printstats()

    for p in t.paragraphs:
        p.printstats()
        p.print()

        for s in p.sentences:
            s.printstats()
            print(s.tokens)
            s.print()
            print(s.words())
            print(s.wordset())


runtests()

# External Functions
def parse(text):
    return Text(text)