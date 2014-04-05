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

setup(
    name = 'NENRA',
    description = 'Restaurant Automotion',
    version = '1.1.1',
	windows=['nenra.py'],
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
data_files = [
            ('phonon_backend',  [ 'F:\PortablePython2751\App\Lib\site-packages\PyQt4\plugins\phonon_backend\phonon_ds94.dll' ]),
            ('datalar', ['F:\\PortablePython2751\\datalar\\18022014.mdb']) ]
    )


