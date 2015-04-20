__author__ = 'bradleyt79'


class Paragraph:
    """group of sentences"""

    para_count = 0
    empty = []
    emptystring = ""

    def __init__(self, string):
        Paragraph.para_count += 1
        self.order = Paragraph.para_count
        self.string = string.strip()
        self.sentences = Paragraph.findsentences(self)
        self.length = len(self.sentences)


    def print(self):
        print(self.string)


    def findsentences(self):
        sentences = []
        if self.string != Paragraph.emptystring:
            for string in self.string.replace(". ", ".|").split("|"):
                sentences.append(Sentence(string))

        return sentences


class Sentence:
    """basic unit of written language"""

    sent_count = 0

    def __init__(self, string):
        Sentence.sent_count += 1
        self.order = Sentence.sent_count
        # self.orderp = num_in_para
        self.string = string
        self.words = string.lower().split()
        self.length = len(self.words)
        # self.type = self.findtype(self)
        # self.parts = self.findparts(self)
        # self.structType = self.findstructtype(self)