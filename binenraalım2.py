from binance.client import Client
from binance.enums import *
import talib as ta
import numpy as np
import time, os, pprint, subprocess
from datetime import datetime
from decimal import Decimal as D, ROUND_DOWN, ROUND_UP
import decimal
import json

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
        mbl2 = self.client.futures_account_trades()

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
                print(tarih, 'alım', mbl['price'], mbl['qty'], mbl['quoteQty'], mbl['commission'])
                toplam = (toplam + float(mbl['quoteQty']))
                toplamadet = toplamadet + float(mbl['qty'])

            else:
                print(tarih, 'satım', mbl['price'], mbl['qty'], mbl['quoteQty'], mbl['commission'])
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


    def generateStochasticRSI(close_array, timeperiod):
        # 1) ilk aşama rsi değerini hesaplıyoruz.
        rsi = ta.RSI(close_array, timeperiod=timeperiod)

        # 2) ikinci aşamada rsi arrayinden sıfırları kaldırıyoruz.
        rsi = rsi[~np.isnan(rsi)]

        # 3) üçüncü aşamada ise ta-lib stoch metodunu uyguluyoruz.
        stochrsif, stochrsis = ta.STOCH(rsi, rsi, rsi, fastk_period=14, slowk_period=3, slowd_period=3)

        return stochrsif, stochrsis


    #    symbol = 'BTCUSDT'
    symbol = 'BTCUSDT'
    interval = '1m'
    limit = 60
    aldi = 0
    al = 0
    zaman = 1
    ordersayiold = 0

    while True:
        ordersayi = len(connection.client.futures_get_open_orders())
        print(ordersayi)
        if ordersayi < 12:
            break

        print("sipariş sayısı 7 emir verilemiyor")
        time.sleep(10)

    while True:
        # 10 saniye bekliyoruz. Sürekli sorgu göndermeye gerek yok.
        time.sleep(zaman)
        ordersayi = len(connection.client.futures_get_open_orders())
        if ordersayi < ordersayiold:
            mesaj = ("{:.2f}".format(
                float(connection.client.futures_position_information(symbol='BTCUSDT')[1]['unRealizedProfit']) + float(
                    connection.client.futures_position_information(symbol='BTCUSDT')[2]['unRealizedProfit'])))
            mesaj1 = mesaj + " * " + ("{:.2f}".format(float(connection.client.futures_account_balance()[1]['balance'])))
            os.system("python mdb/msggonder.py '" + mesaj1 + "  " + str(ordersayi) + " '")

        ordersayiold = ordersayi

        try:
            klines = connection.client.futures_klines(symbol=symbol, interval=interval, limit=limit)
        except Exception as exp:
            print("Kline hatası")
        open_time = [int(entry[0]) for entry in klines]
        open = [float(entry[1]) for entry in klines]
        high = [float(entry[2]) for entry in klines]
        low = [float(entry[3]) for entry in klines]
        close = [float(entry[4]) for entry in klines]

        new_time = [datetime.fromtimestamp(time / 1000) for time in open_time]

        new_time_x = [date.strftime("%d-%m-%y %H:%M") for date in new_time]

        last_closing_price = close[-1]

        previous_closing_price = close[-2]

        print('anlık kapanış ', last_closing_price, ',önceki kapanış ', previous_closing_price)

        close_array = np.asarray(close)

        close_finished = close_array[:-1]

        stochasticRsiF, stochasticRsiS = generateStochasticRSI(close_array, timeperiod=14)

        bbands = ta.BBANDS(close_array * 100, timeperiod=20, nbdevup=2,
                           nbdevdn=2,
                           # Moving average type: simple moving average here
                           matype=0)

        upper, middle, lower = [b / 100 for b in bbands]
        print(lower[-1], middle[-1], upper[-1])
        print(stochasticRsiF[-1], stochasticRsiS[-1])

        if stochasticRsiF[-1] < 83:
            time.sleep(5)
            print("..........................")

        # satım şartı
        if stochasticRsiF[-1] > stochasticRsiS[-1] > 94 and aldi < 1:
            print("sat", low[-1])
            al = 1
            os.system('afplay ' + './images/sat.wav -v 0.9')
            zaman = 0.3
        # alım emri
        if al == 1 and stochasticRsiF[-1] < stochasticRsiS[-1] and stochasticRsiF[-1] < 98 and stochasticRsiF[-1] > 84:
            order = connection.client.futures_create_order(symbol='BTCUSDT', positionSide='SHORT', side='SELL',
                                                           type='MARKET', quantity='0.004')
            orderid = order['orderId']
            print(orderid)
            al = 0
            aldi = aldi + 1
            time.sleep(3)
            order = connection.client.futures_get_order(symbol='BTCUSDT', orderId=orderid)
            fiyat1 = float(order['avgPrice']) - 80.0
            fiyat2 = float(order['avgPrice']) - 100.0
            # fiyat3=float(order['avgPrice'])-60.0

            fiyat = float("{:.2f}".format(fiyat1))
            print(fiyat)
            order = connection.client.futures_create_order(symbol='BTCUSDT', positionSide='SHORT', side='BUY',
                                                           type='LIMIT', timeInForce='GTC', quantity='0.002',
                                                           price=fiyat)

            fiyat = float("{:.2f}".format(fiyat2))
            order = connection.client.futures_create_order(symbol='BTCUSDT', positionSide='SHORT', side='BUY',
                                                           type='LIMIT', timeInForce='GTC', quantity='0.002',
                                                           price=fiyat)
            # print(fiyat1,fiyat2,fiyat)
            # fiyat= float("{:.2f}".format(fiyat3))
            # order = connection.client.futures_create_order(symbol='BTCUSDT', positionSide='SHORT',side='BUY', type='LIMIT',timeInForce='GTC', quantity='0.002',price=fiyat3)

            zaman = 1.0
            time.sleep(80)
            subprocess.Popen('python binenraalım2.py', shell=True)
            print("çıktım")
            break
