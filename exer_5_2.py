#!/usr/bin/python
#coding:utf-8
from bs4 import BeautifulSoup
import urllib2,sys,os,urllib,threading,httplib,json,re
import time,multiprocessing

#tag_cols = soup.findAll("table",{"class":"tagCol"}) # find all the tag cloums

tags_name=multiprocessing.Queue() #for adding consumer queue 
tags_url="http://book.douban.com/tag/"

def get_the_right_coding(s):
    if isinstance(s,unicode):
        new_s=s.encode('gb2312')
    else:
        new_s=s.decode('utf-8').encode('gb2312')
    return new_s

class producer(multiprocessing.Process):#the function of one producer is to get the pics_url of one column 
	def run(self):
	    page = urllib2.urlopen(tags_url)
	    soup = BeautifulSoup(page)
	    tds= soup.findAll('a',href=re.compile('^./'))#find all the tags 
	    i = 0
	    try:
		 while tds[i]:
		     s0= tds[i].string #get the number i's tag name
		     s=get_the_right_coding(s0)
		     tags_name.put(s)#append the variable pics_url to the list 
		     i+=1
	    except:
		print 'finish getting all pics url in one column'

class consumer(multiprocessing.Process): # the function of one consumer is to download all the picture of in one tag
    def run(self):#in the first version we only consider on page 
        tag_name=tags_name.get()
        if not os.path.isdir("./img/"+tag_name+"/"):
            os.mkdir("./img/"+tag_name+"/")  
        tag_page = urllib2.urlopen(tags_url+tag_name)#get the tag page via its url
        pics_url_soup=BeautifulSoup(tag_page)
        pics_url_in=pics_url_soup.findAll("img",{"class":""}) # pictures' urls are contained in pics_url
	for i in range(len(pics_url_in)):
	    pic_url=pics_url_in[i]['src']
            urllib.urlretrieve(pic_url,"./img/"+tag_name+"/"+pic_url[-12:])

p=producer()
c=consumer()

p.start()
c.start()

c.join()
p.join()
