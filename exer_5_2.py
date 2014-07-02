#!/usr/bin/python
#coding:utf-8
from bs4 import BeautifulSoup
import urllib2,sys,urllib,threading,httplib,json,re
import time,multiprocessing

tags_url="http://book.douban.com/tag/"
page = urllib2.urlopen(tags_url)
soup = BeautifulSoup(page)
tag_cols = soup.findAll("table",{"class":"tagCol"}) # find all the tag cloums

pics_url_in_one_column=[] #for adding comsumer queue 

def get_the_right_coding(s)
    if isinstance(s,unicode):
        new_s=s.encode('gb2312')
    else:
        new_s=s.decode('utf-8').encode('gb2312')
    return new_s

def get_pics_url(cn):
    tds= tag_cols[cn].findAll('a',href=re.compile('^./'))#find all the tags in one tag column
    i = 0
    try:
         while tds[i]:
             s0= tds[i].string #get the number i's tag name
 	     s=get_the_right_coding(s0)
             tag_page = urllib2.urlopen(tags_url+s)#get the tag page via its url
             pics_url_soup=BeautifulSoup(tag_page)
             pics_url=pics_url_soup.findAll("img",{"class":""}) # pictures' urls are contained in pics_url
             #urllib.urlretrieve(pics_url[0]["src"],'an.jpg')
             i+=1
             pics_url_in_one_column.append(pics_url) #append the variable pics_url to the list 
    except:
        print 'finish getting all pics url in one column'

class producer(multiprocessing.Process): 
    def run(self,cn):
        get_pics_url(cn)

class comsumer(multiprocessing.Process):
    def run(self):
        d
