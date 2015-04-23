__author__ = 'bradleyt79'
import frequency

# Local dictionary for testing
longman3000 = frequency.longman3000

def lookup_pos(word):
    for key in longman3000:
        if key[0] == word:
            print(key[1])
            return key[1]