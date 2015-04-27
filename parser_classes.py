__author__ = 'bradleyt79'

class Text:
    """group of paragraphs"""

    def __init__(self):
        self.paragraphs = []

    def add(self, paragraph):
        self.paragraphs.append(paragraph)

    def paragraph_count(self):
        len(self.paragraphs)

    def sentence_count(self):
        count = 0
        for paragraph in self.paragraphs:
            count += paragraph.sentence_count

        return count

    def string(self):
        output = ""
        for paragraph in self.paragraphs:
            output = "\n".join([output, paragraph.string()])

        return output

    def print(self):
        print(self.string())

    def printstats(self):
        print("\nText Stats:")
        print("\tParagraphs: {}".format(self.paragraph_count()))
        print("\tSentences: {}".format(self.sentence_count))


class Paragraph:
    """group of sentences"""

    def __init__(self):
        self.sentences = []

    def add(self, sentence):
        self.sentences.append(sentence)

    def sentence_count(self):
        len(self.sentences)

    def word_count(self):
        count = 0
        for sentence in self.sentences:
            count += sentence.word_count

        return count

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
        print("\nParagraph Stats:")
        print("\tSentences: {}".format(self.sentence_count))


class Sentence:
    """basic unit of written language"""

    def __init__(self):
        self.clauses = []
        #self.length = len(self.words())
        #self.word_count = self.length
        #self.unique_count = len(self.wordset())

    def add(self, clause):
        self.clauses.append(clause)

    def string(self):
        " ".join(self.clauses)


class Clause:
    """sub-unit of a sentence"""

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def string(self):
        " ".join(self.parts)