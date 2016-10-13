application_title = "Nenra 1.0"
main_python_file = "nenra.py"

import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = ["atexit","re"]

setup(
    name = application_title,
    version = "1.0",
    description = "NEN Restaurant Automotion 1053",
    options = {
        "build_exe" : {
            "includes" : includes,
            "excludes": ['tcl', 'ttk', 'tkinter', 'Tkinter'],
        }
    },
    executables = [
        Executable(main_python_file, base = base)
    ]
)