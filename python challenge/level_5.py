import pickle
import urllib
import re

def find_out_words_level5(url):
#    object = urllib.urlopen(url)
#get all content of url page
#    print content
#    f = open("test.txt","r+")

    content1 = pickle.loads(content)
    print content1

    object = pickle.load(urllib.urlopen(url))   #return file descriptor
    print object

    for item in object:
        print "".join(map(lambda p: p[0]*p[1], item))  #pthhon: p[0]*p[1]£º print the character


find_out_words_level5('http://www.pythonchallenge.com/pc/def/banner.p')