from binance.client import Client
from binance.enums import *
import talib as ta
import numpy as np
import time, os, pprint, subprocess
from datetime import datetime
from decimal import Decimal as D, ROUND_DOWN, ROUND_UP
import decimal
import json
from threading import Thread
position = False


class BinanceConnection:
    def __init__(self, file):
        self.connect(file)

    """ Creates Binance client """

    def connect(self, file):
        lines = [line.rstrip('\n') for line in open(file)]
        key = lines[0]
        secret = lines[1]
        self.client = Client(key, secret)

    def islemgetir(self, symbol):
        mbl2 = self.client.get_margin_trades(symbol=symbol, isIsolated='TRUE')
        print(mbl2)
        toplam = 0.0
        toplamadet = 0.0
        toplam1 = 0.0
        toplamadet1 = 0.0
        toplamkom = 0.0
        for mbl in mbl2:
            tarih = datetime.fromtimestamp(mbl['time'] / 1000).strftime("%d-%m-%y %H:%M")
            if mbl['commissionAsset'] == 'BNB':
                toplamkom = toplamkom + (float(mbl['qty']) * float(mbl['price']) * 0.00075)
            else:
                toplamkom = toplamkom + (float(mbl['qty']) * float(mbl['price']))

            if mbl['isBuyer']:
                print(tarih, 'alım', mbl['price'], mbl['qty'], str((float(mbl['qty']) * float(mbl['price']))))
                toplam = (toplam + (float(mbl['qty']) * float(mbl['price'])))
                toplamadet = toplamadet + (float(mbl['qty']))

            else:
                print(tarih, 'satım', mbl['price'], mbl['qty'], str(float(mbl['qty']) * float(mbl['price'])))
                toplam1 = (toplam1 + (float(mbl['qty']) * float(mbl['price'])))
                toplamadet1 = toplamadet1 + float(mbl['qty'])

        kalan = (toplamadet - toplamadet1)
        print(toplam, toplam1, kalan * float(mbl['price']), (toplam - toplam1) - kalan * float(mbl['price']), kalan)
        print(toplamkom)

    def islemgetir1(self, symbol):
        mbl2 = self.client.get_my_trades(symbol=symbol)
        print(mbl2)
        toplam = 0.0
        toplamadet = 0.0
        toplam1 = 0.0
        toplamadet1 = 0.0
        toplamkom = 0.0
        for mbl in mbl2:
            tarih = datetime.fromtimestamp(mbl['time'] / 1000).strftime("%d-%m-%y %H:%M")
            if mbl['commissionAsset'] == 'BNB':
                toplamkom = toplamkom + (float(mbl['qty']) * float(mbl['price']) * 0.00075)
            else:
                toplamkom = toplamkom + (float(mbl['qty']) * float(mbl['price']) * 0.001)

            if mbl['isBuyer']:
                print(tarih, 'alım', mbl['price'], mbl['qty'], mbl['quoteQty'])
                toplam = (toplam + float(mbl['quoteQty']))
                toplamadet = toplamadet + float(mbl['qty'])

            else:
                print(tarih, 'satım', mbl['price'], mbl['qty'], mbl['quoteQty'])
                toplam1 = (toplam1 + float(mbl['quoteQty']))
                toplamadet1 = toplamadet1 + float(mbl['qty'])

        kalan = (toplamadet - toplamadet1)
        print(toplam, toplam1, kalan * float(mbl['price']), (toplam - toplam1) - kalan * float(mbl['price']), kalan)
        print(toplamkom)

    #        print(mbl['price'])

    def islemgetirfuture(self, symbol):
        mbl2 = self.client.futures_account_trades(startTime=1633903200000)

        print(mbl2)
        toplam = 0.0
        toplamadet = 0.0
        toplam1 = 0.0
        toplamadet1 = 0.0
        toplamkom = 0.0
        for mbl in mbl2:
            tarih = datetime.fromtimestamp(mbl['time'] / 1000).strftime("%d-%m-%y %H:%M")
            toplamkom = toplamkom + (float(mbl['commission']))

            if mbl['buyer']:
                print(tarih, 'alım', mbl['symbol'], mbl['price'], mbl['qty'], mbl['quoteQty'], mbl['commission'])
                toplam = (toplam + float(mbl['quoteQty']))
                toplamadet = toplamadet + float(mbl['qty'])

            else:
                print(tarih, 'satım', mbl['symbol'], mbl['price'], mbl['qty'], mbl['quoteQty'], mbl['commission'])
                toplam1 = (toplam1 + float(mbl['quoteQty']))
                toplamadet1 = toplamadet1 + float(mbl['qty'])

        kalan = (toplamadet - toplamadet1)
        print(toplam, toplam1, kalan * float(mbl['price']), (toplam - toplam1) - kalan * float(mbl['price']), kalan)
        print(toplamkom)


#        print(mbl['price'])
"""
            try:
                order=connection.client.futures_create_order(symbol='BTCUSDT',positionSide='LONG', side='SELL', type='MARKET', quantity='0.1')
            except:
                print("yok")

"""

if __name__ == '__main__':
    file = "credantial.txt"
    connection = BinanceConnection(file)
    client = connection.client
    symbol = 'SFPUSDT'


    # connection.islemgetirfuture('BTCUSDT')
    def ordercontrol(symbol):

        while True:
            # print('bşala',datetime.now().strftime("%H:%M:%S"))
            elma = client.futures_position_information()
            for i in elma:
                if float(i['entryPrice']) > 0:
                    # pprint.pprint(i)
                    giris = float(i['entryPrice'])
                    likit = giris * 0.99
                    satis = giris * 1.0016
                    simdi = float(i['markPrice'])
                    symbol = i['symbol']
                    miktar = float(i['positionAmt'])
                    # print(symbol,giris,likit,simdi,likit/giris,simdi/giris)
                    if likit > simdi and symbol != 'BTCUSDT':
                        order = connection.client.futures_create_order(symbol=symbol, positionSide='LONG', side='SELL',
                                                                       type='MARKET', quantity=miktar)
                        print('zararına sattım.........', symbol, giris, simdi)
                    if satis < simdi and symbol != 'BTCUSDT':
                        order = connection.client.futures_create_order(symbol=symbol, positionSide='LONG', side='SELL',
                                                                       type='MARKET', quantity=miktar)
                        print('karlı sattım................', symbol, giris, simdi)

            # print('bşala', datetime.now().strftime("%H:%M:%S"))
            time.sleep(1)


    thread = Thread(target=ordercontrol, args=(symbol,))
    thread.start()
