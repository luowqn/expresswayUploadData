#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:luowq
# Data: 2020/4/3 15:00
# File: config.py
import yaml

class Gantry:

    def __init__(self,**kwargs):
        self.__dict__.update(**kwargs)

class Configure:

   def __init__(self,file):
       with open(file,encoding='utf-8') as f:
           contents = yaml.safe_load(f)
           self.mLogLevel = contents['logLevel']
           self.mServerAddr = contents['serverAddr']
           self.mTests = []
           for d in contents['tests']:
               self.mTests.append(Gantry(**d))