
#open the file
f = open('C:\Users\yannpxia\Desktop\chracaters.txt','r')

characters = f.read()
#print characters



dict1 = {'00':00}

for i in characters:
    flag = 0
    for key in dict1.keys():
        print 'hello'
        if key == i:
            print 'I am here'
            dict1[i] = dict1[i] + 1
            flag += 1
            break

    if flag == 0:
        print 'I am there'
        dict1[i] = 1;

for key in dict1:
    print 'key=%s, value=%s' %(key, dict1[key])

########################################################
import urllib

inchar = "abcdefghijklmnopqrstuvwxyz"
remaining = []

def pleasework(url):
    doclocation = urllib.urlopen(url)
    openfile = doclocation.read()
    comment = openfile.split('<!--')[2]
    for s in comment:
        if s in inchar:
            remaining.append(s)
    print remaining

pleasework('http://www.pythonchallenge.com/pc/def/ocr.html')
