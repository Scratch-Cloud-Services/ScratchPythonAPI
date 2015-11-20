import json
import socket
from urllib import request
import requests
import hashlib

__author__ = 'robin'


class cloud:

    cloudPort = 531
    cloudIp = 'cloud.scratch.mit.edu'

    def __init__(self,sessionId,username,projectId):
        self.sessionId = sessionId
        self.projectid = projectId
        self.username = username

        self.cloudId = self.getCloudId()
        self.md5 = hashlib.md5()

        # create an INET, STREAMing socket
        print("Connecting to Cloud server..")
        self.socket = socket.create_connection((self.cloudIp, self.cloudPort))
        print('Connected!')

    def getCloudId(self):
        cookies = dict(scratchsessionsid = self.sessionId)

        r = requests.get('https://scratch.mit.edu/projects/'+str(self.projectid)+'/cloud-data.js',cookies=cookies)
        r.encoding = 'utf8'
        return r.text[1495:1531]




    def set(self,var, val):
        #{"user": "robinp", "value": "", "token2": "md5 hex of token", "token": "cloudId", "name": "☁ STORAGE", "method": "set", "project_id": "10085455"}

        self.md5.update(self.cloudId.encode('utf-8'))

        payload = {
            'user': self.username,
            'value': val,
            'token': self.cloudId,
            'token2': self.md5.hexdigest(),
            'name': '☁ '+var,
            'method': 'set',
            'project_id': self.projectid

        }


        print(json.dumps(payload))
        self.socket.send(json.dumps(payload).encode())
        return '☁ '+var
