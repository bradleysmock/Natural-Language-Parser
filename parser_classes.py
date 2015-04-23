__author__ = 'bradleyt79'

import re
import parser


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

    def __init__(self, string):
        Text.para_count += 1
        self.order = Text.para_count
        self.tokens = self.tokenize(string)
        self.sentences = self.findsentences(self.tokens)
        self.sentence_count = len(self.sentences)

    def tokenize(self, string):
        # Maybe slow...
        sub = [".", "?", "!", ",", ":", ";", "- ", "' ", " '", '"', "(", ")"]
        for x in sub:
            string = string.replace("{}".format(x), " {} ".format(x))

        return string.split()

    def findsentences(self, tokens):
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

        self.string = " ".join(tokens)  # TODO remove space before punctuation
        self.words = tokens  # TODO remove punctuation
        self.length = len(self.words)
        self.wordset = set(self.words)
        self.uniquelength = len(self.wordset)

    def printstats(self):
        print("Sentence Stats for Sentence {:3}:".format(self.order))
        print("\t{:10}{:3}".format("Words:", self.length))
        print("\t{:10}{:3}".format("Unique:", self.uniquelength))
        print("\t{:10}{:3.2%}".format("% Unique:", self.uniquelength / self.length))


# Class Tests
sample = """In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income. The rest of it went in a doublet of fine cloth and velvet breeches and shoes to match for holidays, while on week-days he made a brave figure in his best homespun. He had in his house a housekeeper past forty, a niece under twenty, and a lad for the field and market-place, who used to saddle the hack as well as handle the bill-hook. The age of this gentleman of ours was bordering on fifty; he was of a hardy habit, spare, gaunt-featured, a very early riser and a great sportsman. They will have it his surname was Quixada or Quesada (for here there is some difference of opinion among the authors who write on the subject), although from reasonable conjectures it seems plain that he was called Quexana. This, however, is of but little importance to our tale; it will be enough not to stray a hair's breadth from the truth in the telling of it.
You must know, then, that the above-named gentleman whenever he was at leisure (which was mostly all the year round) gave himself up to reading books of chivalry with such ardour and avidity that he almost entirely neglected the pursuit of his field-sports, and even the management of his property; and to such a pitch did his eagerness and infatuation go that he sold many an acre of tillageland to buy books of chivalry to read, and brought home as many of them as he could get. But of all there were none he liked so well as those of the famous Feliciano de Silva's composition, for their lucidity of style and complicated conceits were as pearls in his sight, particularly when in his reading he came upon courtships and cartels, where he often found passages like "the reason of the unreason with which my reason is afflicted so weakens my reason that with reason I murmur at your beauty;" or again, "the high heavens, that of your divinity divinely fortify you with the stars, render you deserving of the desert your greatness deserves." Over conceits of this sort the poor gentleman lost his wits, and used to lie awake striving to understand them and worm the meaning out of them; what Aristotle himself could not have made out or extracted had he come to life again for that special purpose. He was not at all easy about the wounds which Don Belianis gave and took, because it seemed to him that, great as were the surgeons who had cured him, he must have had his face and body covered all over with seams and scars. He commended, however, the author's way of ending his book with the promise of that interminable adventure, and many a time was he tempted to take up his pen and finish it properly as is there proposed, which no doubt he would have done, and made a successful piece of work of it too, had not greater and more absorbing thoughts prevented him."""

sample1 = """The man in the mask screamed. The woman laughed. The boy cried.
The girl in the petticoat smiled. The dog with a bone whined. The cat mewed."""

t = Text(sample)

#t.print()
#t.printstats()

for p in t.paragraphs:
    # p.printstats()
    # p.print()

    for s in p.sentences:
        s.printstats()

#print(t.paragraphs[0].tokens)