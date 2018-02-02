# -*- coding: utf-8 -*-
import sqlite3

baglanti = sqlite3.connect('HAMMADDELER.sqlite')
if (baglanti):
    print('Baglanti Başarılı!')
else:
    print('Bağlantı Başarısız!')

# baglanti kurulan veriyi seç.
veritabani_sec = baglanti.cursor()

# seçili olan veritabanın verileri okuyalım
#oku = veritabani_sec.execute("SELECT name FROM sqlite_master WHERE type='table';")
oku = veritabani_sec.execute("SELECT * FROM hammadde;")
for verileri_cek in oku.fetchall():
    print(verileri_cek)

baglanti.commit()
baglanti.close()
