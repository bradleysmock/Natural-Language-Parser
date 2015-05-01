__author__ = 'bradleyt79'

from nltk import pos_tag
from string import punctuation


# Simply returns the type of the word given it.
def wordtype(word):
    pos = pos_tag([word])[0][1]
    if pos in punctuation:
        return None
    else:
        # NLTK's POS Tagger is much more robust than my parser currently can handle.
        # Therefore, simplify the POS before passing to the parser.
        conversion = [
            ["CC", "Conj"],
            ["CD", "N"],
            ["DT", "Det"],
            ["EX", "N"],
            ["FW", "N"],
            ["IN", "Prep"],
            ["JJ", "Adj"],
            ["JJR", "Adj"],
            ["JJS", "Adj"],
            ["LS", "N"],
            ["MD", "Aux"],
            ["NN", "N"],
            ["NNP", "N"],
            ["NNPS", "N"],
            ["NNS", "N"],
            ["PDT", "Det"],
            ["POS", "Adj"],
            ["PRP", "N"],
            ["PRP$", "N"],
            ["RB", "Adv"],
            ["RBR", "Adv"],
            ["RBS", "Adv"],
            ["RP", "Prep"],
            ["TO", "Prep"],
            ["UH", "N"],
            ["VB", "V"],
            ["VBD", "V"],
            ["VBG", "V"],
            ["VBN", "V"],
            ["VBP", "V"],
            ["VBZ", "V"],
            ["WDT", "Det"],
            ["WP", "Pron"],
            ["WP$", "Pron"],
            ["WRB", "Adv"],
        ]
        for x in conversion:
            if pos == x[0]:
                return x[1]
            else:
                continue

    print("Could not match word type in NLTKdict. Please add {} to conversion.".format(pos))
    return None

# NLTKdict Tests


def runtests():
    from samples import tokens1, tokens2
    for word in tokens1:
        print(wordtype(word))

    for word in tokens2:
        print(wordtype(word))


# runtests()