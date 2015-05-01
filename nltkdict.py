__author__ = 'bradleyt79'

from nltk import pos_tag
from string import punctuation


# Simply returns the type of the word given it.
def wordtype(word):
    pos = pos_tag([word])[0][1]
    if pos in punctuation:
        return None
    else:
        conversion = [
            ["DT", "Det"],
            ["NN", "N"],
            ["IN", "Prep"],
            ["VBD", "V"],
            ["NNP", "N"],
            ["NNS", "N"]
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


# runtests()