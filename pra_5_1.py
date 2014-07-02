# -*- coding: cp936 -*-
import time,string
import mechanize,urllib
from mechanize import Browser

urlname=urllib.quote('马伊琍')
br=Browser()
br.set_handle_robots(False) ##ignore the robots.txt
urlhttp=r'http://www.baidu.com/s?'+urlname+"&pn=10&rn=20&ie=utf-8&usm=4&rsv_page=1"
response=br.open(urlhttp)
filename='temp.html'
f=open(filename,'w')
f.write(response.read())
f.close()
