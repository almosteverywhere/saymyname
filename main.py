#!/usr/bin/python
import re
import lxml.html
mdict = {}
# bad words no one shoudl say, but there you go
# bad_words = ['bitch', 'nigga' ]

# given some text, match the occurences of bitch, and n-word
def read_words(stuff, bad_words=['bitch', 'nigga']):

    for word in bad_words:

        # matches = re.findall('bitch', stuff)
        matches = re.findall(word, stuff)
        print "you have " + str(len(matches)) + " " + word + " up in here"
        # print "you have " + str(len(matches)) + " bitches up in here"
        # mydict['bitches'] = len(matches)

        mydict[word] = len(matches)




# # Open file
#   f = open('test.txt', 'r')
#   # Feed the file text into findall(); it returns a list of all the found strings
#
# trings = re.findall(r'some pattern', f.read())

stuff = "bitch, whatever, some stuff, bitches, bitch, nigga, niggas, what's up my nigga"
read_words(stuff)