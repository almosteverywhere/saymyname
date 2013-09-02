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
        # url_list.append(base_url + i['href'])
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
    # now we can strip out the \n
    # and split on the space



    # need a way to get the text and the link text
    #
    # # extract the link text
    # # to run regex
    # # soup returns a tag object but regex needs a string
    # for i in lyrics_mess:
    #     lyrics_string = lyrics_string + " " + str(i)
    # # here we have all the link text
    # contents = re.findall('<a .*>(.*)</a>', lyrics_string)

    # we don't care about the order, because all we're doing is counting
    # the occurences of a word

    # links = lyrics[0].findAll('a')
    # also gives you all links what all the stuff, and the a href contents as well

    # now we need the stuff outside the links
    # performance on this thing will be terrible, but let's worry about that later

    # for i in lyrics:
    # string_lyrics = string_lyrics + " " + i

generate_song_urls(link)
