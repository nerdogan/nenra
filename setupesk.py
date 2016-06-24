import sys
from cx_Freeze import setup, Executable
import sys
from esky import bdist_esky
from distutils.core import setup

base = None
if sys.platform == "win32":
    base = "Win32GUI"

import os
Mydata_files=[]
for file in os.listdir(r"C:\Users\NAMIK\PycharmProjects\nenra"):
    if file.endswith(".png"):
        f2 = file
        Mydata_files.append(f2)
print  Mydata_files
includefiles = Mydata_files
# Dependencies are automatically detected, but it might need fine tuning.
PY2APP_OPTIONS = {"packages": ["os"], "excludes": ["tkinter"]}

DATA_FILES = Mydata_files

# Using py2app
setup(
        name="Nenra esk",
        version="0.1002",
        scripts=[bdist_esky.Executable("nenra.py", icon="nenra.ico",shortcutName="Nenra",
            shortcutDir="DesktopFolder")],
        data_files=DATA_FILES,
        options={"bdist_esky": {
            "freezer_module": "cxfreeze",
            "freezer_options": PY2APP_OPTIONS,
        }}
)

