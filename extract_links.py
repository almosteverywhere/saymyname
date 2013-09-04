#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup
import re
from decimal import Decimal

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
def get_lyrics(song_url):
    page = urllib2.urlopen(song_url).read()
    soup = BeautifulSoup(page)
    soup.prettify()
    # this gets the lyrics, but a lot of it is link text and is a huge mess
    lyrics = soup.select(".lyrics")
    lyrics_string = lyrics[0].text
    lyrics_string = re.sub("\n", " ", lyrics_string)

    return lyrics_string

# given an artist page with a bunch of links, return urls
def get_song_urls(url="http://rapgenius.com/artists/A-ap-rocky"):
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

# given an ajax url, in the files directory, get the list of all songs
# by that artist, and save the lyrics for all the songs in
# ./artist/song so we can do data analysis at our leisure
# given an artist page with a bunch of links, return urls
# enormous asap rocky url=http://rapgenius.com/songs?for_artist_page=12417&id=A-ap-rocky&lyrics_seo=false&page=1&pagination=false&search[by_artist]=12417&search[unexplained_songs_last]=titlelis
# for a given artist, gives us the first 10 pages of song urls
def get_song_urls_defeat_ajax(base_url):

    all_urls = []

    artist_url1 = "http://rapgenius.com/songs?for_artist_page=12417&id=A-ap-rocky&lyrics_seo=false&page="
    num = 1
    artist_url2 = "&pagination=false&search[by_artist]=12417&search[unexplained_songs_last]=title"
    # we ignore past 10 pages

    for i in range(1,10):
        all_urls.append(artist_url1 + str(i) + artist_url2)

    urls = []
    list = []

    # ok, now this is super ghetto, we look at each of these pages, and check
    # check when ul.song_list is empty.
    for url in all_urls[8:]:
        page = urllib2.urlopen(url).read()
        soup = BeautifulSoup(page)
        soup.prettify()
        # in the ajax version, songs come in groups of 20 there
        # are many ul.song_list in a page, with a group of 20 songs
        # ok this is disgusting, but this is how we're going to cycle through the list
        # of songs.
        songlist = soup.select("ul.song_list a")
        for link in songlist:
            urls.append(base_url + link['href'])
    return urls



# bad words no one shoudl say, but there you go
# bad_words = ['bitch', 'nigga' ]

# given some text, match the occurences of bitch, and n-word
def count_words(lyrics, bad_words=['bitch', 'nigga']):
    mydict = {}

    for word in bad_words:

        # matches = re.findall('bitch', stuff)
        matches = re.findall(word, lyrics)
        # print "you have " + str(len(matches)) + " " + word + " up in here"
        # print "you have " + str(len(matches)) + " bitches up in here"
        # mydict['bitches'] = len(matches)

        mydict[word] = len(matches)

    # return a word count as well
    words = lyrics.split()
    num_words = len(words)
    mydict['num_words'] = num_words

    print_dict(mydict)
    return mydict

def print_dict(dict):
    for key in dict.keys():
        print str(key) + " : " + str(dict[key]) + "\n"

# given an artist, give the total count of bad words for all songs
# for right now it only counts the first page of songs
def reckoning(artist_url="http://rapgenius.com/artists/A-ap-rocky", bad_words=['bitch', 'nigga']):

# ok this is super ghetto, better to get each iteration to edit the same dict
    big_dict = {}
    big_dict['bitch'] = 0
    big_dict['nigga'] = 0
    big_dict['num_words'] = 0

# get the list of urls:
    url_list = get_song_urls(artist_url)
    num_songs = len(url_list)
    # for u in url_list:
    #     print u
    for u in url_list:
        print "song: " + u
        lyrics = get_lyrics(u)
        small_dict = count_words(lyrics)
        big_dict['bitch'] += (0 or small_dict['bitch'])
        big_dict['nigga'] += (0 or small_dict['nigga'])
        big_dict['num_words'] += (0 or small_dict['num_words'])
        # print "now we have " + str(big_dict['bitch']) + " bitches"
        # print "now we have " + str(big_dict['nigga']) + " niggas"
        small_dict = {}

    print "Total for " + artist_url
    big_dict_stats(big_dict, num_songs)

def big_dict_stats(dict, num_songs):
    print_dict(dict)
    p_b = Decimal(dict['bitch']) / Decimal(num_songs)
    p_n = Decimal(dict['nigga']) / Decimal(num_songs)
    print "B-word is used on average" + str(p_b) + " times per song"
    print "n-word is used on average" + str(p_n) + " times per song"

# stats we want:
# per total words
# so far asap rocky:
# nigga : 133
#
# bitch : 78

# Total for http://rapgenius.com/artists/A-ap-rocky
# nigga : 133
#
# bitch : 78
#
# num_words : 11091
#
# B-word is used 0.007032729239924262915877738707
# n-word is used 0.01199170498602470471553511856

# need some kind of memoisation or store the results in a db of some kind
# more signicant is per number of songs
# or how many times per song


# Total for http://rapgenius.com/artists/Lil-wayne
# nigga : 131
#
# bitch : 80
#
# num_words : 12017
#
# B-word is used 4per song
# n-word is used 6.55per song
#
# Total for http://rapgenius.com/artists/Jay-z
# nigga : 133
#
# bitch : 24
#
# num_words : 12461
#
# B-word is used on average1.2 times per song
# n-word is used on average6.65 times per song

# Total for http://rapgenius.com/artists/A-ap-rocky
# nigga : 133
#
# bitch : 78
#
# num_words : 11091
#
# B-word is used on average3.9 times per song
# n-word is used on average6.65 times per song