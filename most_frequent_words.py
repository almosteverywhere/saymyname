#!/usr/bin/python

from rap_stats import *
from collections import Counter
import re

# stop_words = "a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your"

# stop_words = re.split("," stop_words)

stop_file = "stop_words2.txt"

stop_words = []

def get_stop_words(file):

	f = open(file, "r")
	for word in f.readlines():
		stop_words.append(word.strip())
	return stop_words


# pass in a list of artists, return a counter of most used words,
# so can be used for just one
# all update a big global dict, probably a better way to do this
def count_words_for_all_artists(artists_list):
	count = Counter()
	for artist in artists_list:
		# annoying git directory
		print "Artist:" + artist
		if re.search('\.git', artist):
			continue

		artist_count = count_all_words_for_one_artist(artist)
		if artist_count:
			count += artist_count
	return count

def count_all_words_for_one_artist(artist):
	count = Counter()
	song_list = make_song_list(artist)
	for song in song_list:
		lyrics = scrape_lyrics_from_song(song)
		words = re.findall(r'\w+', lyrics.lower())
		count.update(words)
	return count

def make_artists_list(dir=basedir):
	results = {}
	artists = os.listdir(dir)
	return artists

if __name__ == '__main__':
	artists = make_artists_list()
	big_count = count_words_for_all_artists(artists)
	print big_count.most_common(100)
    