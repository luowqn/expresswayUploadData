#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:luowq
# Data: 2020/4/3 16:01
# File: toExpressWay.py
from Signalway import  SwRequests
from common import MessageTypeEnum

class UploadData:

    def __init__(self,serverAddr):
        self.mSockfd = SwRequests(0)
        self.mServerAddr = serverAddr
        self.mDataAccess = self.__getBody('jsons/dataAccess.json')
        self.mHeartBeat = self.__getBody('jsons/heartbeat.json')


    def post(self,msgType,url):
        try:
            json = None
            if msgType == MessageTypeEnum.DATA_ACCESS_MSG:
                json = self.
            elif msgType == MessageTypeEnum.HEART_BEAT_MSG:
                pass
            if json:
                resp = self.mSockfd.post(self.mServerAddr+"/"+url,)
                return resp
            else:
                return None
        except Exception as ex:
            raise ex

    def __getBody(self, file):
        try:
            with open(file, encoding='utf-8') as f:
                bodyText = f.read()
                return bodyText
        except Exception as ex:
            raise ex

    def close(self):
         self.mSockfd.close()