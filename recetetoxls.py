# -*- coding: utf-8 -*-

import sys
import time as ttim

from modulemdb import *
import re
import xlwt
import datetime

data=[]


class recetetoxls():
    def __init__(self):
        
        self.wb = xlwt.Workbook(encoding="utf-8")
        self.dest_filename = 'recete.xls'
        date_format = xlwt.XFStyle()
        date_format.num_format_str = u'#,##0.00₺'
        date_xf = xlwt.easyxf(num_format_str='DD/MM/YYYY')
        self.ws1 = self.wb.add_sheet("recete")
        self.style1 = xlwt.easyxf('pattern: pattern solid, fore_colour red;')

    
    def kontrol(girdi):
        girdi = str(girdi)
        ara = re.search("\.", girdi)
        if ara:
            print girdi
            derle = re.compile("\.")
            cikti = derle.sub(",", girdi)
            return float(cikti)
        return int(girdi)

    def yaz(self,kodd):
        # veritabanından bilgi çek

        bul2 = self.myddb.cek2(kodd, "recete", "menukod")
        i = len(bul2)
        j = 5

        aa = 0
        toplam = 0
        print bul2
        for row1 in bul2:
            item = str(row1[2])

            bul3 = self.myddb.cek2(item, "hammadde", "hamkod")
            print bul3

            item = str(bul3[0][1])
            self.ws1.write(self.satir,0,item + " ")

            item = bul3[0][2]
            self.ws1.write(self.satir, 1, item + " ")

            item = bul3[0][3]
            self.ws1.write(self.satir, 2, item + " ")
            item = int(row1[3])
            self.ws1.write(self.satir, 3, item )
            self.satir = self.satir + 1

        self.ws1.write(self.satir+1, 0, " ")
        self.satir+=2


    def goster(self):
        print "*toxls arayüzü açıldı"
        # some_date = QtCore.QDate(2011,4,22)
        self.myddb = Myddb()
        bul = self.myddb.cek("select * from hammadde where kategori=2 or kategori=3 order by hamkod")
        self.satir=0

        for row1 in bul:
            self.ws1.write(self.satir, 0, row1[1],self.style1)
            self.ws1.write(self.satir, 1, row1[2], self.style1)
            self.ws1.write(self.satir, 2, "", self.style1)
            self.ws1.write(self.satir, 3, "", self.style1)

            self.satir = self.satir + 1

            self.yaz(row1[1])


        self.wb.save(self.dest_filename)

        

if __name__ == "__main__":
    fatura1=recetetoxls()
    fatura1.goster()
