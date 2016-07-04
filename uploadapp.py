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
files = {'file': open('ver.png', 'rb')}
r = requests.post(url, files=files)


files = {'file': open('./dist/nenra-0.1016-win32.msi', 'rb')}
r = requests.post(url, files=files)

