__author__ = 'bradleyt79'
import longman3000
import customdict

# Contains functions for dealing with dictionaries.

# Local dictionaries for testing
type_dicts = [longman3000, customdict]
freq_dicts = [longman3000]
# TODO link to NLTK for dictionaries

def wordtype(word):
    for type_dict in type_dicts:
        if type_dict.wordtype(word) is not None:
            return type_dict.wordtype(word)
        else:
            continue

    print("Word type not found. Please extend dictionaries to include {}.".format(word))
    # TODO in a future update add function to dynamically add these into the customdict
    return None

