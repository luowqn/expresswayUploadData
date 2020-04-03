#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:luowq
# Data: 2020/4/3 16:02
# File: initSystem.py
from config import Configure
from Signalway import SwLog

def initLog(file,loglevel):
    try:
        log = SwLog(file,loglevel)
        return log
    except Exception as ex:
        raise ex

def initConf(file):
    try:
        conf = Configure(file)
        return conf
    except Exception as ex:
        raise  ex



