# -*- coding:utf8 -*-

# name='',
# version='',
# packages=,
# url='',
# license='',
# author='',
# author_email='',
# description=''
import shutil
import os
import requests

url = 'http://nen.duckdns.org/dist/index1.php'
url1 = 'https://pushmeapi.jagcesar.se'
os.chdir('c:\\Users\\NAMIK\\Desktop\\nenra')
shutil.make_archive('nenra','zip','nenra')

files = {'file': open('c:\\Users\\NAMIK\\Desktop\\nenra\\nenra.zip', 'rb')}
r = requests.post(url, files=files)

appnot=" Nenra yeni versiyon yüklendi"
files1 = {'title':appnot,'url':'http://nen.duckdns.org/dist','token':'uttju5EvfwKMJHftmlPMtmj2WvYbUZRgScOQBPoGTfQRqZgXsp5UxWOI0GXyoi4t'}


r = requests.post(url1,json=files1 )

