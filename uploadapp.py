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
from pushsafer import Client,init
url = 'http://nen.duckdns.org/dist/index1.php'
url1 = 'https://pushmeapi.jagcesar.se'
os.chdir('c:\\Users\\NAMIK\\Desktop\\nenra')
shutil.make_archive('nenra','zip','nenra')

files = {'file': open('c:\\Users\\NAMIK\\Desktop\\nenra\\nenra.zip', 'rb')}
r = requests.post(url, files=files)

appnot=" Namık ERDOĞAN saat 18:30 da çıkış yapmıştır"
files1 = {'title':appnot,'url':'http://nen.duckdns.org/masa.php','token':'uttju5EvfwKMJHftmlPMtmj2WvYbUZRgScOQBPoGTfQRqZgXsp5UxWOI0GXyoi4t'}


r = requests.post(url1,json=files1 )

init("cFZr0FW5Han7YxELPMZb")

appnot=" Namık ERDOĞAN saat 18:30 da çıkış yapmıştır"
Client("").send_message(appnot, "Bishop", "4274", "1", "4", "2", "https://www.pushsafer.com", "Open Pushsafer", "0", "", "", "")