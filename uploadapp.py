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
url = 'http://nen.duckdns.org:8080/dist/index1.php'
os.chdir('c:\\Users\\NAMIK\\Desktop\\nenra')
shutil.make_archive('nenra','zip','nenra')

files = {'file': open('c:\\Users\\NAMIK\\Desktop\\nenra\\nenra.zip', 'rb')}
r = requests.post(url, files=files)
