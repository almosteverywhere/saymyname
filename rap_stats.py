#!/usr/bin/python

from bs4 import BeautifulSoup
from collections import Counter
import re, os, sys

# where we downloaded the files to 
basedir = "/Users/julielavoie/PycharmProjects/saymyname/files/"
default_artist = "Kanye-west"
default_dir = basedir + default_artist
# yeah, excuse my language, but that's what the proj is about 
bad_words = ['bitch','ho']

# Given an artist name, return a list of all song files
# files are organized as files/artist-name/{song1,song2}...
# GOOD
# IS THIS CALLED ANYWHERE????
def get_song_list(artist_name=default_artist):
    allfiles = []
    dir = basedir + artist_name
    filenames = os.listdir(dir)
    for f in filenames:
        ##### FIXME THIS STUFFFFFFFFF
        #### # remove .git from dir. 
            if re.search( '\.git', f):
                continue
            else:
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
def make_lyrics_dict(lyrics, bad_words=bad_words):
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

# do all the artists and put in a big dictionary
# should be call count_for_all_artists
def make_big_dict(dir=basedir, testing=False):
    results = {}
    artists = os.listdir(dir)
    if testing:
        for artist in artists[:4]:
            if re.search('\.git', artist):
                continue
            print "Artist " + artist
            results[artist] = make_artist_dict(artist)    
    else: 
        for artist in artists:
            if re.search('\.git', artist):
                continue
            print "Artist " + artist
            results[artist] = make_artist_dict(artist)
    return results

# instead we could have count_em_up return a dict of the songs with the titles
# count for one_artist
def make_artist_dict(artist, bad_words=bad_words):
    # start with empty dictionary

    artist_dict = {}
    
    # get the list of all songs for artist, one song per file
    file_list = get_song_list(artist)
    # num_songs = len(file_list)
    for f in file_list:
        
        lyrics = get_lyrics_string(f)
        song_name = os.path.basename(f)
        # this still returns: 
        # 'Kanye-west-cant-tell-me-nothing-roc-remix-lyrics.html'
        # what we want is count words to return a dictionary 
        artist_dict[song_name] = Counter(make_lyrics_dict(lyrics))
    return artist_dict

# given an dict with all the counts for the artists, calculate a bunch of stats 
# and return a dict with the stats?
# allright this is some magic shit let it be:
# sorted_page_sequence_list = sorted(page_sequence_dict.items(), key=itemgetter(1), reverse=True)
def make_stats(dict):
    # ok, let's make a dict of results
    results = {}

    # there must be a better way to do this! 
    for artist in dict.keys():
        
        num_songs = len(dict[artist])
        # DEBUG
        if num_songs == 0:
            print "artist has no songs:" + artist
            continue
        results[artist] = {}
        for word in bad_words:
            word_total = word + "_total"
            word_avg = word + "_avg" 
            count = 0 
            for song in dict[artist].keys():
                count += dict[artist][song][word]
            results[artist][word_avg] = "%.2f" % (float(count) / float(num_songs))
            results[artist][word_total] = count
            # average = "%.2f" % average
        results[artist]["num_songs"] = num_songs
    return results    

# get the results dict, print out the stats to a file
def print_stats(results, results_file="results.txt"):
    f = open(results_file, "w")
    for artist in results.keys():
        f.write("Artist: %s\n" % artist)
        for key in results[artist].keys():
            f.write(key +" " + str(results[artist][key]) + " \n")
        f.write("\n\n")   
    f.close()

# key tells us what to sort on
def get_sorted_stats(results, mykey):
    # f = open("results_sorted.txt", "w")
    sorted_stats = sorted(results.items(), key=lambda x: x[1][mykey], reverse=True)
    return sorted_stats

# should be a better way to do this, it's just once the stats are sorted
# they are put into a list instead of a dict
def print_sorted_stats(results, mykey, results_file="results.txt"): 
    f = open(results_file, "w")
    myresults = get_sorted_stats(results, mykey)
    for artist in myresults:
        # artist[0] is the name
        f.write("Artist: %s\n" % artist[0])
        # print the one we care about the most first
        f.write(mykey + " " + str(artist[1][mykey]) + " \n")
        for key in artist[1].keys():
            if key != mykey:
                f.write(key + " " + str(artist[1][key]) + " \n") 
        f.write("\n\n")   
    f.close()


# def calculate_average(dict, bad_word):
#     total_words = 0
#     total_songs = 0
#     for i in dict.keys():
#             total_words += dict[i][bad_word]
#             total_songs += dict[i]['num_songs']
#     average = float(total_words)/ float(total_songs)
#     return (average, total_words, total_songs)

# def sliced_average(dict, bad_word, keys=()):
#     total_words = 0
#     total_songs = 0
#     for i in keys:
#             total_words += dict[i][bad_word]
#             total_songs += dict[i]['num_songs']
#     average = float(total_words)/ float(total_songs)
#     return (average, total_words, total_songs)



# def big_dict_stats(dict, num_songs):
#     print_dict(dict)

#     for word in dict:
#         average = float(dict[word]) / float(num_songs)
#         average = "%.2f" % average
#         print word + " is used on average " + str(average) + " times per song."


if __name__ == '__main__':
    # we can do the stats for just one artist 
    if sys.argv[1:]:
        name = sys.argv[1]
        dict = make_artist_dict(name)
        make_stats(dict)

    else:
        results = make_big_dict()
        stats = make_stats(results) 
        print_sorted_stats(stats, 'bitch_avg')    