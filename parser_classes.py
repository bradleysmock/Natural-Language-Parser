__author__ = 'bradleyt79'

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
        # print(clauselist)
        for clause in clauselist:
            if type(clause) is Clause:
                # assumes the clause is complete
                self.add(clause)
            else:
                # convert clause to several Clauses
                total = len(clause)
                remaining = total
                # Strikes prevent against infinite loops of "Full" clauses
                strikes = 0
                c = Clause()
                while remaining > 0 and strikes < 2:
                    # Add phrase to clause
                    # print("Making Clause {}".format(c))
                    success = c.add(clause[total - remaining])
                    if success is True:
                        remaining -= 1
                        strikes = 0
                        if remaining == 0:
                            # TODO clumsy but works
                            #  add partial final phrase if any
                            c.addfinal()
                            self.clauses.append(c)
                    elif success is False:
                        # Clause is full, so add to self.clauses and start new clause
                        self.clauses.append(c)
                        c = Clause()
                        # print("\tCreating new clause: {}".format(c))
                        strikes += 1
                    else:
                        print("Error in S.build with {}".format(clause))
                        break

                # self.clauses.append(c)

    def structure(self):
        return [x.type() for x in self.clauses]

    def word_count(self):
        return sum(x.word_count() for x in self.clauses)

    def string(self):
        return " ".join(clause.string() for clause in self.clauses)

    def clausestrings(self):
        return [clause.string() for clause in self.clauses]

    def print(self):
        print(self.string())

    def printstats(self):
        print("Sentence Stats:")
        print("Words: {}".format(self.word_count()))


class Clause:
    """sub-unit of a sentence"""

    def __init__(self):
        # Parts are what are actually in the Clause
        self.parts = []
        self.num_words = 0
        # Define possible Clause structure from grammar
        self.model_structure = grammar.C().value
        self.finalphrase = ""

    # Adds a single token to the clause. Returns True if successful, False if the clause if full, and None if error.
    def add(self, token):
        # add punctuation
        if token in string.punctuation:
            self.parts.append(token)
            return True
        # add word
        else:
            # add token to phrase within clause
            for phrase in self.model_structure:
                # TODO addtophrase doesn't handle PP correctly
                if grammar.addtophrase(token, phrase) is None:
                    # add failed -- look in next phrase
                    self.model_structure = self.model_structure[1:]
                    # if phrase is not empty add to clause parts
                    if not phrase.isempty:
                        self.parts.append(phrase)
                        self.finalphrase = ""

                else:
                    # add successful!
                    phrase.isempty = False
                    self.num_words += 1
                    self.finalphrase = phrase
                    return True

            if self.model_structure == grammar.empty_C:
                # clause is full
                return False

            return None

    def addfinal(self):
        if self.finalphrase != '':
            self.parts.append(self.finalphrase)

    def word_count(self):
        return self.num_words

    def structure(self):
        partslist = []
        for part in self.parts:
            if type(part) is str:
                partslist.append(part)
            else:
                partslist.append(part.type)

        return partslist

    def string(self):
        stringlist = []
        for x in self.parts:
            if type(x) is str:
                stringlist.append(x.strip())
            else:
                stringlist.append(x.string().strip())

        return " ".join(stringlist)

    def print(self):
        print(self.string())

    def printstats(self):
        print("Clause Stats:")
        print("\tWords: {}".format(self.word_count()))
        print("\tStructure: {}".format(self.structure()))


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
        s.build(sentence)
        # for clause in s.clauses:
        #    clause.printstats()
        print("\nSentence: {}\n\t{}".format(s.string(), s.clausestrings()))
        s.printstats()
        p.add(s)

    print("\nParagraph:\n{}".format(p.string()))
    p.printstats()

    t.add(p)
    print("\nText:\n{}".format(t.string()))
    t.printstats()


run_tests()