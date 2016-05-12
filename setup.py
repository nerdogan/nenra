#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      muhasebe-2
#
# Created:     27.01.2014
# Copyright:   (c) muhasebe-2 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from distutils.core import setup
import py2exe,sys,os 
sys.argv.append('py2exe')

import os
Mydata_files=[]
for file in os.listdir(r"C:\Users\NAMIK\PycharmProjects\nenra"):
    if file.endswith(".png"):
        f2 = '', [file]
        Mydata_files.append(f2)

setup(
    name = 'NENRA',
    description = 'Restaurant Automotion',
    version = '1.4.2',
	windows=[{ 'script':'nenra.py','icon_resources': [(0, 'nenra.ico')] }],
	options={
    'py2exe': {
    'packages' : ['PyQt4','adodbapi','reportlab',
    'reportlab.graphics.charts',
    'reportlab.graphics.samples',
    'reportlab.graphics.widgets',
    'reportlab.graphics.barcode',
    'reportlab.graphics',
    'reportlab.lib',
    'reportlab.pdfbase',
    'reportlab.pdfgen',
    'reportlab.platypus'],
    'includes':['sip','MySQLdb'],
    'dll_excludes': [''],
    'bundle_files': 1 
    }
    },
data_files = Mydata_files
    )


