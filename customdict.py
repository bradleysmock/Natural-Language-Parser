__author__ = 'bradleyt79'

import os

def opendict():
    with open("customdict", 'r') as f:
        return f.readlines()

def add(word):
    entries = opendict()
    # TODO finish!


def wordtype(word):
    # TODO after reformat dictionary - if word in dictionary.keys():
    for key in dictionary:
        if key[0] == word or key[0] == word.lower():
            return key[1]

dictionary = {
    ('the', 'Det'),
    ('mask', 'N'),
    ('screamed', 'V'),
    ('laughed', 'V'),
    ('cried', 'V'),
    ('petticoat', 'N'),
    ('smiled', 'V'),
    ('a', 'Det'),
    ('whined', 'V'),
    ('mewed', 'V'),
    ('Dr', 'N'),
    ('John', 'N'),
    ('said', 'V'),
    ('Mr', 'N'),
    ('Mrs', 'N'),
    ('Kim', 'N'),
    ('gave', 'V'),
    ('is', 'V'),
    ('eating', 'V'),
    ('delicious', 'Adj'),
    ('hotdog', 'N')
}