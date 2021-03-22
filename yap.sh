#!/bin/bash

echo "***** show başlıyor"
pyuic4-3.6  -x mainwindow.ui -o ui_mainwindow.py
pyuic4-3.6  -x recete.ui -o ui_recete.py
pyuic4-3.6  -x recete2.ui -o ui_recete2.py
pyuic4-3.6  -x fatura.ui -o ui_fatura.py
pyuic4-3.6  -x maliyet.ui -o ui_maliyet.py
echo "pyuic4-3.6  -x nenraweb.ui -o ui_nenraweb.py"
pyuic4-3.6  -x stok.ui -o ui_stok.py
pyuic4-3.6  -x masraf.ui -o ui_masraf.py
echo "***** build klasöründeki eski dosyalar siliniyor"

rm -rf build dist
python3.6 setup.py py2app --iconfile nenra.icns -d /Users/namikerdogan/Desktop
echo "********* open /Users/namikerdogan/Desktop/nenra.app"

./yoursway-create-dmg/create-dmg  --background Background.png --icon nenra3.app 180 210 --app-drop-link 360 200  --window-size 527 429 --icon-size 54 nenra.dmg /Users/namikerdogan/Desktop/nenra3.app

python3.6 uploadapp.py