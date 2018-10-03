#!/usr/bin/env python
# -*- coding: utf-8 -*-

from modulemdb import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.rl_settings import *

toplam=0

#  hammadde son fiyatları geçici  tabloya yazar
# CREATE TEMPORARY TABLE IF NOT EXISTS table2 AS (SELECT a.hamkod, a.`tarih`, a.`birimfiy`
# FROM  (
#     SELECT hamkod, MAX(tarih) as tarih, birimfiy
#     FROM cariay where fistipi=10
#     GROUP BY hamkod ) as x left join cariay a on a.tarih=x.tarih and a.hamkod=x.hamkod order by hamkod )

tarih1="2018-08-01"
tarih2="2018-08-31"

satis="SELECT departman,sum(adet),SUM(TUTAR) FROM bishop.CIRO  where tarih between %s  and %s and departman!=0 group by 1"
myddb = Myddb()
print myddb.cur.execute(satis,(tarih1,tarih2))
bul=myddb.cur.fetchall()

for row in bul:
    sql="insert into bishop.genelrapor (rkod,aciklama,miktar1,tarih) values (%s,%s,%s,%s)"
    myddb.cur.execute(sql,(row[0],"600.0"+str(row[0]),row[2],tarih2))
    myddb.conn.commit()
    toplam=toplam+row[2]

sql="insert into bishop.genelrapor (rkod,aciklama,miktar1,tarih) values (%s,%s,%s,%s)"
myddb.cur.execute(sql,(4,"600",toplam,tarih2))
myddb.conn.commit()


sql="SELECT  muhkod,sum(round(birimfiy*miktar*(kdv+100)/100,2)) tutar FROM test.cariay  where tarih between %s  and %s  and fistipi=10 GROUP BY muhkod ORDER BY muhkod"
myddb.cur.execute(sql,(tarih1,tarih2))
bul=myddb.cur.fetchall()
elma=10
for row in bul:
    sql="insert into bishop.genelrapor (rkod,aciklama,miktar1,tarih) values (%s,%s,%s,%s)"
    myddb.cur.execute(sql,(elma,row[0],row[1], tarih2))
    elma=elma+1

myddb.conn.commit()