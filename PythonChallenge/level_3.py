import urllib
import re

inchar = "abcdefghijklmnopqrstuvwxyz"
remaining = []

def find_out_words_level3(url):
    print 'enter'
    doclocation = urllib.urlopen(url)
    openfile = doclocation.read()
    characters = openfile.split('<!--')[1]
    pattern = '[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]'
    m = re.findall(pattern, characters)
    print m
#    pattern1 = '[a-z]'
#    string1 = m
#    n = re.findall(pattern1, string1)
#    print n
#    print 'out'

find_out_words_level3('http://www.pythonchallenge.com/pc/def/equality.html')