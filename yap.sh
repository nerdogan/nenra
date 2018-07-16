#!/bin/bash

echo "***** show başlıyor"
pyuic4-2.7  -x mainwindow.ui -o ui_mainwindow.py
pyuic4-2.7  -x recete.ui -o ui_recete.py
pyuic4-2.7  -x recete2.ui -o ui_recete2.py
pyuic4-2.7  -x fatura.ui -o ui_fatura.py
pyuic4-2.7  -x maliyet.ui -o ui_maliyet.py
pyuic4-2.7  -x nenraweb.ui -o ui_nenraweb.py
pyuic4-2.7  -x stok.ui -o ui_stok.py

echo "***** build klasöründeki eski dosyalar siliniyor"

rm -rf build dist
python setup.py py2app --iconfile nenra.icns -d /Users/namikerdogan/Desktop
echo "********* open /Users/namikerdogan/Desktop/nenra.app"

./yoursway-create-dmg/create-dmg  --background Background.png --icon nenra.app 180 210 --app-drop-link 360 200  --window-size 527 429 --icon-size 54 nenra.dmg /Users/namikerdogan/Desktop/nenra.app

python2.7 uploadapp.py