__author__ = 'bradleyt79'

from nltk import pos_tag


# Simply returns the type of the word given it.
def wordtype(word):
    return pos_tag([word])

# NLTKdict Tests


def runtests():
    from samples import tokens1, tokens2
    for word in tokens1:
        print(wordtype(word))


# runtests()