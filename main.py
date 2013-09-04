#!/usr/bin/python
import sys
from extract_links import *

import re


# stuff = "bitch, whatever, some stuff, bitches, bitch, nigga, niggas, what's up my nigga"
# read_words(stuff)

if __name__ == '__main__':
    if sys.argv[1:]:
        url = sys.argv[1]
        # print url
        reckoning(url)
# take stuff from command-line arguments to make it easier to test

# text = parse_text("http://rapgenius.com/A-ap-rocky-fuckin-problems-lyrics")
# mydict = read_words(text)
# print_dict(mydict)
