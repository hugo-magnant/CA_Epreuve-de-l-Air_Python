import sys
import unicodedata
import re

def filter_strings(array, string):
    normalized_string = unicodedata.normalize('NFD', string).lower()
    normalized_string = re.sub(r'\W+', '', normalized_string)

    def match(word):
        normalized_word = unicodedata.normalize('NFD', word).lower()
        normalized_word = re.sub(r'\W+', '', normalized_word)
        return normalized_string in normalized_word

    return list(filter(match, array))

if len(sys.argv) < 3:
    print("error")
    sys.exit(1)

string_to_match = sys.argv[-1]
words = sys.argv[1:-1]

if filtered_words := filter_strings(words, string_to_match):
    print(", ".join(filtered_words))
else:
    print("")
