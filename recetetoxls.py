# -*- coding: utf-8 -*-

import sys
import time as ttim

from modulemdb import Myddb
import re
import xlwt
import datetime
from xlrd import open_workbook

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
        self.style2 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow;')



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
        self.satir = 0

        for row1 in bul:
            self.ws1.write(self.satir, 0, row1[1], self.style1)
            self.ws1.write(self.satir, 1, row1[2], self.style1)
            self.ws1.write(self.satir, 2, "", self.style1)
            self.ws1.write(self.satir, 3, "", self.style1)

            self.satir = self.satir + 1

            self.yaz(row1[1])

    def goster1(self):
        print "*toxls arayüzü nnn açıldı"
        # some_date = QtCore.QDate(2011,4,22)
        self.myddb = Myddb()
        self.satir = 1
        self.elma = 1
        path = 'C:\\Users\\NAMIK\\Google Drive\\bishop\\PERSONEL\\ARCBISHOP1.xls'
        wb = open_workbook(path, formatting_info=True)
        sheet = wb.sheet_by_name("RECETE")
        for i in range(sheet.nrows):
            cell = sheet.cell(i, 0)  # The first cell
            print(cell.xf_index, sheet.cell(rowx=i, colx=0).value, str(sheet.cell(rowx=i, colx=1).value))
            bul = self.myddb.cek("select * from hammadde where hamad like '" + str(sheet.cell(rowx=i, colx=0).value) + "'")
            if cell.xf_index==23:
                self.ws1.write(self.satir, 0, str(sheet.cell(rowx=i, colx=0).value), self.style2)
            else:
                self.ws1.write(self.satir, 0, str(sheet.cell(rowx=i, colx=0).value), self.style1)
            self.satir=self.satir+1
            if len(bul)==0:
                self.ws1.write(self.satir-1, 5, str(self.elma), self.style1)
                self.elma=self.elma+1


            for row1 in bul:
                self.ws1.write(self.satir, 0, row1[1], self.style1)
                self.ws1.write(self.satir, 1, row1[2], self.style1)
                self.ws1.write(self.satir, 2, row1[3], self.style1)
                self.ws1.write(self.satir, 3, "", self.style1)

                self.satir = self.satir + 1

        self.wb.save(self.dest_filename)

        

if __name__ == "__main__":
    fatura1=recetetoxls()
   # fatura1.goster()
    fatura1.goster1()
