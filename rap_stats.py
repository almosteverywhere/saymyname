#!/usr/bin/python

from bs4 import BeautifulSoup
import re, os 

# where we downloaded the files to 
basedir = "/Users/julielavoie/PycharmProjects/saymyname/files/"
default_artist = "Kanye-west"
default_dir = basedir + default_artist
# yeah, excuse my language, but that's what the proj is about 
bad_words = ['bitch','ho']

# Given an artist name, return a list of all song files
# files are organized as files/artist-name/{song1,song2}...
# GOOD
def get_song_list(artist_name=default_artist):
    allfiles = []
    dir = basedir + artist_name
    filenames = os.listdir(dir)
    for f in filenames:
            allfiles.append(os.path.join(dir,f))
    return allfiles

# given a file containing one song, return the lyrics as a string
# GOOD 
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
# RETURNS THE LYRICS FOR ONE SONGb
def count_words(lyrics, bad_words=bad_words):
    mydict = {}

    for word in bad_words:
        # we need this because b**** only really matches itself + plural
        # but hoes matches all kinds of other words 
        if word == 'ho':
            matches = re.findall(r'\bhoe?s?\b', lyrics, re.IGNORECASE)
        else:
            matches = re.findall(word, lyrics, re.IGNORECASE)
        mydict[word] = len(matches) or 0
    return mydict

def print_dict(dict):
    for key in dict.keys():
        print str(key) + " : " + str(dict[key]) + "\n"

# given an artist, give the total count of bad words for all songs
def count_em_up(artist="Kanye-west", bad_words=bad_words):
    max_song_key = ""
    max_num_key = ""

    artist_dict = {}
    for word in bad_words:
        # FIXME we should probably be using json
        # max_song_key = "max_" + word + "_song"
        # max_num_key =  "max" + word + "_num"
        artist_dict[word] = 0
        # artist_dict[max_num_key] = 0
        # artist_dict[max_song_key] = ""


    file_list = get_song_list(artist)
    num_songs = len(file_list)
    for f in file_list:
        print "song: " + f
        lyrics = get_lyrics_string(f)
        small_dict = count_words(lyrics)

        for word in bad_words:
            artist_dict[word] += (0 or small_dict[word])

        # need to reset the small dict
        small_dict = {}

    # print "Total for " + artist + " over " + str(num_songs) + " songs:"
    # big_dict_stats(big_dict, num_songs)
    artist_dict['num_songs'] = num_songs
    return artist_dict

# do all the artists and put in a big dictionary
def get_all_artists(dir=basedir):
    results = {}
    artists = os.listdir(dir)
    for artist in artists:
        print "Artist " + artist
        results[artist] = count_em_up(artist)
    return results

def calculate_average(dict, bad_word):
    total_words = 0
    total_songs = 0
    for i in dict.keys():
            total_words += dict[i][bad_word]
            total_songs += dict[i]['num_songs']
    average = float(total_words)/ float(total_songs)
    return (average, total_words, total_songs)

def slice_dict(dict, keys=[]):
    # holy fuck this is some magic ish
    # new_dict = itemgetter(*keys)(results)
    # oh, doesn't work, returns a tuple.
    return new_dict

def sliced_average(dict, bad_word, keys=()):
    total_words = 0
    total_songs = 0
    for i in keys:
            total_words += dict[i][bad_word]
            total_songs += dict[i]['num_songs']
    average = float(total_words)/ float(total_songs)
    return (average, total_words, total_songs)



def big_dict_stats(dict, num_songs):
    print_dict(dict)

    for word in dict:
        average = float(dict[word]) / float(num_songs)
        average = "%.2f" % average
        print word + " is used on average " + str(average) + " times per song."