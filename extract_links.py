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

