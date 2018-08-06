import urllib
import re

def find_out_words_level3(url):
    for count in range(1,400):   #repeat 400 times
        print 'enter function'
        print 'original string: ' + url
        doclocation = urllib.urlopen(url)
        openfile = doclocation.read()   # get all characters of url page

        print openfile
        if 'Divide by' in openfile:
            pattern = '\d+$'
            obj = re.search(pattern, url)
            print obj.group(0)
            num = obj.group(0)
            num = int(num)/2
        elif 'html' in openfile:
            num = openfile.split('.')[0]
            print num
            pattern = '\d+$'
            break
        else:
            pattern = '\d+$'
            num = re.search(pattern, openfile)
            print num.group(0)
            num = num.group(0)
        num = str(num)
        pattern = url.split('=')[1]
        print 'pattern:' + pattern
        url = re.sub(pattern, num, url)  #replace the the new num of old num in url as the next url
        print url
        print 'end of function'



find_out_words_level3('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=59022')