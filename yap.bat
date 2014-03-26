python C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py -x mainwindow.ui -o ui_mainwindow.py
python C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py -x recete.ui -o ui_recete.py
python C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py -x recete2.ui -o ui_recete2.py
python C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py -x fatura.ui -o ui_fatura.py

rem *** Used to create a Python exe 

rem ***** get rid of all the old files in the build folder
rd /S /Q build

rem ***** create the exe
python setup.py py2exe --includes sip
D:\aproje\nenra\dist\nenra.exe
rem **** pause so we can see the exit codes
rem pause "done...hit a key to exit"
xcopy D:\aproje\nenra\dist y:\nenra /s /d /y
xcopy Z:\datalar\gunluk D:\aproje\nenra\mdb\dist\datalar /s /d /y