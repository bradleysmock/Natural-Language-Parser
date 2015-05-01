__author__ = 'bradleyt79'

# Future expansion notes:
# Needs a way to expand the dictionary while running the program.


# Simply returns the type of the word given it.
def wordtype(word):
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
    ('Dr', 'Adj'),
    ('John', 'N'),
    ('said', 'V'),
    ('Mr', 'Adj'),
    ('Mrs', 'Adj'),
    ('Kim', 'N'),
    ('gave', 'V'),
    ('is', 'V'),
    ('eating', 'V'),
    ('delicious', 'Adj'),
    ('hotdog', 'N'),
    ('genius', 'N')
}