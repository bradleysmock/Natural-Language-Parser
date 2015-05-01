__author__ = 'bradleyt79'
import nltkdict
import longman3000
import customdict

# Contains functions for dealing with dictionaries.

# Local dictionaries for testing
type_dicts = [nltkdict, longman3000, customdict]
# Future expansion -- freq_dicts = [nltkdict, longman3000]


# Simply returns the type of the word given it by querying the type_dicts until the word is found.
def word_type(word):
    for type_dict in type_dicts:
        if type_dict.word_type(word) is not None:
            return type_dict.word_type(word)
        else:
            continue

    print("Word type not found. Please extend dictionaries to include {}.".format(word))
    # Future expansion: add function to dynamically add these into the customdict
    return None

