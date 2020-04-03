#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:luowq
# Data: 2020/4/3 12:25
# File: main.py
from function.initSystem import initConf,initLog

if __name__ == '__main__':
    conf = initConf('config.yml')
    initLog('logs/expresswayUploadData.log',conf.mLogLevel)