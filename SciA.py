#!/usr/bin/env python
#-*- coding: utf-8 -*-

#===========================================================
# File Name: SciA.py
# Author：shshi
# E-mail:553102057@qq.com
# Created Time: 2014-01-17
# Version: 1.0
# Description: 
# Copyright: Wayne_Shih
#===========================================================
import re
import urllib
import os
from bs4 import BeautifulSoup
class SciA():
    url = ''
    def __init__(self, url):
        self.url = url

    def getLink(self):
        url = self.url
        page = urllib.urlopen(url)
        html = page.read()
        reg = r'<a class="thumb" href="(.*?)" title=".*?">'
        link_re = re.compile(reg)
        link_list = re.findall(link_re,html)
        newspage = "http://www.scientificamerican.com"+str(link_list[0])
        return newspage

    def getMp3(self):
        url = self.getLink()
        page = urllib.urlopen(url)
        html = page.read()
#        print html
#        reg = r'<a id="mp3Link" href="(.*?)"'
        reg = r'<a href="(.*?)" rel="nofollow">Download MP3</a>'

        Mp3_re = re.compile(reg)
        Mp3_list = re.findall(Mp3_re,html)     
        Mp3_link = "http://www.scientificamerican.com"+str(Mp3_list[0])
#        print Mp3_link
        
        regn = r'<title>(.*?)</title>'
        regn_re = re.compile(regn)
        reg_name = str(re.findall(regn_re,html)[0])+".mp3"
            
        mp3_path='./SAmp3/%s'%reg_name
        if os.path.exists(mp3_path):
            return False
        else:
            urllib.urlretrieve(Mp3_link,mp3_path)
            return mp3_path

    def getTxt(self):
        url = self.getLink()
        page = urllib.urlopen(url)
        html = page.read()
        soup = BeautifulSoup(html)
        
        txt_path='./SAmp3/%s.txt'%soup.title.get_text()
        if os.path.exists(txt_path):
            return False
        else:
            f = open(txt_path,'a')
#            f.write('%s'%soup.find("span",text=re.compile("2014")).get_text())    #Write Date
            f.write('\n%s\n'%soup.title.get_text())                               #Write Title 
            f.write('%s\n'%soup.p.get_text().encode("utf-8"))                       #Write Introduction
            f.write('*'*17)                                                       #Write Delimiter
#            for i in soup.find_all("p")[4:10]:    
#                f.write('%s'%i.get_text().encode("utf-8"))                        #Write Body
            f.close()
            return txt_path


if __name__ == '__main__':
    File = SciA("http://www.scientificamerican.com/podcast/60-second-science/")
    File.getLink()
    File.getMp3()
    File.getTxt()
