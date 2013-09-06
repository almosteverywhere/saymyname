#!/usr/bin/python
import sys
from extract_links import *

import re


# stuff = "bitch, whatever, some stuff, bitches, bitch, nigga, niggas, what's up my nigga"
# read_words(stuff)

if __name__ == '__main__':
    if sys.argv[1:]:
        name = sys.argv[1]
        dict = reckoning(name)
        big_dict_stats(dict, dict['num_songs'])

    else: # f = open("results.txt", "w")
        results = get_results()
        for key in results.keys():
            if key != "num_songs":
                dict = results[key]
                print "----------------------------------"
                print "Total for " + key + " over " + str(dict['num_songs']) + " songs:"
                big_dict_stats(dict, dict['num_songs'])
                print "\n\n\n"
# take stuff from command-line arguments to make it easier to test

# text = parse_text("http://rapgenius.com/A-ap-rocky-fuckin-problems-lyrics")
# mydict = read_words(text)
# print_dict(mydict)
