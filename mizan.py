# -*- coding: utf-8 -*-

from modulemdb import *
from datetime import datetime,timedelta
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.rl_settings import *


class mizan():
    def __init__(self,tarih1,tarih2):
        self.tarih1 = tarih1
        self.tarih2 = tarih2

    def last_day_of_month( self,any_day):
        any_day = datetime.strptime(any_day, '%Y-%m-%d').date()
        next_month = any_day.replace(day=28) + timedelta(days=4)  # this will never fail
        return next_month - timedelta(days=next_month.day)+ timedelta(days=1)

    def bishopgenel(self):
        self.toplam = 0
        self.toplam1 = 0

        satis="SELECT departman,sum(adet),SUM(TUTAR) FROM (select * from bishop.ciro union all select * from bishop.ciro1) as ciroo  where tarih between %s  and %s and departman!=0 group by 1"
        myddb = Myddb()
        print(myddb.cur.execute(satis, (self.tarih1, self.tarih2)))
        bul=myddb.cur.fetchall()
        myddb.cur.execute("delete from bishop.genelrapor  where tarih between %s  and %s ",(self.tarih1,self.tarih2))
        for row in bul:
            sql="insert into bishop.genelrapor (rkod,aciklama,miktar1,tarih) values (%s,%s,%s,%s)"
            myddb.cur.execute(sql,(row[0],"600.0"+str(row[0]),row[2],self.tarih2))
            myddb.conn.commit()
            self.toplam=self.toplam+row[2]

        sql="insert into bishop.genelrapor (rkod,aciklama,miktar1,tarih) values (%s,%s,%s,%s)"
        myddb.cur.execute(sql,(4,"600",self.toplam,self.tarih2))

        #Aybaşı sayım toplamı alınacak
        sayim="select sum(sayim.miktar*sayim.fiyat1) from TEST.sayim where date(tarih)= %s"
        myddb.cur.execute(sayim,[(self.tarih1)])
        bul=myddb.cur.fetchall()
        print(self.tarih1)
        sayim="select sum(sayim.miktar*sayim.fiyat1) from TEST.sayim where date(tarih)= %s"
        myddb.cur.execute(sayim,[(self.last_day_of_month(self.tarih1))])
        bul1=myddb.cur.fetchall()
        print(bul1)
        if bul1[0][0]!=None and bul[0][0]!=None:
            bul1 = bul[0][0] - bul1[0][0]
        else:
            bul1=0
        # Stok farkını dikkate almamak için aşağıdaki satırı kullanın
        bul1=0

        self.toplam1=self.toplam1+bul1
        myddb.cur.execute(sql, (9, "659." ,(bul1 ), self.tarih2))
        myddb.conn.commit()




        sql="SELECT  muhkod,sum(round(birimfiy*miktar*(kdv+100)/100,2)) tutar FROM test.cariay  where tarih between %s  and %s  and fistipi=10 GROUP BY muhkod ORDER BY muhkod"
        myddb.cur.execute(sql,(self.tarih1,self.tarih2))
        bul=myddb.cur.fetchall()
        elma=10
        for row in bul:
            sql="insert into bishop.genelrapor (rkod,aciklama,miktar1,tarih) values (%s,%s,%s,%s)"
            myddb.cur.execute(sql,(elma,row[0],row[1], self.tarih2))
            elma=elma+1
            self.toplam1 = self.toplam1 + row[1]

        sql="insert into bishop.genelrapor (rkod,aciklama,miktar1,tarih) values (%s,%s,%s,%s)"
        myddb.cur.execute(sql,(99,"770",self.toplam1,self.tarih2))






        myddb.conn.commit()

    def testgen(self):
        myddb = Myddb()

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
            print(str(row[0]))
            sql="select miktar1,rkod from bishop.genelrapor where tarih= %s"
            myddb.cur.execute(sql,(str(row[0]),))
            bul1=myddb.cur.fetchall()
            for row1 in bul1:
                print(row1[0])
                sqlx = "update test.genelrapor set `" + str(row[0]) + "` = %s where `rkod` = %s "
                myddb.cur.execute(sqlx,(str(row1[0]),(row1[1])))

        myddb.conn.commit()


if __name__ == '__main__':
    elma=mizan("2020-01-01","2020-01-31")
    elma.bishopgenel()
    elma.tarih1 = "2020-02-01"
    elma.tarih2 = "2020-02-29"
    elma.bishopgenel()
    """
    elma.tarih1 = "2019-01-01"
    elma.tarih2 = "2019-01-31"
    elma.bishopgenel()
    elma.tarih1 = "2019-02-01"
    elma.tarih2 = "2019-02-28"
    elma.bishopgenel()
    elma.tarih1="2019-03-01"
    elma.tarih2="2019-03-31"
    elma.bishopgenel()
    elma.tarih1="2019-04-01"
    elma.tarih2="2019-04-30"
    elma.bishopgenel()
    elma.tarih1="2019-05-01"
    elma.tarih2="2019-05-31"
    elma.bishopgenel()
    elma.tarih1="2019-06-01"
    elma.tarih2="2019-06-30"
    elma.bishopgenel()
    elma.tarih1="2019-07-01"
    elma.tarih2="2019-07-31"
    elma.bishopgenel()
    elma.tarih1="2019-08-01"
    elma.tarih2="2019-08-31"
    elma.bishopgenel()
    elma.tarih1="2019-09-01"
    elma.tarih2="2019-09-30"
    elma.bishopgenel()
    elma.tarih1 = "2019-10-01"
    elma.tarih2 = "2019-10-31"
    elma.bishopgenel()
    elma.tarih1 = "2019-11-01"
    elma.tarih2 = "2019-11-30"
    elma.bishopgenel()
    elma.tarih1 = "2019-12-01"
    elma.tarih2 = "2019-12-31"
    elma.bishopgenel()
    
    elma.tarih1 = "2018-01-01"
    elma.tarih2 = "2018-01-31"
    elma.bishopgenel()
    elma.tarih1 = "2018-02-01"
    elma.tarih2 = "2018-02-28"
    elma.bishopgenel()
    elma.tarih1 = "2018-03-01"
    elma.tarih2 = "2018-03-31"
    elma.bishopgenel()
    elma.tarih1 = "2018-04-01"
    elma.tarih2 = "2018-04-30"
    elma.bishopgenel()
    elma.tarih1 = "2018-05-01"
    elma.tarih2 = "2018-05-31"
    elma.bishopgenel()
    elma.tarih1 = "2018-06-01"
    elma.tarih2 = "2018-06-30"
    elma.bishopgenel()
    elma.tarih1 = "2018-07-01"
    elma.tarih2 = "2018-07-31"
    elma.bishopgenel()
    elma.tarih1 = "2018-08-01"
    elma.tarih2 = "2018-08-31"
    elma.bishopgenel()
    elma.tarih1 = "2018-09-01"
    elma.tarih2 = "2018-09-30"
    elma.bishopgenel()
    elma.tarih1 = "2018-10-01"
    elma.tarih2 = "2018-10-31"
    elma.bishopgenel()
    elma.tarih1 = "2018-11-01"
    elma.tarih2 = "2018-11-30"
    elma.bishopgenel()
    elma.tarih1 = "2018-12-01"
    elma.tarih2 = "2018-12-31"
    elma.bishopgenel()
"""
    elma.testgen()
    print("mizan güncelleme bitti")








