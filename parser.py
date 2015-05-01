__author__ = 'bradleyt79'

import parser_classes
import samples

# Global Constants
end_paragraph = ["\n", "||"]
end_sentence = [".", "?", "!"]
end_clause = [",", ":", ";", "- ", "' ", " '", '"', "(", ")"]
sub = end_sentence + end_clause
# Future expansion: abbrev list needs to be much more robust
abbrev = ["Dr.", "Mr.", "Mrs.", "etc.", "e.g.", "i.e."]


# Breaks a text (string) into tokens.
def tokenize(text):
        # Future expansion: revise for better speed and efficiency
        for x in abbrev:
            text = text.replace("{}".format(x), "{}".format(x[:-1]))

        for x in sub:
            text = text.replace("{}".format(x), " {} ".format(x))

        return text.split()


def split_by(tokens, split_list):
    return_list = []
    part = []
    for n in range(0, len(tokens)):
        token = tokens[n]
        if n == len(tokens) - 1:
            part.append(token)
            return_list.append(part)
        elif token in split_list:
            part.append(token)
            return_list.append(part)
            part = []
        else:
            part.append(token)
            
    return return_list


def split_into_sentences(tokens):
    return split_by(tokens, end_sentence)


def split_into_paragraphs(tokens):
    return split_by(tokens, end_paragraph)


# Returns a Text object from a string
def parse(text):
    new_text = parser_classes.Text()
    tokens = tokenize(text)
    paragraphs = split_into_paragraphs(tokens)
    for paragraph in paragraphs:
        new_paragraph = parser_classes.Paragraph()
        sentences = split_into_sentences(paragraph)
        for sentence in sentences:
            # remove paragraph ends
            if sentence[0] in end_paragraph:
                continue
            else:
                new_sentence = parser_classes.Sentence()
                new_sentence.build(sentence)
                new_paragraph.add(new_sentence)

        new_text.add(new_paragraph)

    return new_text


# Tests
def test_tokenize(text):
    print(tokenize(text))


def test_parse(text):
    parsing = parse(text)

    parsing.print()
    parsing.print_stats()

    pn = 1
    for p in parsing.paragraphs:
        print("\nParagraph {}".format(pn))
        p.print()
        p.print_stats()
        print("")

        sn = 1
        for s in p.sentences:
            print("Sentence {} - {}".format(sn, s.string()))
            print(s.structure_string())
            s.print_stats()
            print("")

            sn += 1

        pn += 1


def run_tests():
    test_tokenize(samples.text1)
    test_parse(samples.text1)


# run_tests()