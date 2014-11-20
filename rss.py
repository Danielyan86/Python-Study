import feedparser
    
python_wiki_rss_url = "http://ax.phobos.apple.com.edgesuite.net/WebObjects/MZStore.woa/wpa/MRSS/newreleases/limit=300/rss.xml"


feed = feedparser.parse( python_wiki_rss_url )


f = open("rss.xml","r+")
print type(feed)
for item in feed['items']:
	print type(item)
	for key in item.keys():
		print item[key]
	# break
		# for key in i.keys():
		# 	print key


f.close()

# print feed