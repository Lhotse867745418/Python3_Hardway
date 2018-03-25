#-------------------------------------------------------------------------------
# Name:        class
# Purpose:
#
# Author:      lhotse
#
# Created:     24/03/2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import random

from urllib.request import urlopen

import sys

WORD_URL = "http://learncodethehardway.org/words.txt"

WORDS = []

PHRASES = {

    "class %%%(%%%):":
        "make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef__init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object): \n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "set *** to an instance of class %%%.",
    "***.***(@@@)":
        "from *** get the *** function, call it with params self, @@@.",
    "***.***":
        "from *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first

if len(sys.argv) == 2 and sys.argv[1] =="english":

    PHRASES_FIRST =True
    print("it is true.")

else:

    PHRASES_FIRST = False
    print("it is false.")

# load up the words from the website

for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding = "utf-8"))
    print(str(word.strip()))

def convert(snippet, phrase):

    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]

    other_names = random.sample(WORDS, snippet.count("***"))

    results = []

    param_names = []

    for i in range(0, snippet.count("@@@")):

        param_count = random.randint(1,3)
        param_names.append(', ' .join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:

        result = sentence[:]

        # fake class names

        for word in class_names:
            result =result.replace("%%%", word, 1)

        # fake other names

        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists

        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

    # keep going until they hit ctrl-d
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question,answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question,answer = answer,question
                print(question)
                input('>')
                print(f"answer: {answer}\n\n")

except EOFError:
    print("\nBye")


def main():
    pass

if __name__ == '__main__':
    main()
