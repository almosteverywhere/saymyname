#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup
import re

base_url = "http://rapgenius.com"
link = "http://rapgenius.com/artists/A-ap-rocky"

# given the artist's url, return the list of song urls
def generate_song_urls(artist_url):

    song_urls = []

    page = urllib2.urlopen(link).read()
    soup = BeautifulSoup(page)
    soup.prettify()
    mylist = soup.select("ul.song_list a")

    # ok super ghetto must be faster
    for i in mylist:
        song_urls.append(base_url + i['href'])

    for url in song_urls[:2]:
        print url
    print "returning list of urls"
    return song_urls[:2]

# given a song url, return the lyrics as a string
def parse_text(song_url):
    page = urllib2.urlopen(song_url).read()
    soup = BeautifulSoup(page)
    soup.prettify()
    # this gets the lyrics, but a lot of it is link text and is a huge mess
    lyrics = soup.select(".lyrics")
    lyrics_string = lyrics[0].text
    lyrics_string = re.sub("\n", " ", lyrics_string)

    return lyrics_string

# given an artist page with a bunch of links, return urls
def parse_link_page(url="http://rapgenius.com/artists/A-ap-rocky"):
    urls = []
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page)
    soup.prettify()
    songlist = soup.select("ul.song_list")
    # gives you all links in the first page of all songs
    list = songlist[1].select("a")
    for i in list:
        urls.append(base_url + i['href'])

    return urls
    # oh crap, it does a scroll down thing to load more song titles
    # ok, let's do the first page as a sample, and then we can figure out
    # what to do for pagination, we can use net console to figure out
    # what url the ajax is requesting to

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



parse_link_page()