__author__ = 'bradleyt79'


def word_frequency(word, word_list):
    return sum([1 for x in word_list if x == word])


def word_frequency_string(word, word_list):
    return "{} - '{}'".format(word_frequency(word, word_list), word)


def word_percentage(word, word_list):
    return word_frequency(word, word_list) / len(word_list)


def word_percentage_string(word, word_list, places):
    return "{:.{places}%} '{}'".format(word_percentage(word, word_list), word, places=places)


def word_diversity(word_list):
    return len(set(word_list)) / len(word_list)


def word_diversity_string(word_list, places):
    return "{:.{places}%} unique".format(word_diversity(word_list), places=places)


def most_common(word_list, number, stats):
    if stats == 3:  # frequency and percentage
        output_list = [[word_frequency(word, word_list),
                       word_percentage(word, word_list),
                       word] for word in set(word_list)]
    elif stats == 2:  # percentage only
        output_list = [[word_percentage(word, word_list),
                       word] for word in set(word_list)]
    else:  # stats == 1  frequency only
        output_list = [[word_frequency(word, word_list),
                       word] for word in set(word_list)]
    if number > len(word_list):
        return sorted(output_list, reverse=True)
    else:
        return sorted(output_list[:number], reverse=True)


def most_common_string(word_list, number, stats):
    if stats == 3:  # frequency and percentage
        output = ["{:4} - {:7.2%} : {}".format(word[0], word[1], word[2])
                  for word in most_common(word_list, number, stats)]
    elif stats == 2:  # percentage only
        output = ["{:7.2%} : {}".format(word[0], word[1]) for word in most_common(word_list, number, stats)]
    else:  # stats == 1  frequency only
        output = ["{:4} : {}".format(word[0], word[1]) for word in most_common(word_list, number, stats)]

    return "\n".join(output)


def get_stats(word_list):
    return "\n".join(["Lexical Report",
                      "Number of Words: {}".format(len(word_list)),
                      "Word Diversity: {}".format(word_diversity_string(word_list, 2)),
                      "Most Common Words:\n{}".format(most_common_string(word_list, 10, 3))])


# Lexical Tests
def run_tests():
    from samples import tokens1
    tokens = tokens1
    word = "the"
    # print(word_frequency(word, tokens))
    print(word_frequency_string(word, tokens))
    # print(word_percentage(word, tokens))
    print(word_percentage_string(word, tokens, 2))
    # print(word_diversity(tokens))
    print(word_diversity_string(tokens, 2))
    print(most_common(tokens, 10, 3))
    print(get_stats(tokens))

# run_tests()