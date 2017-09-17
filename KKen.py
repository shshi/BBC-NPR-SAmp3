#!/usr/bin/env python
#-*- coding: utf-8 -*-

#===========================================================
# File Name: KKen.py
# Author：shshi
# E-mail:553102057@qq.com
# Created Time: 2013-12-06
# Version: 1.0
# Description: 
# Copyright: Wayne_Shih
#===========================================================
import re
import urllib
import os
class KKen():
    url = ''
    def __init__(self, url):
        self.url = url

    def getLink(self):
        url = self.url
        page = urllib.urlopen(url)
        html = page.read()
        reg = r'<a href="(.*?)" title="(?:(?!视频|词汇).)*?" target="_blank">.*?</a>'
        link_re = re.compile(reg)
        link_list = re.findall(link_re,html)
        newspage = "http://www.kekenet.com%s"%str(link_list[0])
        return newspage

    def getMp3(self):
        url = self.getLink()
        page = urllib.urlopen(url)
        html = page.read()
        reg0 = r"var domain= '(.*?)';"
        Furl0_re = re.compile(reg0)
        Furl0 = re.findall(Furl0_re,html)

        reg1 = r'var thunder_url ="(.*?\.mp3)"'
        Furl1_re = re.compile(reg1)
        global Furl1
        Furl1 = re.findall(Furl1_re,html)     
           
        Link_mp3 = str(Furl0[0])+str(Furl1[0])

        if os.path.exists('./kekemp3/%s'%Furl1[0].split('/')[-1]):
            return False
        else:
            mp3_path='./kekemp3/%s'%Furl1[0].split('/')[-1]
            urllib.urlretrieve(Link_mp3,mp3_path)
            return mp3_path

    def getLrc(self):
        Link_lrc = "http://www.kekenet.com/"+str(Furl1[0])+".lrc"
        if os.path.exists('./kekemp3/%s.lrc'%re.split('/|\.',Furl1[0])[-2]):
            return False
        else:
            lrc_path='./kekemp3/%s.lrc'%re.split('/|\.',Furl1[0])[-2]
            urllib.urlretrieve(Link_lrc,lrc_path)
            return lrc_path
if __name__ == '__main__':
    File = KKen("http://www.kekenet.com/broadcast/bbc/")
    File.getMp3()
    File.getLrc()
