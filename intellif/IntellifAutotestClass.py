#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import base64
import pymysql

__author__ = "xestone"


class DbData(object):
    def __init__(self, ip='192.168.2.27', user='root', password='introcks1234', db_name='intellif_face'):
        self.ip = ip
        self.user = user
        self.password = password
        self.db_name = db_name

    def query(self, t_name='t_face_1', count=100):
        listFeatures = []
        database = pymysql.connect(self.ip, self.user, self.password, self.db_name)
        cursor = database.cursor()
        sql = "select face_feature from %s limit %s" % (t_name, count)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            # BLOB数据类型处理
            encoded = base64.b64encode(row[0])
            decoded = encoded.decode('utf-8')
            listFeatures.append(decoded)
        return listFeatures
