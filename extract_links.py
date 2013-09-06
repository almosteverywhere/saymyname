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
bad_words = ['bitch', 'dick', 'nigga', 'ho']

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
            matches = re.findall(r'\bhoe?s?\b', lyrics, re.IGNORECASE)
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
