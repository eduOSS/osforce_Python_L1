#!/usr/bin/python
#coding:utf-8
from bs4 import BeautifulSoup
import urllib2,sys,urllib,threading,httplib,json,re

reload(sys)
sys.setdefaultencoding('utf8')
tags_url="http://book.douban.com/tag/"
page = urllib2.urlopen(tags_url)
soup = BeautifulSoup(page)

#tag_cols = soup.findAll("table",{"class":"tagCol"})
tds= soup.findAll('a',href=re.compile('^./'))
#for_pages = ?start=0&type=T

i = 0
try:
    while tds[i]:
        s= tds[i].string
        if isinstance(s,unicode):
            s=s.encode('gb2312')
        else:
            s=s.decode('utf-8').encode('gb2312')
        #tag_name=urllib.quote(tag_name_cn)
        tag_page = urllib2.urlopen(tags_url+s)
        i+=1
	pics_url_soup=BeautifulSoup(tag_page)
        pics_url=pics_url_soup.findAll("img",{"class":""})
	print pics_url 
	print '*',len(pics_url),"*"
	pic_url=pics_url[0]['src']
        urllib.urlretrieve(pic_url,'./img/'+pic_url[-12:])
except:
     print 'over!'
