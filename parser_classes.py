__author__ = 'bradleyt79'

import grammar
import string
import lexical


class Text:
    """group of paragraphs"""

    def __init__(self):
        self.paragraphs = []

    def add(self, paragraph):
        self.paragraphs.append(paragraph)

    def paragraph_count(self):
        return len(self.paragraphs)

    def sentence_count(self):
        return sum(x.sentence_count() for x in self.paragraphs)

    def word_count(self):
        return sum(x.word_count() for x in self.paragraphs)

    # Returns a string including all words and punctuation in the Text
    def string(self):
        return " ".join(x.string() for x in self.paragraphs)

    # Returns a string detailing the structure of the sentences in the Text
    def filled_structure_string(self):
        return " ".join(paragraph.filled_structure_string() for paragraph in self.paragraphs)

    def print(self):
        print(self.string())

    def print_filled_structure(self):
        print(self.filled_structure_string())

    def get_stats(self):
        return "\n\n".join(["Text Stats:",
                          "\tParagraphs: {}".format(self.paragraph_count()),
                          "\tSentences: {}".format(self.sentence_count()),
                          "\tWords: {}".format(self.word_count()),
                          lexical.get_stats(self.string().split())])

    def print_stats(self):
        print(self.get_stats())


class Paragraph:
    """group of sentences"""

    def __init__(self):
        self.sentences = []

    def add(self, sentence):
        self.sentences.append(sentence)

    def sentence_count(self):
        return len(self.sentences)

    def word_count(self):
        return sum(x.word_count() for x in self.sentences)

    # Returns a string including all words and punctuation in the Paragraph
    def string(self):
        return " ".join(sentence.string() for sentence in self.sentences)

    def structure_string(self):
        return " ".join(sentence.structure_string() for sentence in self.sentences)

    def filled_structure_string(self):
        return " ".join(sentence.filled_structure_string() for sentence in self.sentences)

    def print(self):
        print(self.string())

    def print_filled_structure(self):
        print(self.filled_structure_string())

    def print_stats(self):
        print("\nParagraph Stats:")
        print("\tSentences: {}".format(self.sentence_count()))
        print("\tWords: {}".format(self.word_count()))
        print(lexical.get_stats(self.string().split()))


class Sentence:
    """basic unit of written language"""

    def __init__(self):
        self.clauses = []

    def add(self, clause):
        return self.clauses.append(clause)

    def build_from_clauses(self, clause_list):
        for clause in clause_list:
            if type(clause) is Clause:
                # assumes the clause is complete
                self.add(clause)
            else:
                # convert to Clause(s)
                self.build(clause)

    # converts a list of tokens to one or more Clauses
    def build(self, tokens):
        c = Clause()
        total = len(tokens)
        remaining = len(tokens)
        strikes = 0
        while remaining > 0 and strikes < 2:
            # Add token to clause
            success = c.add(tokens[total - remaining])
            if success is True:
                remaining -= 1
                strikes = 0
                if remaining == 0:
                    # future version: revise this because it's clumsy but works
                    # add partial final phrase if any
                    c.add_final()
                    self.clauses.append(c)
            elif success is False:
                # Clause is full, so add to self.clauses and start new clause
                self.clauses.append(c)
                c = Clause()
                # print("\tCreating new clause: {}".format(c))
                strikes += 1
            else:
                print("Error in S.build with {}".format(tokens[total-remaining]))
                break

    def word_count(self):
        return sum(x.word_count() for x in self.clauses)

    # Returns a string including all words and punctuation in the Sentence
    def string(self):
        return " ".join(clause.string() for clause in self.clauses)

    def clause_strings(self):
        return [clause.string() for clause in self.clauses]

    def structure_string(self):
        return " ".join([x.structure_string() for x in self.clauses])

    def filled_structure_string(self):
        return " ".join([clause.filled_structure_string() for clause in self.clauses])

    def structure(self):
        return [x.structure() for x in self.clauses]

    def filled_structure(self):
        return [x.filled_structure() for x in self.clauses]

    def print(self):
        print(self.string())

    def print_stats(self):
        print("Sentence Stats:")
        print("Words: {}".format(self.word_count()))


