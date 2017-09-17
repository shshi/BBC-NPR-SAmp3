#!/usr/bin/env python
#-*- coding: utf-8 -*-

#===========================================================
# File Name: Sexe.py
# Author：shshi
# E-mail:553102057@qq.com
# Created Time: 2013-12-06
# Version: 1.0
# Description: 
# Copyright: Wayne_Shih
#===========================================================
import KKen
import SciA
import sendmail
from Sconfig import receiver1,receiver2

File_BBC=KKen.KKen("http://www.kekenet.com/broadcast/bbc/")
File_NPR=KKen.KKen("http://www.kekenet.com/broadcast/NPR/")
File_SA=SciA.SciA("http://www.scientificamerican.com/podcast/60-second-science/")
#File_SA_podcast=SciA.SciA("http://www.scientificamerican.com/podcast/podcasts.cfm?type=60-second-science")

mp3_BBC=File_BBC.getMp3()
lrc_BBC=File_BBC.getLrc()
mp3_NPR=File_NPR.getMp3()
lrc_NPR=File_NPR.getLrc()
mp3_SA=File_SA.getMp3()
txt_SA=File_SA.getTxt()
#mp3_SciA=File_SA_podcast.getMp3()
#txt_SciA=File_SA_podcast.getTxt()

sub_BN="Your latest BBC and NPR news from Wayne"
sub_SA="Your latest Scientific American from Wayne"
sub_SciA="Your latest Scientific American Podcast from Wayne"

content_BN="carpe diem!\n\n\nMore information here:[BBC]%s ;  [NPR]%s\n-------this mail is automatically sent by Wayne_Shih's little robot"%(File_BBC.getLink(),File_NPR.getLink())
content_BBC="carpe diem!\n\n\nMore information here:[BBC]%s ; No update for NPR\n-------this mail is automatically sent by Wayne_Shih's little robot"%File_BBC.getLink()
content_NPR="carpe diem!\n\n\nMore information here:[NPR]%s ; No update for BBC\n-------this mail is automatically sent by Wayne_Shih's little robot"%File_NPR.getLink()
content_SA="enjoy your day!\n\n\nMore information here:%s\n-------this mail is automatically sent by Wayne_Shih's little robot"%File_SA.getLink()
#content_SciA="enjoy your day!\n\n\nMore information here:%s\n-------this mail is automatically sent by Wayne_Shih's little robot"%File_SA_podcast.getLink()

if mp3_BBC == False and mp3_NPR == False:
    print "No update for BBC and NPR"
else:
    for i in receiver2:
        if mp3_BBC != False and mp3_NPR != False:
            sendmail.send_mail(i,sub_BN,content_BN,mp3_BBC,lrc_BBC,mp3_NPR,lrc_NPR)
        elif mp3_BBC != False:
            sendmail.send_mail(i,sub_BN,content_BBC,mp3_BBC,lrc_BBC,mp3_NPR,lrc_NPR)
            print "No update for NPR"
        else:
            sendmail.send_mail(i,sub_BN,content_NPR,mp3_BBC,lrc_BBC,mp3_NPR,lrc_NPR)
            print "No update for BBC"
			
if mp3_SA == False:
    print "No update for Scientific American"
else:
    for i in receiver1:
        sendmail.send_mail(i,sub_SA,content_SA,mp3_SA,txt_SA,False,False)
'''
if mp3_SciA == False:
    print "No update for Scientific American Podcast"
else:
    for i in receiver1:
        sendmail.send_mail(i,sub_SciA,content_SciA,mp3_SciA,txt_SciA,False,False)
'''

