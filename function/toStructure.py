#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:luowq
# Data: 2020/4/3 16:01
# File: toStructure.py
from Signalway import SwRequests,SwString,SwFile,SwTime
from common import MessageTypeEnum
import uuid

class Strutrue:

    def __init__(self,url,apiKey,token):
        self.mSockfd = SwRequests(0)
        self.mUrl = url
        self.mApiKey = apiKey
        self.mToken = token
        self.mCarBodyJson = self.__getBody('jsons/carBody.json')
        self.mCarFaceJson =self.__getBody('jsons/carFace.json')
        self.mCarModuleJson = self.__getBody('jsons/carModule.json')
        self.mPlateNumberJson = self.__getBody('jsons/plateNumber.json')
        self.mDataAccessJson = self.__getBody('jsons/dataAccess.json')
        self.mHeartBeatJson = self.__getBody('jsons/heartbeat.json')

    def post(self, msgType, imageUrl):
        try:
            json = None
            if msgType == MessageTypeEnum.CAR_FACE_MSG:
                json = self.mCarFaceJson
            elif msgType == MessageTypeEnum.CAR_BODY_MSG:
                json = self.mCarBodyJson
            elif msgType == MessageTypeEnum.CAR_MODULE_MSG:
                json = self.mCarModuleJson
            elif msgType == MessageTypeEnum.CAR_PLATENUMBER_MSG:
                json = self.mPlateNumberJson
            if json:
                body = self.__generateBody(json, imageUrl)
                bodyJson = SwString.toJson(body)
                resp = self.mSockfd.post(self.mUrl, bodyJson)
                return resp
            else:
                return None
        except Exception as ex:
            raise ex

    def close(self):
        self.mSockfd.close()

    def __getBody(self,file):
        try:
            with open(file,encoding='utf-8') as f:
                bodyText = f.read()
                return bodyText
        except Exception as ex:
            raise ex

    def __generateBody(self,body,imageUrl):
        try:
            source = bytes(imageUrl, encoding="utf8")
            newKey = SwString.toHmacMd5(self.mToken,source)
            w,h = SwFile.getImageSize(imageUrl)
            imageName = imageUrl.split('/')[-1]
            self.mPlateNumberBody = self.__replaceBodyVars(body,newKey,w,h,imageName,imageUrl)

        except Exception as ex:
            raise ex

    def __replaceBodyVars(self,String,newKey,w,h,imageName,imageUrl):
       id = str(uuid.uuid4())
       return String.replace("${id}",id).replace("${apiKey}",self.mApiKey)\
                .replace("${newKey}",newKey).replace("${imageWidth}",w).replace("${imageHeight}",h)\
                .replace("${imageTime}",SwTime.getNow()).replace("${imageName}",imageName).replace("${imageUrl}",imageUrl)

