__author__ = 'bradleyt79'

import parser_classes as p

def parse(text):
    # for now, separate text into one paragraph and multiple sentences
    p1 = p.Paragraph(text)
    p1.print()