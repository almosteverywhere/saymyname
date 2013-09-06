#!/usr/bin/python
import re, sys
from extract_links import *

if __name__ == '__main__':
    if sys.argv[1:]:
        name = sys.argv[1]
        dict = count_em_up(name)
        big_dict_stats(dict, dict['num_songs'])

    else:
        # f = open("results.txt", "w")
        results = get_all_artists()
        for key in results.keys():
            if key != "num_songs":
                dict = results[key]
                print "----------------------------------"
                print "Total for " + key + " over " + str(dict['num_songs']) + " songs:"
                big_dict_stats(dict, dict['num_songs'])
                print "\n\n\n"
