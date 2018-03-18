#-------------------------------------------------------------------------------
# Name:        string, bytes, and character encoding?
# Purpose:     languages.txt decode utf-8, encode utf-8
#
# Author:      lhotse
#
# Created:     17/03/2018
# Copyright:   (c) lhotse 2018
# Licence:
#-------------------------------------------------------------------------------


import sys

script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


# utf-8 decode and encode
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)
    print(raw_bytes, "<==>", cooked_string)


languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)

