import sys
from collections import Counter
from string import punctuation


def load_data(filepath):
    with open(filepath, 'r', encoding="utf-8") as the_file:
        return the_file.read()


def get_clean_words(txt_data):
    text = txt_data
    all_punctuation = punctuation + "—–«»…\n"
    for symbol in range(len(all_punctuation)):
        text = text.replace(all_punctuation[symbol], "")

    words = text.casefold().split(" ")

    words_not_empty = [word for word in words if word != '']

    return words_not_empty


def get_most_frequent_words(text, number_of_words):
    words = get_clean_words(text)
    most_frequent_words = []

    words_selection = Counter(words).most_common(number_of_words)

    for word in words_selection:
        most_frequent_words.append(word)

    return most_frequent_words


if __name__ == '__main__':

    if len(sys.argv) == 1:
        sys.exit('{} <filename>'.format(sys.argv[0]))

    filepath = sys.argv[1]
    text_input = load_data(filepath)

    selection_number = 10
    most_frequent_words = get_most_frequent_words(text_input, selection_number)

    print("Top frequent words:")
    for next_word, quantity in most_frequent_words:
        print('{} - {}'.format(next_word, quantity))
