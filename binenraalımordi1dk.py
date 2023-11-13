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


if __name__ == '__main__':
    file = "credantial.txt"
    connection = BinanceConnection(file)
    client = connection.client
    file = "credantialMTUNCER.txt"
    connection1 = BinanceConnection(file)
    client1 = connection1.client
    file = "credantialemre.txt"
    connection2 = BinanceConnection(file)
    client2 = connection2.client


    def generateStochasticRSI(close_array, timeperiod):
        # 1) ilk aşama rsi değerini hesaplıyoruz.
        rsi = ta.RSI(close_array, timeperiod=timeperiod)

        # 2) ikinci aşamada rsi arrayinden sıfırları kaldırıyoruz.
        rsi = rsi[~np.isnan(rsi)]

        # 3) üçüncü aşamada ise ta-lib stoch metodunu uyguluyoruz.
        stochrsif, stochrsis = ta.STOCH(rsi, rsi, rsi, fastk_period=14, slowk_period=3, slowd_period=3)

        return stochrsif, stochrsis


    def generateRSI(close_array, timeperiod):
        # 1) ilk aşama rsi değerini hesaplıyoruz.
        rsi = ta.RSI(close_array, timeperiod=timeperiod)

        # 2) ikinci aşamada rsi arrayinden sıfırları kaldırıyoruz.
        rsi = rsi[~np.isnan(rsi)]

        return rsi


    #    symbol = 'BTCUSDT'
    symbol1 = 'TOMOUSDT'
    symbol = 'ORDIUSDT'
    interval = '1m'
    limit = 90
    aldi = 0
    al = 0
    zaman = 3
    ordersayiold = 0
    yirmibes = 999
    margin = 0
    mparayok1 = 0
    mparayokemre = 0

    while True:
        ordersayi = len(connection.client.futures_get_open_orders(symbol=symbol))
        print(ordersayi)
        if ordersayi < 10:
            mesaj = (connection.client.futures_position_information(symbol='ORDIUSDT')[0]['unRealizedProfit'])

            mesaj = mesaj + " __ " + (connection.client.futures_account_balance()[1]['balance'])
            print(mesaj)
            break

        print("sipariş sayısı 7 emir verilemiyor")
        time.sleep(30)

    while True:
        # 10 saniye bekliyoruz. Sürekli sorgu göndermeye gerek yok.
        time.sleep(zaman)
        print(time.strftime('%c'))

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

        RSI1 = generateRSI(close_array, timeperiod=14)

        bbands = ta.BBANDS(close_array * 100, timeperiod=20, nbdevup=2,
                           nbdevdn=2,
                           # Moving average type: simple moving average here
                           matype=0)

        upper, middle, lower = [b / 100 for b in bbands]
        print(lower[-1], middle[-1], upper[-1])
        print(RSI1[-1])

        if 40 > RSI1[-1]:
            order = connection.client.futures_create_order(symbol=symbol, positionSide='LONG', side='BUY',
                                                           type='MARKET', quantity='1')
            orderid = order['orderId']
            time.sleep(3)
            order = connection.client.futures_get_order(symbol=symbol, orderId=orderid)
            print(order)
            fiyatm = float(order['avgPrice'])
            fiyat1 = float(order['avgPrice']) * 1.010
            fiyat2 = float(order['avgPrice']) * 1.010
            # fiyat3 = float(order1['avgPrice']) + 0.000300

            fiyat = float("{:.3f}".format(fiyat1))
            order = connection.client.futures_create_order(symbol=symbol, positionSide='LONG', side='SELL',
                                                           type='LIMIT', timeInForce='GTC', quantity='1',
                                                           price=fiyat)

            os.system(
                "/Users/namikerdogan/PycharmProjects/nenra/venv/bin/python /Users/namikerdogan/PycharmProjects/nenra/mdb/msggonder.py '"  "spot_al__*" + str(
                    close[-1]) + "'")
            os.system(
                "/Users/namikerdogan/PycharmProjects/nenra/venv/bin/python /Users/namikerdogan/PycharmProjects/nenra/bgetfurures.py")

        if 40 > RSI1[-1]:
            time.sleep(57)
            print("..........................1")
        else:
            pass
            # os.system("C:\\Users\\bisho\\PycharmProjects\\nenra\\venv\\Scripts\\python.exe  C:\\Users\\bisho\\PycharmProjects\\nenra\\mdb\\msggonder.py '"  "__*" + str(close[-1]) + "'")
