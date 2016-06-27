import sys
from cx_Freeze import setup, Executable

import os
Mydata_files=[]
for file in os.listdir(r"C:\Users\NAMIK\PycharmProjects\nenra"):
    if file.endswith(".png"):
        f2 = file
        Mydata_files.append(f2)
print  Mydata_files
includefiles = Mydata_files
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"],'include_files':includefiles}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "nenra",
        version = "0.1012",
        description = "NEN Restaurant Automotion"
                      "",
        options = {"build_exe": build_exe_options},
        executables = [Executable("nenra.py", base=base,icon="nenra.ico")]
        )