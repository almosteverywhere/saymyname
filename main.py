#!/usr/bin/python
from extract_links import *
import re

# bad words no one shoudl say, but there you go
# bad_words = ['bitch', 'nigga' ]

# given some text, match the occurences of bitch, and n-word
def read_words(stuff, bad_words=['bitch', 'nigga']):
    mydict = {}

    for word in bad_words:

        # matches = re.findall('bitch', stuff)
        matches = re.findall(word, stuff)
        # print "you have " + str(len(matches)) + " " + word + " up in here"
        # print "you have " + str(len(matches)) + " bitches up in here"
        # mydict['bitches'] = len(matches)

        mydict[word] = len(matches)

    return mydict

def print_dict(dict):
    for key in dict.keys():
        print str(key) + " : " + str(dict[key]) + "\n"

# stuff = "bitch, whatever, some stuff, bitches, bitch, nigga, niggas, what's up my nigga"
# read_words(stuff)

text = parse_text("http://rapgenius.com/A-ap-rocky-fuckin-problems-lyrics")
mydict = read_words(text)
print_dict(mydict)
