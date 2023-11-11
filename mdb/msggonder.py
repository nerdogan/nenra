# -*- coding:utf8 -*-
from datetime import datetime, timedelta
import time as ttim
import smtplib
from socket import *
import subprocess
import requests
import sys
import nenraconfig


token = nenraconfig._GetOption2('token')

print(token)
elma = sys.argv[1]
print(elma)
rq = requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),
                   data={'chat_id': 839088426, 'text': elma}).json()
rq = requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),
                   data={'chat_id': 1445403534, 'text': elma}).json()
