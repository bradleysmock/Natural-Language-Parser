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

    def filledstructurestring(self):
        return " ".join(paragraph.filledstructurestring() for paragraph in self.paragraphs)

    def print(self):
        print(self.string())

    def printfilledstructure(self):
        print(self.filledstructurestring())

    def getstats(self):
        return "\n".join(["Text Stats:",
                          "\tParagraphs: {}".format(self.paragraph_count()),
                          "\tSentences: {}".format(self.sentence_count()),
                          "\tWords: {}".format(self.word_count())])

    def printstats(self):
        print(self.getstats())


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

    def structurestring(self):
        return " ".join(sentence.structurestring() for sentence in self.sentences)

    def filledstructurestring(self):
        return " ".join(sentence.filledstructurestring() for sentence in self.sentences)

    def print(self):
        print(self.string())

    def printfilledstructure(self):
        print(self.filledstructurestring())

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

    def buildfromclauses(self, clauselist):
        # print(clauselist)
        for clause in clauselist:
            if type(clause) is Clause:
                # assumes the clause is complete
                self.add(clause)
            else:
                # convert to Clause(s)
                self.build(clause)

    # converts a list of tokens to one or more Clauses
    def build(self, tokens):
        c = Clause()
        total = len(tokens)
        remaining = len(tokens)
        strikes = 0
        while remaining > 0 and strikes < 2:
            # Add token to clause
            success = c.add(tokens[total - remaining])
            if success is True:
                remaining -= 1
                strikes = 0
                if remaining == 0:
                    # future version: revise this because it's clumsy but works
                    # add partial final phrase if any
                    c.addfinal()
                    self.clauses.append(c)
            elif success is False:
                # Clause is full, so add to self.clauses and start new clause
                self.clauses.append(c)
                c = Clause()
                # print("\tCreating new clause: {}".format(c))
                strikes += 1
            else:
                print("Error in S.build with {}".format(tokens[total-remaining]))
                break

    def word_count(self):
        return sum(x.word_count() for x in self.clauses)

    def string(self):
        return " ".join(clause.string() for clause in self.clauses)

    def clausestrings(self):
        return [clause.string() for clause in self.clauses]

    def structurestring(self):
        return " ".join([x.structurestring() for x in self.clauses])

    def filledstructurestring(self):
        return " ".join([clause.filledstructurestring() for clause in self.clauses])

    def structure(self):
        return [x.structure() for x in self.clauses]

    def filledstructure(self):
        return [x.filledstructure() for x in self.clauses]

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
            if not self.finalphrase.isempty:
                self.parts.append(self.finalphrase)
                self.finalphrase = ""

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

    def string(self):
        stringlist = []
        for x in self.parts:
            if type(x) is str:
                stringlist.append(x.strip())
            else:
                stringlist.append(x.string().strip())

        return " ".join(stringlist)

    def structurestring(self):
        return " ".join(self.structure())

    def filledstructurestring(self):
        return str(self.filledstructure())

    def structure(self):
        partslist = []
        for part in self.parts:
            if type(part) is str:
                partslist.append(part)
            else:
                partslist.append(part.type)

        return partslist

    def filledstructure(self):
        partslist = []
        for part in self.parts:
            if type(part) is str:
                partslist.append(part)
            else:
                partslist.append((part.type, part.string()))

        return partslist

    def print(self):
        print(self.string())

    def printstructure(self):
        print(self.structure())

    def printfilledstructure(self):
        print(self.filledstructure())

    def printstats(self):
        print("Clause Stats:")
        print("\tWords: {}".format(self.word_count()))
        print("\tStructure: {}".format(self.structure()))


# Parser Class Tests
def run_tests():
    sentences = [
        ['The', 'man', 'in', 'the', 'mask', 'screamed', '.'],
        ['The', 'woman', 'laughed', '.'],
        ['The', 'boy', 'cried', '.'],
        ['The', 'girl', 'in', 'the', 'petticoat', 'smiled', '.'],
        ['The', 'dog', 'with', 'a', 'bone', 'whined', '.'],
        ['The', 'cat', 'mewed', '.'],
        ['Dr', 'John', 'said', 'hello', '.'],
        ['Mr', 'Kim', 'gave', 'Mrs', 'Kim', 'a', 'gift', '.']
    ]

    t = Text()
    p = Paragraph()
    for sentence in sentences:
        s = Sentence()
        s.build(sentence)
        for clause in s.clauses:
            clause.print()
            clause.printstructure()
            clause.printfilledstructure()
            clause.printstats()
        print("\nSentence: {}".format(s.string()))
        print("\tStructure: {}".format(s.structurestring()))
        print("\tStructure Filled: {}".format(s.filledstructurestring()))
        s.printstats()
        p.add(s)

    print("\nParagraph:\n{}".format(p.string()))
    p.printstats()

    t.add(p)
    print("\nText:\n{}".format(t.string()))
    t.printstats()


# run_tests()