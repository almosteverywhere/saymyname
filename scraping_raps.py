#!/usr/bin/python

from bs4 import BeautifulSoup
import re
import os

basedir = "/Users/julielavoie/PycharmProjects/saymyname/files/"
# link = "http://rapgenius.com/artists/A-ap-rocky"
# file = basedir + "Dead-prez/Dead-prez-the-hood-lyrics.html"
default_artist = "Kanye-west"
default_dir = basedir + default_artist
# bad_words=['bitch', 'nigga', 'fuck', 'pussy']
bad_words = ['bitch', 'dick', 'nigga']

# Given an artist name, return a list of all song files
# files are organized as files/artist-name/{song1,song2}...
def get_song_list(artist_name=default_artist):
    allfiles = []
    dir = basedir + artist_name
    filenames = os.listdir(dir)
    for f in filenames:
            allfiles.append(os.path.join(dir,f))
    return allfiles

# given a file containing one song, return the lyrics as a string
def get_lyrics_string(file):
    f = open(file, 'r')
    page = f.read()
    # using beautiful soup to navigate the dom and get
    # back the stuff that we need
    soup = BeautifulSoup(page)
    soup.prettify()
    lyrics = soup.select(".lyrics")
    if lyrics:
        lyrics_string = lyrics[0].text
        lyrics_string = re.sub("\n", " ", lyrics_string)
        return lyrics_string
    else:
        return ""

# given lyrics and a dict of bad words, count the occurrences
# of each bad word and return a dictionary of results
def count_words(lyrics, bad_words=bad_words):
    mydict = {}

    for word in bad_words:
        if word == 'ho':
            matches = re.findall(r'\bho\b', lyrics, re.IGNORECASE)
        else:
            matches = re.findall(word, lyrics, re.IGNORECASE)
        mydict[word] = len(matches) or 0
    # why are we doing this?
    print_dict(mydict)
    return mydict

def print_dict(dict):
    for key in dict.keys():
        print str(key) + " : " + str(dict[key]) + "\n"

# given an artist, give the total count of bad words for all songs
def count_em_up(artist="Kanye-west", bad_words=bad_words):

    # FIXME: ok this is super ghetto, better to get each iteration to edit the same dict
    big_dict = {}
    for word in bad_words:
        big_dict[word] = 0

    file_list = get_song_list(artist)
    num_songs = len(file_list)
    for f in file_list:
        print "song: " + f
        lyrics = get_lyrics_string(f)
        small_dict = count_words(lyrics)

        for word in bad_words:
            big_dict[word] += (0 or small_dict[word])
        # need to reset the small dict
        small_dict = {}

    # print "Total for " + artist + " over " + str(num_songs) + " songs:"
    # big_dict_stats(big_dict, num_songs)
    big_dict['num_songs'] = num_songs
    return big_dict

# do all the artists and put in a big dictionary
def get_all_artists(dir='/Users/julielavoie/PycharmProjects/saymyname/files'):
    results = {}
    artists = os.listdir(dir)
    for artist in artists:
        print "Artist " + artist
        results[artist] = count_em_up(artist)
    return results

def big_dict_stats(dict, num_songs):
    print_dict(dict)

    for word in dict:
        average = float(dict[word]) / float(num_songs)
        average = "%.2f" % average
        print word + " is used on average " + str(average) + " times per song."

# -------

#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup
import re
import os
from decimal import Decimal

base_url = "file:///Users/julielavoie/PycharmProjects/saymyname/files"
basedir = "/Users/julielavoie/PycharmProjects/saymyname/files/"
link = "http://rapgenius.com/artists/A-ap-rocky"
file = basedir + "Dead-prez/Dead-prez-the-hood-lyrics.html"
default_artist = "Kanye-west"
default_dir = basedir + default_artist
# bad_words=['bitch', 'nigga', 'fuck', 'pussy']
bad_words = ['bitch', 'dick', 'nigga']

# Given an artist name, return a list of all song files
# for now, we'll give like Kanye-west
def get_file_list(artist_name=default_artist):
    # print "ARTIST NAME" + artist_name
    allfiles = []
    dir = basedir + artist_name
    filenames = os.listdir(dir)
    for f in filenames:
            allfiles.append(os.path.join(dir,f))
    return allfiles

# given a file containing one song, return the lyrics as a string
def get_lyrics(file):
    f = open(file, 'r')
    page = f.read()
    # page = urllib2.urlopen(song_url).read()
    soup = BeautifulSoup(page)
    soup.prettify()
    lyrics = soup.select(".lyrics")
    if lyrics:
        lyrics_string = lyrics[0].text
        lyrics_string = re.sub("\n", " ", lyrics_string)
        return lyrics_string
    else:
        return ""

# # given the artist's url, return the list of song urls
# def generate_song_urls(artist_url):
#
#     song_urls = []
#
#     page = urllib2.urlopen(link).read()
#     soup = BeautifulSoup(page)
#     soup.prettify()
#     mylist = soup.select("ul.song_list a")
#
#     # ok super ghetto must be faster
#     for i in mylist:
#         song_urls.append(base_url + i['href'])
#
#     for url in song_urls[:2]:
#         print url
#     print "returning list of urls"
#     return song_urls[:2]


# bad words no one shoudl say, but there you go
# bad_words = ['bitch', 'nigga' ]

# given some text, match the occurences of bitch, and n-word
def count_words(lyrics, bad_words=bad_words):
    mydict = {}

    for word in bad_words:
        if word == 'ho':
            matches = re.findall(r'\bho\b', lyrics, re.IGNORECASE)
        else:
            matches = re.findall(word, lyrics, re.IGNORECASE)
        mydict[word] = len(matches) or 0

    # return a word count as well
    # words = lyrics.split()
    # num_words = len(words)
    # mydict['num_words'] = num_words

    print_dict(mydict)
    return mydict

def print_dict(dict):
    for key in dict.keys():
        print str(key) + " : " + str(dict[key]) + "\n"

# given an artist, give the total count of bad words for all songs
def reckoning(artist="Kanye-west", bad_words=bad_words):

    # ok this is super ghetto, better to get each iteration to edit the same dict
    big_dict = {}
    for word in bad_words:
        big_dict[word] = 0

    file_list = get_file_list(artist)
    num_songs = len(file_list)
    # for u in url_list:
    #     print u
    for f in file_list:
        print "song: " + f
        lyrics = get_lyrics(f)
        small_dict = count_words(lyrics)

        for word in bad_words:
            # print word
            # print word
            big_dict[word] += (0 or small_dict[word])
        small_dict = {}

    # print "Total for " + artist + " over " + str(num_songs) + " songs:"
    # big_dict_stats(big_dict, num_songs)
    big_dict['num_songs'] = num_songs
    return big_dict

# do all the artist and put in a big dictionary
def get_results(dir='/Users/julielavoie/PycharmProjects/saymyname/files'):
    results = {}
    artists = os.listdir(dir)
    for artist in artists:
        print "Artist " + artist
        results[artist] = reckoning(artist)
    return results


def big_dict_stats(dict, num_songs):
    print_dict(dict)

    for word in dict:
        average = float(dict[word]) / float(num_songs)
        average = "%.2f" % average
        print word + " is used on average " + str(average) + " times per song."

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
