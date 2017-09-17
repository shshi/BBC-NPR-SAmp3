#!/usr/bin/env python
#-*- coding: utf-8 -*-

#===========================================================
# File Name: sendmail.py
# Author：shshi
# E-mail:553102057@qq.com
# Created Time: 2013-12-06
# Version: 1.0
# Description: 
# Copyright: Wayne_Shih
#===========================================================

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Sconfig import mail_host,mail_user,mail_pass,mail_postfix
#####################
def send_mail(receiver,sub,content,attfile1,attfile2,attfile3,attfile4):
    
    me="Wayne_rbt"+"<"+mail_user+"@"+mail_postfix+">"
    
    msg = MIMEMultipart()
    if attfile1:
        att1 = MIMEText(open(attfile1,'rb').read(),'base64','gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment;filename=%s'%attfile1
        msg.attach(att1)

    if attfile2:
        att2 = MIMEText(open(attfile2,'rb').read(),'base64','gb2312')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment;filename=%s'%attfile2
        msg.attach(att2)

    if attfile3:
        att3 = MIMEText(open(attfile3,'rb').read(),'base64','gb2312')
        att3["Content-Type"] = 'application/octet-stream'
        att3["Content-Disposition"] = 'attachment;filename=%s'%attfile3
        msg.attach(att3)

    if attfile4:
        att4 = MIMEText(open(attfile4,'rb').read(),'base64','gb2312')
        att4["Content-Type"] = 'application/octet-stream'
        att4["Content-Disposition"] = 'attachment;filename=%s'%attfile4
        msg.attach(att4)
    
    body = MIMEText(content)
    msg.attach(body)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ",".join(receiver)
    
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, receiver, msg.as_string())
        s.close()
        print "Successfully sent to %s"%msg['to']
        return True
    except Exception, e:
        print "Failed while sending to %s"%str(e)
        return False

