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
        return self.clauses.append(clause)

    def build(self, clauselist):
        print(clauselist)
        for clause in clauselist:
            if type(clause) is Clause:
                self.add(clause)
            else:
                # convert clause to several Clauses
                print(clause)
                self.clauses.append(Clause())
                total = len(clause)
                remaining = total
                strikes = 0
                while remaining > 0 and strikes < 3:
                    print(self.clauses[-1].string())
                    success = self.clauses[-1].add(clause[total - remaining])
                    if success is True:
                        remaining -= 1
                        strikes = 0
                        continue
                    elif success is False:
                        self.clauses.append(Clause())
                        strikes += 1
                        continue
                    else:
                        break

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
        # Define clause structure from grammar
        # For reference: grammar.C: [Conj, AdvP, NP, VP, IO, DO, AdvP]
        self.model_structure = grammar.C

    def add(self, token):
        # add punctuation
        if token in string.punctuation:
            self.parts.append(token)
        # add word
        else:
            # add token to phrase within clause
            for phrase in self.model_structure:
                if grammar.addtophrase(token, phrase) is None:
                    # add failed -- look in next phrase
                    # if phrase is not empty add to clause parts
                    if not phrase.isempty:
                        self.parts.append(phrase)

                    self.model_structure = self.model_structure[1:]
                else:
                    # add successful!
                    print(phrase.string())
                    phrase.isempty = False
                    return True

            if self.model_structure == grammar.empty_C:
                print("clause is full")
                return False

            return None

    def word_count(self):
        return sum([1 for x in self.parts if x not in string.punctuation])

    def string(self):
        # stringlist = []
        # for x in self.parts:
        #     if type(x) is str:
        #         stringlist.append(x)
        #     else:
        #         stringlist.append(x.string())
        # TODO
        return self.parts

    def print(self):
        print(self.string())

    def printstats(self):
        print("Clause Stats:")
        print("\tWords: {}".format(self.word_count()))
        print("\tStructure: {}".format(self.model_structure))


# Class Tests
def run_tests():
    sentences = [
        [['The', 'man', 'in', 'the', 'mask', 'screamed'], ['.']]  #,
        # [['The', 'woman', 'laughed'], ['.']],
        # [['The', 'boy', 'cried'], ['.']],
        # [['The', 'girl', 'in', 'the', 'petticoat', 'smiled'], ['.']],
        # [['The', 'dog', 'with', 'a', 'bone', 'whined'], ['.']],
        # [['The', 'cat', 'mewed'], ['.']],
        # [['Dr', '.', 'John', 'said'], ['hello'], ['.']],
        # [['Mr', '.', 'Kim', 'gave', 'Mrs', '.', 'Kim', 'a', 'gift'], ['.']]
    ]

    t = Text()
    p = Paragraph()
    for sentence in sentences:
        s = Sentence()
        s.build(sentence)

        p.add(s)
        # s.print()
        # s.printstats()

    # print("\nParagraph:\n{}".format(p.string()))
    # p.printstats()

    t.add(p)
    # print("\nText:\n{}".format(t.string()))
    # t.printstats()


run_tests()