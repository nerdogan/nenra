# name='',
# version='',
# packages=,
# url='',
# license='',
# author='',
# author_email='',
# description=''

import requests
url = 'http://nen.duckdns.org/dist/index1.php'


files = {'file': open('/Users/namikerdogan/nenra/rw.nenra.dmg', 'rb')}
r = requests.post(url, files=files)
