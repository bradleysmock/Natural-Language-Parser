__author__ = 'bradleyt79'

import os

def opendict():
    with open("customdict", 'r') as f:
        return f.readlines()

def add(word):
    entries = opendict()
    # TODO finish!