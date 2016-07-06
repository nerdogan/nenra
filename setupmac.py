'''

from distutils.core import setup
import py2app
py2app_options = dict(
    iconfile='nenra.icns',
)
setup(
    app=['nenra.py'],
    data_files=[
      'fatura.png',
      'image.png',
'maliyet.png',	
    ],
    options=dict(
      py2app=py2app_options,
    )
)

'''

import sys
from cx_Freeze import setup, Executable

import os

Mydata_files=[]
for file in os.listdir(r"/Users/nenra/PROCE/nenra"):
    if file.endswith(".png"):
        f2 = file
        Mydata_files.append(f2)
print  Mydata_files
#Mydata_files.append("horn.wav")
includefiles = Mydata_files
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"],'include_files':includefiles}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "nenra",
        version = "0.1016",
        description = "NEN Restaurant Automotion 1016"
                      "",
        options = {"build_exe": build_exe_options},
        executables = [Executable("nenra.py",icon="nenra.icns")]
        )