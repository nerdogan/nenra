# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        
# Purpose:
#
# Author:      NAMIK ERDOĞAN
#
# Created:     22.06.2016
# Copyright:   (c) NAMIK ERDOĞAN  2016
# Licence:     
#-------------------------------------------------------------------------------
import win32com.client  as win32

excel = win32.gencache.EnsureDispatch('Excel.Application') #uses current instance of excel

fname=r'C:\Users\NAMIK\PycharmProjects\nenra\02102017tdy.xls'
wb=excel.Workbooks.Open(fname)
wb.SaveAs(fname+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
wb.Close()                               #FileFormat = 56 is for .xls extension
excel.Application.Quit()