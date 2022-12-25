C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic6.exe -x mainwindow.ui -o ui_mainwindow.py
C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic6.exe -x recete.ui -o ui_recete.py
C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic6.exe -x recete2.ui -o ui_recete2.py
C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic6.exe -x fatura.ui -o ui_fatura.py
C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic6.exe -x maliyet.ui -o ui_maliyet.py
C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic6.exe -x cari.ui -o ui_cari.py
C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic6.exe -x stok.ui -o ui_stok.py
C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic6.exe -x rapor.ui -o ui_rapor.py
C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic6.exe -x masraf.ui -o ui_masraf.py
C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic6.exe -x hesap.ui -o ui_hesap.py


rem *** Used to create a Python exe 

rem ***** get rid of all the old files in the build folder Compress-Archive -Path "C:\sordum\" -DestinationPath "C:\sordum.zip"
rd /S /Q build

rem ***** create the e
c:\users\namik\appdata\local\programs\python\Python38\Scripts\pyinstaller --clean --win-private-assemblies -F nenra.spec --distpath="C:\Users\NAMIK\OneDrive\Desktop\nenra2"  -w

rem "c:\Program Files (x86)\WinRAR\Rar.exe" a -r c:\Users\NAMIK\Desktop\nenra\nenra.rar c:\Users\NAMIK\Desktop\nenra\nenra
python uploadapp.py
rem D:\aproje\nenra\mdb\dist\nenra2.exe
rem **** pause so we can see the exit codes
rem pause "done...hit a key to exit"
rem xcopy D:\aproje\nenra\mdb\dist y:\nenra2 /s /d /y