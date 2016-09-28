#Written by Mariah Davis
#09/11/2016

import urllib
import feedparser
from nltk import tokenize, sent_tokenize

#Must install feedparser and nltk before using this program.

#Reads in RSS feed, converts it to a string. Then creates a list of strings
#based on the RSS feed. Compares both the entire feed, as well as the individual
#string in the feed, to the feed already placed into a dictionary. If the feed is
#a duplicate, delete the url from the dictionary. Print out the reamining urls
#to an output file. Keeps the mapped feed to the URL for future use/alteratiion
#to the code.

start_line = 0
flag = 0
rss_url_feed_dict = {}
rss_url_feed_non_repeat_dict = {}

with open ("/home/piglet/Documents/feed_list.tsv") as inputfile:
    for line in inputfile:
        if start_line >= 1:
            url = line[7:]
            rss_feed = feedparser.parse(url)
            rss_feed_string = str(rss_feed['feed'])
            rss_feed_paragraph= tokenize.sent_tokenize(rss_feed_string)
            
            for key in rss_url_feed_dict:
                for value in rss_url_feed_dict[key]:
                    if rss_feed_string in rss_url_feed_dict[key]:
                        flag = 1
                        break
                    
            if flag == 0:
                rss_url_feed_non_repeat_dict [url] = [rss_feed_string]
                rss_url_feed_dict [url] = [rss_feed_string]
                
                for key in rss_url_feed_dict:
                    for value in rss_url_feed_dict[key]:
                        for sentence in rss_feed_paragraph:
                            if sentence in rss_url_feed_dict[key]:
                                flag = 1
                                break
                if flag == 0:
                    rss_url_feed_non_repeat_dict [url] = [rss_feed_string]
                    rss_url_feed_dict [url] = [rss_feed_string]
                else:
                    rss_url_feed_dict [url] = [rss_feed_string]
                    
            if flag == 1:
                rss_url_feed_dict [url] = [rss_feed_string]
                
        flag = 0       
        start_line = start_line +1

rss_url_feed_dict.clear()
inputfile.close()

outputfile = open('output.txt', 'w')

for key in rss_url_feed_non_repeat_dict:
    outputfile.write(key)

outputfile.close()
