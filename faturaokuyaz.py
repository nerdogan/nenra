# -*- coding:utf-8 -*-
__author__ = 'NAMIK'

from PyQt4 import QtGui, QtCore
from fatura import Fatura
from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.compat import range
import re,sys
import xlwt
import datetime , time
from modulemdb import *
#import win32com.client  as win32

#excel = win32.gencache.EnsureDispatch('Excel.Application') #uses current instance of excel



app = QtGui.QApplication(sys.argv)
mydb=Myddb()
fname = unicode(QtGui.QFileDialog.getOpenFileName())
print fname
openfile=fname
"""
if fname.endswith("s"):
    fname=os.path.normpath(fname)
    wb=excel.Workbooks.Open(fname)
    wb.SaveAs(fname+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
    wb.Close()                               #FileFormat = 56 is for .xls extension
    openfile = fname + "x"
excel.Application.Quit()
"""

def kontrol(girdi):
        girdi = str(girdi)
        ara = re.search("\,", girdi)
        if ara:
            print girdi
            derle = re.compile("\,")
            cikti = derle.sub(".",girdi)
            return float(cikti)
        return int(girdi)

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)


wb =  xlwt.Workbook(encoding="utf-8")
dest_filename = '021020tdy.xls'
date_format = xlwt.XFStyle()
date_format.num_format_str = u'#,##0.00₺'
date_xf = xlwt.easyxf(num_format_str='DD/MM/YYYY')
style1 = xlwt.easyxf('pattern: pattern solid, fore_colour red;')

 # Filename line 'C:\\Users\\NAMIK\\Google Drive\\bishop\\PERSONEL\\fatura1.xlsx'


wb1 = load_workbook(openfile, read_only=True)
ws = wb1.active
aa=0
ab=0
data=[]
for row in ws.rows:
    ac=0
    ab=ab+1
    if ab==99999:
        break
    if ab < 2:
        continue

    print "   "
    for cell in row:
        if  ( ac==1 or    ac==2 or ac == 5 or ac==10):
            if cell.value==None:
                ab=99999
            deger1=cell.value
            data.append(deger1)
            print deger1

            print ab,ac+1
        if ( ac == 4  or ac == 6 or ac == 7 or ac == 11 ):
            if cell.value == None:
                ab = 99999
            deger1 = kontrol(cell.value)
            data.append(deger1)
            print deger1
            print ab, ac + 1

        if ( ac == 0):
            if cell.value == None:
                ab = 99999
                continue
            deger = datetime.datetime.strptime(str(cell.value), "%Y-%m-%d %H:%M:%S")

#            deger = datetime.datetime.strptime(str(cell.value), "%d%m%y")
            print deger

            t = deger.timetuple()
            deger2 = datetime.date(t[0],t[1],t[2])
            data.append(deger2)
            print  deger2



        ac=ac+1

elma="elma"
kesinti="243000000"
#kesinti="1890666868"
print len(data)
satir=3
satir1=1
satir2=1
dur=0.05

ws3 =wb.add_sheet("gelir")
ws4 =wb.add_sheet("gider")


fatura=Fatura()
fatura.goster()
for row in range((len(data)/9)):



    for col in range(1,2):
        if elma!=data[aa+1]:
            elma = data[aa + 1]
            dt=data[aa]


            fatura.lineEdit.setText('B')
            fatura.lineEdit_2.setText(elma)
            fatura.dateEdit.setDate(QtCore.QDate(dt.year, dt.month, dt.day))
            time.sleep(dur)
            if fatura.label_5.text()=="":
                fatura.lineEdit_3.setText("tdy")
                time.sleep(dur)
                fatura.slotfatura(0,0)
                time.sleep(dur)
                satir2=1
            else :
                aa=aa+9
                elma="elma"
                continue

        print 'xxxxxxxxxxxxxxxx', elma,aa


        print data[aa]

        satir2=satir2+1
        satir=satir2

        sql="insert into hambarkod (barkodno) values (%s)"
        try:
            mydb.cur.execute(sql,((data[aa+2]),))
            mydb.conn.commit()
        except MySQLdb.IntegrityError as e:
            if not e[0] == 1062:
                raise
            else:
                print u"Veritabanı girişi zaten yapılmış" , satir1
                satir1=satir1+1



        sql="select hamkod1,miktar from hambarkod where barkodno=%s"
        mydb.cur.execute(sql, ((data[aa + 2]),))
        bul=mydb.cur.fetchone()
        if bul:
            print bul
            fatura.lineEdit_3.setText(str(bul[0]))
            data[aa+3]=data[aa+3]*bul[1]



        time.sleep(dur)
        if fatura.tableWidget.rowCount()==0 or fatura.tableWidget.rowCount()>1:
            if data[aa+7]=="1":
                fatura.lineEdit_3.setText("yiyecek")
            if data[aa+7]=="8":
                fatura.lineEdit_3.setText("yiyecek")
            if data[aa+7]=="18":
                fatura.lineEdit_3.setText("temizlik")

        time.sleep(dur)

        fatura.slotfatura(0,0)

        time.sleep(dur)
        fatura.tableWidget_2.setItem((satir - 2), 3, QtGui.QTableWidgetItem(str(data[aa + 7])))
        if data[aa+4]=="KG" :
            data[aa + 3]=data[aa+3]*1000

        fatura.tableWidget_2.setItem((satir-2), 4, QtGui.QTableWidgetItem(str(data[aa+3])))
        fatura.tableWidget_2.setItem(satir-2, 6, QtGui.QTableWidgetItem(str(data[aa+6])))
        time.sleep(dur)
        fatura.slotfaturakaydet()
        aa=aa+1

        aa=aa+1

        aa=aa+1

        aa = aa + 1

        aa = aa + 1

        aa = aa + 1

        aa = aa + 1
        aa = aa + 1
        aa = aa + 1

print satir1, " tekrar var"
app.exec_()
deger=last_day_of_month(deger)
t = deger.timetuple()
deger2 = datetime.date(t[0], t[1], t[2])

wb.save(dest_filename)