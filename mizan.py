#!/usr/bin/env python
# -*- coding: utf-8 -*-

from modulemdb import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.rl_settings import *

toplam=0
toplam1=0

#  hammadde son fiyatları geçici  tabloya yazar
# CREATE TEMPORARY TABLE IF NOT EXISTS table2 AS (SELECT a.hamkod, a.`tarih`, a.`birimfiy`
# FROM  (
#     SELECT hamkod, MAX(tarih) as tarih, birimfiy
#     FROM cariay where fistipi=10
#     GROUP BY hamkod ) as x left join cariay a on a.tarih=x.tarih and a.hamkod=x.hamkod order by hamkod )

#tarih1="2018-09-01"
#tarih2="2018-09-30"

#tarih1="2018-10-01"
#tarih2="2018-10-31"

#tarih1="2018-11-01"
#tarih2="2018-11-30"

#tarih1="2019-01-01"
#tarih2="2019-01-31"

#tarih1="2019-02-01"
#tarih2="2019-02-28"

tarih1="2019-07-01"
tarih2="2019-07-31"

satis="SELECT departman,sum(adet),SUM(TUTAR) FROM bishop.CIRO  where tarih between %s  and %s and departman!=0 group by 1"
myddb = Myddb()
print myddb.cur.execute(satis,(tarih1,tarih2))
bul=myddb.cur.fetchall()
myddb.cur.execute("delete from bishop.genelrapor  where tarih between %s  and %s ",(tarih1,tarih2))
for row in bul:
    sql="insert into bishop.genelrapor (rkod,aciklama,miktar1,tarih) values (%s,%s,%s,%s)"
    myddb.cur.execute(sql,(row[0],"600.0"+str(row[0]),row[2],tarih2))
    myddb.conn.commit()
    toplam=toplam+row[2]

sql="insert into bishop.genelrapor (rkod,aciklama,miktar1,tarih) values (%s,%s,%s,%s)"
myddb.cur.execute(sql,(4,"600",toplam,tarih2))



sql="SELECT  muhkod,sum(round(birimfiy*miktar*(kdv+100)/100,2)) tutar FROM test.cariay  where tarih between %s  and %s  and fistipi=10 GROUP BY muhkod ORDER BY muhkod"
myddb.cur.execute(sql,(tarih1,tarih2))
bul=myddb.cur.fetchall()
elma=10
for row in bul:
    sql="insert into bishop.genelrapor (rkod,aciklama,miktar1,tarih) values (%s,%s,%s,%s)"
    myddb.cur.execute(sql,(elma,row[0],row[1], tarih2))
    elma=elma+1
    toplam1 = toplam1 + row[1]

sql="insert into bishop.genelrapor (rkod,aciklama,miktar1,tarih) values (%s,%s,%s,%s)"
myddb.cur.execute(sql,(99,"gider",toplam1,tarih2))
myddb.conn.commit()


sql="""

DROP TABLE IF EXISTS `genelrapor`;
CREATE TABLE `genelrapor` (
	`id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
	`rkod` INT(10) UNSIGNED NOT NULL,
	`aciklama` VARCHAR(50) NULL DEFAULT NULL,

"""

sqlx="select distinct tarih from bishop.genelrapor order by tarih "
myddb.cur.execute(sqlx)
bul=myddb.cur.fetchall()


sql1=""
for row in bul:
    sql1=sql1+" `"+str(row[0])+"` decimal(12,2) DEFAULT NULL, "


sql2="""
	`ktarih` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB


"""
myddb1=Myddb()
myddb1.cur.execute(sql+sql1+sql2)
myddb1.kapat()

sqlx="select distinct rkod,aciklama from bishop.genelrapor "
myddb.cur.execute(sqlx)
bul1=myddb.cur.fetchall()
myddb.conn.commit()
sqlx=""
for row in bul1:
    sqlx="insert into test.genelrapor (rkod,aciklama) values (%s,%s) "
    myddb.cur.execute(sqlx,(row[0],row[1]))


myddb.conn.commit()

for row in bul:
    print str(row[0])
    sql="select miktar1,rkod from bishop.genelrapor where tarih= %s"
    myddb.cur.execute(sql,(str(row[0]),))
    bul1=myddb.cur.fetchall()
    for row1 in bul1:
        print row1[0]
        sqlx = "update test.genelrapor set `" + str(row[0]) + "` = %s where `rkod` = %s "
        myddb.cur.execute(sqlx,(str(row1[0]),(row1[1])))

myddb.conn.commit()











