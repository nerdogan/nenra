python C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py -x mainwindow.ui -o ui_mainwindow.py
python C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py -x recete.ui -o ui_recete.py
python C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py -x recete2.ui -o ui_recete2.py
python C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py -x fatura.ui -o ui_fatura.py
python C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py -x maliyet.ui -o ui_maliyet.py
python C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py -x cari.ui -o ui_cari.py
python C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py -x stok.ui -o ui_stok.py
python C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py -x rapor.ui -o ui_rapor.py
python C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py -x masraf.ui -o ui_masraf.py
python C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py -x hesap.ui -o ui_hesap.py


rem *** Used to create a Python exe 

rem ***** get rid of all the old files in the build folder
rd /S /Q build

rem ***** create the e
pyinstaller --clean --win-private-assemblies -F nenra.spec --distpath="C:\Users\NAMIK\Desktop\nenra"  -w

rem "c:\Program Files (x86)\WinRAR\Rar.exe" a -r c:\Users\NAMIK\Desktop\nenra\nenra.rar c:\Users\NAMIK\Desktop\nenra\nenra
python uploadapp.py
rem D:\aproje\nenra\mdb\dist\nenra2.exe
rem **** pause so we can see the exit codes
rem pause "done...hit a key to exit"
rem xcopy D:\aproje\nenra\mdb\dist y:\nenra2 /s /d /y