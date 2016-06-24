# -*- coding: utf-8 -*-
#  name='',
# version='',
# packages=,
# url='',
# license='',
# author='',
# author_email='',
# description=''
from urllib2 import urlopen
import os

class Updater():
	def __init__(self):

		with open("ver.png", "r") as dosya:
			elma1=dosya.read()

		urlpath =urlopen('http://nen.duckdns.org:8080/dist/ver.png')
		string = urlpath.read()
		print string, elma1
		if elma1==string:
			print u"aynı"
		else:
			filename=string
			remotefile = urlopen('http://nen.duckdns.org:8080/dist/' + filename)
			localfile = open(filename,'wb')
			localfile.write(remotefile.read())
			localfile.close()
			remotefile.close()
			with open("ver.png", "w") as dosya:
				dosya.write(filename)
			os.system(filename)