class Clause:
    """sub-unit of a sentence"""

    def __init__(self):
        # Parts are what are actually in the Clause
        self.parts = []
        self.num_words = 0
        # Define possible Clause structure from grammar
        self.model_structure = grammar.C().value
        self.final_phrase = ""

    # Adds a single token to the clause. Returns True if successful, False if the clause if full, and None if error.
    def add(self, token):
        # add punctuation
        if token in string.punctuation:
            if not self.final_phrase.is_empty:
                self.parts.append(self.final_phrase)
                self.final_phrase = ""

            self.parts.append(token)
            return True
        # add word
        else:
            # add token to phrase within clause
            for phrase in self.model_structure:
                # TODO add_to_phrase doesn't handle PP correctly
                if grammar.add_to_phrase(token, phrase) is None:
                    # add failed -- look in next phrase
                    self.model_structure = self.model_structure[1:]
                    # if phrase is not empty add to clause parts
                    if not phrase.is_empty:
                        self.parts.append(phrase)
                        self.final_phrase = ""

                else:
                    # add successful!
                    phrase.is_empty = False
                    self.num_words += 1
                    self.final_phrase = phrase
                    return True

            if self.model_structure == grammar.empty_C:
                # clause is full
                return False

            return None

    def add_final(self):
        if self.final_phrase != '':
            self.parts.append(self.final_phrase)

    def word_count(self):
        return self.num_words

    # Returns a string including all words and punctuation in the Clause
    def string(self):
        string_list = []
        for x in self.parts:
            if type(x) is str:
                string_list.append(x.strip())
            else:
                string_list.append(x.string().strip())

        return " ".join(string_list)

    # Returns a string detailing the structure of the Clause
    def structure_string(self):
        return " ".join(self.structure())

    # Returns a string detailing the structure and words of the Clause
    def filled_structure_string(self):
        return str(self.filled_structure())

    def structure(self):
        parts_list = []
        for part in self.parts:
            if type(part) is str:
                parts_list.append(part)
            else:
                parts_list.append(part.type)

        return parts_list

    def filled_structure(self):
        parts_list = []
        for part in self.parts:
            if type(part) is str:
                parts_list.append(part)
            else:
                parts_list.append((part.type, part.string()))

        return parts_list

    def print(self):
        print(self.string())

    def print_structure(self):
        print(self.structure())

    def print_filled_structure(self):
        print(self.filled_structure())

    def print_stats(self):
        print("Clause Stats:")
        print("\tWords: {}".format(self.word_count()))
        print("\tStructure: {}".format(self.structure()))


# Parser Class Tests
def run_tests():
    sentences = [
        ['The', 'man', 'in', 'the', 'mask', 'screamed', '.'],
        ['The', 'woman', 'laughed', '.'],
        ['The', 'boy', 'cried', '.'],
        ['The', 'girl', 'in', 'the', 'petticoat', 'smiled', '.'],
        ['The', 'dog', 'with', 'a', 'bone', 'whined', '.'],
        ['The', 'cat', 'mewed', '.'],
        ['Dr', 'John', 'said', 'hello', '.'],
        ['Mr', 'Kim', 'gave', 'Mrs', 'Kim', 'a', 'gift', '.']
    ]

    t = Text()
    p = Paragraph()
    for sentence in sentences:
        s = Sentence()
        s.build(sentence)
        for clause in s.clauses:
            clause.print()
            clause.print_structure()
            clause.print_filled_structure()
            clause.print_stats()
        print("\nSentence: {}".format(s.string()))
        print("\tStructure: {}".format(s.structure_string()))
        print("\tStructure Filled: {}".format(s.filled_structure_string()))
        s.print_stats()
        p.add(s)

    print("\nParagraph:\n{}".format(p.string()))
    p.print_stats()

    t.add(p)
    print("\nText:\n{}".format(t.string()))
    t.print_stats()


# run_tests()