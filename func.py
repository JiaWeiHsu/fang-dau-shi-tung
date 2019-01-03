# /usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from time import time
import cv2
import numpy as np
import ConfigParser

ROOT_NODE = -1

def get_frame():
    img = open("image/1.jpg", "rb").read()
    return img

def countObj():

    if os.stat('image/0.jpg').st_size > 0:

        fidelity = False
        fidelityValue = .7
        img = cv2.imread('image/0.jpg')
        imgCopy = img.copy()
        img = cv2.medianBlur(img, 15)
        #img = cv2.adaptiveBilateralFilter(img, (5, 5), 150) # Preserve edges
        #img = cv2.blur(img, (3,3))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #imgt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 3, 10)
        _, imgt = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        #_, imgt = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY_INV)
        imgt = cv2.morphologyEx(imgt, cv2.MORPH_OPEN, (5, 5))

        img2 = imgt.copy()
        c, h = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        fidelityRange = 0
        if fidelity:
            maxArea = .0;
            for i in c: # With images it is convenient to know the greater area
                area = cv2.contourArea(i)
                if area > maxArea:
                    maxArea = area
            fidelityRange = maxArea - (maxArea * fidelityValue); # If objects have same size it prevents false detection

        totalContours = 0

        br = []
        for i in xrange(len(c)):
            if h[0][i][3] == ROOT_NODE and cv2.contourArea(c[i]) >= fidelityRange:
                totalContours += 1
                approx = cv2.approxPolyDP(c[i], 3, True)
                br.append(cv2.boundingRect(approx))
        for b in br:
            cv2.rectangle(imgCopy, (b[0], b[1]), (b[0] + b[2], b[1] + b[3]), (255, 255, 0), 3)
        cv2.imwrite('image/1.jpg', imgCopy)
        print 'Total contours: ', totalContours
        return totalContours

    else:
        print(-1)
        return -1


