#!/bin/bash

echo "***** show başlıyor"
#python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py
python -m PyQt6.uic.pyuic  -x mainwindow.ui -o ui_mainwindow.py
python -m PyQt6.uic.pyuic  -x recete.ui -o ui_recete.py
python -m PyQt6.uic.pyuic  -x recete2.ui -o ui_recete2.py
python -m PyQt6.uic.pyuic  -x fatura.ui -o ui_fatura.py
python -m PyQt6.uic.pyuic  -x maliyet.ui -o ui_maliyet.py
python -m PyQt6.uic.pyuic  -x cari.ui -o ui_cari.py
python -m PyQt6.uic.pyuic  -x stok.ui -o ui_stok.py
python -m PyQt6.uic.pyuic  -x masraf.ui -o ui_masraf.py
python -m PyQt6.uic.pyuic  -x rapor.ui -o ui_rapor.py
echo "***** build klasöründeki eski dosyalar siliniyor"

rm -rf build dist
#python setup.py py2app --packages=PyQt5 --iconfile nenra.icns -d /Users/namikerdogan/Desktop
echo "********* open /Users/namikerdogan/Desktop/nenra.app"

#./yoursway-create-dmg/create-dmg  --background Background.png --icon nenra.icns 180 210 --app-drop-link 360 200  --window-size 527 429 --icon-size 54 nenra.dmg /Users/namikerdogan/Desktop/NENRA2.app
