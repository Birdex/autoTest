#!/usr/bin/env python
# -*- coding:utf-8 -*-
from intellif.IntellifAutotestClass import DbData
from intellif.execute import compare

__author__ = "xestone"

listFeatures = DbData(ip='192.168.2.27').query(t_name='t_face_1', count=100)
for feature in listFeatures:
    compare()
