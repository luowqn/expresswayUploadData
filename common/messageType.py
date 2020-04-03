#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:luowq
# Data: 2020/4/3 17:40
# File: messageType.py
from enum import Enum,unique

@unique
class MessageTypeEnum(Enum):
    CAR_FACE_MSG = 0
    CAR_BODY_MSG = 1
    CAR_PLATENUMBER_MSG = 2
    CAR_MODULE_MSG =4
    DATA_ACCESS_MSG = 5
    HEART_BEAT_MSG = 6