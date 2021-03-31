python "C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic.py" -x mainwindow.ui -o ui_mainwindow.py
python "C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic.py" -x recete.ui -o ui_recete.py
python "C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic.py" -x recete2.ui -o ui_recete2.py
python "C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic.py" -x fatura.ui -o ui_fatura.py
python "C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic.py" -x maliyet.ui -o ui_maliyet.py
python "C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic.py" -x rapor.ui -o ui_rapor.py
python "C:\Users\bisho\PycharmProjects\nenra\venv\Scripts\pyuic.py" -x rapor.ui -o ui_rapor.py

rem ***** get rid of all the old files in the build folder
rd /S /Q build

rem ***** create the exe


python setupcx.py bdist_msi

rem D:\aproje\nenra\mdb\dist\nenra2.exe
rem **** pause so we can see the exit codes
rem pause "done...hit a key to exit"
cd