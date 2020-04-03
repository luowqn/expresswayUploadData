#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:luowq
# Data: 2020/4/3 17:08
# File: test.py
import urllib3
from io import BytesIO
from PIL import Image
import requests

resp = requests.get('http://172.18.2.9:82/test/桂AV1225_出口图片_车头.jpg')
tmpIm = BytesIO(resp.content)
im = Image.open(tmpIm)
w = im.size[0]
h = im.size[1]
print(w,h)