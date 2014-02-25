# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NAMIK ERDO?AN
#
# Created:     23.01.2014
# Copyright:   (c) NAMIK ERDO?AN 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import adodbapi
import MySQLdb

class Mmdb():
    def __init__(self):
        database = "D:\\dist\\datalar\\27012014.mdb"
        constr = 'Provider=Microsoft.Jet.OLEDB.4.0; Data Source=%s'  % database
        self.tablename = "satodeme"
        # connect to the database
        self.conn = adodbapi.connect(constr)
        # create a cursor
        self.cur = self.conn.cursor()
    def cek(self):
        # extract all the data
        sql = "select * from %s" % self.tablename
        self.cur.execute(sql)
        # show the result
        self.result = self.cur.fetchall()
        return self.result

    def kapat(self):
        self.cur.close()
        self.conn.close()



class Myddb():
    def __init__(self):
        # connect to the database
        self.conn = MySQLdb.connect('127.0.0.1', 'root', '654152', 'test', charset='utf8');


        # create a cursor
        self.cur = self.conn.cursor()
        self.cur.execute("SET NAMES UTF8")
        self.cur.execute("SET character_set_client=utf8")







    def cek( self , tablenam):
        self.tablename=tablenam
        # extract all the data
        sql = "select * from %s" % self.tablename
        self.cur.execute(sql)
        # show the result
        self.result = self.cur.fetchall()
        
        return self.result

    def cek1( self,sql,tablenam,colname):
        # extract all the data
        #sql = "select * from %s" % self.tablename
        sql=" '%"+ sql +"%'"
        print sql
        sql1="select * from "+tablenam+ " where "+colname+" like "+sql
        print sql1
        self.cur.execute(sql1)
        # show the result
        self.result = self.cur.fetchall()
        return self.result
    def cek2( self,sql,tablenam,colname):
        # extract all the data
        #sql = "select * from %s" % self.tablename
        #sql="'"+ sql +"'"
        print sql
        sql1="select * from "+tablenam+ " where "+colname+" = %s "
        print sql1
        self.cur.execute(sql1,sql)
        # show the result
        self.result = self.cur.fetchall()
        return self.result

    def sil( self,sql,tablenam,colname):
        # extract all the data
        #sql = "select * from %s" % self.tablename
        #sql="'"+ sql +"'"
        print sql
        sql1="delete from "+tablenam+ " where "+colname+" = %s "
        print sql1
        self.cur.execute(sql1,sql)
        # show the result
        self.result =  self.cur.lastrowid
        return self.result



    def kaydet( self,deger0,deger1,deger2):
        # extract all the data
        #sql = "select * from %s" % self.tablename
        #sql="'"+ sql +"'"
        
        sql1="insert into recete (menuid,hammaddeid,miktar) values (%s,%s,%s)"
        print sql1
        print self.cur.execute(sql1,(deger0,deger1,deger2))

        # show the result
        print "Auto Increment ID: %s" % self.cur.lastrowid
        self.result = self.cur.lastrowid
        
        return self.result

    def kapat(self):
        self.cur.close()
        self.conn.close()

