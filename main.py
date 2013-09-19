#!/usr/bin/python
import re, sys
from operator import itemgetter
from rap_stats import *


if __name__ == '__main__':
    if sys.argv[1:]:
        name = sys.argv[1]
        dict = count_em_up(name)
        big_dict_stats(dict, dict['num_songs'])

    else:
        # f = open("results.txt", "w")
        results = get_all_artists()
# sorted_results = sorted(results.items(),key=lambda x: (x[1]['bitch']/ x[1]['num_songs']),reverse=True)
        # print str(i) + "average:" + str(float(i[1]['bitch']) / float(i[1]['num_songs']))

        # sorted_resuls = sorted()
        # 
  # sorted_page_sequence_list = sorted(page_sequence_dict.items(), key=itemgetter(1), reverse=True)
  # holy duck this works:
  # sorted_results = sorted(results.items(),key=lambda x: x[1]['bitch'],reverse=True)
        # ok, we should be able to sort on how many times they use bitch

        for key in results.keys():
            if key != "num_songs":
                dict = results[key]
                print "----------------------------------"
                print "Total for " + key + " over " + str(dict['num_songs']) + " songs:"
                big_dict_stats(dict, dict['num_songs'])
                print "\n\n\n"
