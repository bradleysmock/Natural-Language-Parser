__author__ = 'bradleyt79'

#Note
# Five English phrase types taken from Dictionary of English Grammar by Leech et al.
# Noun Phrase ​​​(det) + (modifier) + noun + (modifier)
# Verb Phrase ​​​(auxiliary) + verb
# Prepositional Phrase​​ preposition + noun phrase
# Adjective Phrase​​ (modifier) + adjective + (modifier)
# Adverb Phrase​​ (modifier) + adverb + (modifier)
#
# Clause​​​​ (conjunction) + (adverbial) + noun phrase + verb phrase + (indirect object) + (direct object) + (complement) + (adverbial)

# Grammar Constituents
S = ("S", "Sentence")
C = ("C", "Clause")
NP = ("NP", "Noun Phrase")
VP = ("VP", "Verb Phrase")
PP = ("PP", "Prepositional Phrase")
AdjP = ("AdjP", "Adjective Phrase")
AdvP = ("AdvP", "Adverb Phrase")
DO = ("DO", "Direct Object")
IO = ("IO", "Indirect Object")
Mod = ("Mod", "Modifier")
N = ("N", "Noun")
V = ("V", "Verb")
Adj = ("Adj", "Adjective")
Adv = ("Adv", "Adverb")
PN = ("PN", "Pronoun")
Prep = ("Prep", "Preposition")
Conj = ("Conj", "Conjunction")
Aux = ("Aux", "Auxiliary")
Det = ("Det", "Determiner")
Empty = ("Empty", "")
end = ("end", "")

# Grammar Patterns
patterns = {
    # Sentence Level
    S: [],  # Really a clause list
    C: (Conj, AdvP, NP, VP, IO, DO, AdvP),  # TODO Add Complement
    # Non-terminal Phrases
    NP: (Det, Mod, N, Mod),
    VP: (Aux, V),
    PP: (Prep, NP),
    AdjP: (Mod, Adj, Mod),
    AdvP: (Mod, Adv, Mod),
    DO: (NP),
    IO: (PP),
    # Non-terminal Modifiers
    Mod: (AdjP),  # TODO How to handle these?
    #Mod: (AdvP),
    # Terminal forms
    N: (end),
    V: (end),
    Prep: (end),
    Adj: (end),
    Adv: (end),
    Det: (end),
    Aux: (end),
    # Empty
    Empty: (end)
}