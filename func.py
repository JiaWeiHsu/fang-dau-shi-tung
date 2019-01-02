#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from time import time
import cv2
import numpy as np
import ConfigParser

def get_frame():
    index = str(int(time()) % 2)
    img = open("image/" + index + ".jpg", "rb").read()
    return img


def sendEmail(img, to_addr):
    cf = ConfigParser.ConfigParser()
    cf.read("email.conf")

    gmail_user = cf.get("email", "username")
    gmail_password = cf.get("email", "password")
    Subject = "標題"

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = Subject
    msgRoot['From'] = gmail_user
    msgRoot['To'] = to_addr
    
    fp = open(img, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-Disposition', 'attachment', filename=os.path.basename(img))
    msgRoot.attach(msgImage)
   
    msg=msgRoot.as_string()

    smtp=smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.ehlo()
    smtp.login(gmail_user, gmail_password)
    status=smtp.sendmail(gmail_user, to_addr, msg)
    if status=={}:
        print("郵件傳送成功!")
    else:
        print("郵件傳送失敗!")
    smtp.quit()


def isDifferent(imgA, imgB):
    img1 = cv2.imread('image/0.jpg', 0)
    img2 = cv2.imread('image/1.jpg', 0)
    res = cv2.absdiff(img1, img2)
    res = res.astype(numpy.uint8)
    percentage = (numpy.count_nonzero(res) * 100)/ res.size
    print percentage

# sendEmail("image/0.jpg","bryan35818363680919@gmail.com")
