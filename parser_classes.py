__author__ = 'bradleyt79'

import lexicon
import grammar
import string

class Text:
    """group of paragraphs"""

    def __init__(self):
        self.paragraphs = []

    def add(self, paragraph):
        self.paragraphs.append(paragraph)

    def paragraph_count(self):
        return len(self.paragraphs)

    def sentence_count(self):
        return sum(x.sentence_count() for x in self.paragraphs)

    def word_count(self):
        return sum(x.word_count() for x in self.paragraphs)

    def string(self):
        return " ".join(x.string() for x in self.paragraphs)

    def print(self):
        print(self.string())

    def printstats(self):
        print("\nText Stats:")
        print("\tParagraphs: {}".format(self.paragraph_count()))
        print("\tSentences: {}".format(self.sentence_count()))
        print("\tWords: {}".format(self.word_count()))


class Paragraph:
    """group of sentences"""

    def __init__(self):
        self.sentences = []

    def add(self, sentence):
        self.sentences.append(sentence)

    def sentence_count(self):
        return len(self.sentences)

    def word_count(self):
        return sum(x.word_count() for x in self.sentences)

    def string(self):
        return " ".join(sentence.string() for sentence in self.sentences)

    def print(self):
        print(self.string())

    def printstats(self):
        print("\nParagraph Stats:")
        print("\tSentences: {}".format(self.sentence_count()))
        print("\tWords: {}".format(self.word_count()))


class Sentence:
    """basic unit of written language"""

    def __init__(self):
        self.clauses = []

    def add(self, clause):
        self.clauses.append(clause)

    def word_count(self):
        return sum(x.word_count() for x in self.clauses)

    def string(self):
        return " ".join(clause.string() for clause in self.clauses)

    def print(self):
        print(self.string())

    def printstats(self):
        print("Sentence Stats:")
        print("Words: {}".format(self.word_count()))


class Clause:
    """sub-unit of a sentence"""

    def __init__(self):
        self.parts = []
        self.type = "Unknown"
        # For reference: grammar.C: (Conj, AdvP, NP, VP, IO, DO, AdvP)
        self.structure = grammar.C

    def add(self, part):
        # add punctuation
        if part in string.punctuation:
            self.parts.append(part)
        # add word
        else:
            #  get word type
            wordtype = lexicon.wordtype(part)
            # consult grammar
            phrase = grammar.phrasetype(wordtype)
            print(phrase)
            # able to add to current clause?
            if True:
                self.parts.append(part)
                return True
            else:
                return False


    def word_count(self):
        return sum([1 for x in self.parts if x.isalnum()])

    def string(self):
        return " ".join(self.parts)

    def print(self):
        print(self.string())

    def printstats(self):
        print("Clause Stats:")
        print("\tWords: {}".format(self.word_count()))
        print("\tStructure: {}".format(self.structure))


# External Functions
def newClause(part):
    return Clause().add(part)


# Class Tests
def run_tests():
    sentences = [
        [['The', 'man', 'in', 'the', 'mask', 'screamed'], ['.']],
        [['The', 'woman', 'laughed'], ['.']],
        [['The', 'boy', 'cried'], ['.']],
        [['The', 'girl', 'in', 'the', 'petticoat', 'smiled'], ['.']],
        [['The', 'dog', 'with', 'a', 'bone', 'whined'], ['.']],
        [['The', 'cat', 'mewed'], ['.']],
        [['Dr', '.', 'John', 'said'], ['hello'], ['.']],
        [['Mr', '.', 'Kim', 'gave', 'Mrs', '.', 'Kim', 'a', 'gift'], ['.']]
    ]

    t = Text()
    p = Paragraph()
    for sentence in sentences:
        s = Sentence()
        for clause in sentence:
            c = Clause()
            for part in clause:
                c.add(part)

            s.add(c)
            c.print()
            # c.printstats()

        p.add(s)
        # s.print()
        # s.printstats()

    # print("\nParagraph:\n{}".format(p.string()))
    # p.printstats()

    t.add(p)
    # print("\nText:\n{}".format(t.string()))
    # t.printstats()


run_tests()

