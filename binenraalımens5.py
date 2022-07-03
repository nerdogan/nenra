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

    def generateStochasticRSI(close_array, timeperiod):
        # 1) ilk aşama rsi değerini hesaplıyoruz.
        rsi = ta.RSI(close_array, timeperiod=timeperiod)

        # 2) ikinci aşamada rsi arrayinden sıfırları kaldırıyoruz.
        rsi = rsi[~np.isnan(rsi)]

        # 3) üçüncü aşamada ise ta-lib stoch metodunu uyguluyoruz.
        stochrsif, stochrsis = ta.STOCH(rsi, rsi, rsi, fastk_period=14, slowk_period=3, slowd_period=3)

        return stochrsif, stochrsis


    #    symbol = 'BTCUSDT'
    symbol = 'ENSUSDT'
    interval = '5m'
    limit = 90
    aldi = 0
    al = 0
    zaman = 3
    ordersayiold = 0
    yirmibes=999

    while True:
        ordersayi = len(connection.client.futures_get_open_orders(symbol=symbol))
        print(ordersayi)
        if ordersayi < 100:
            mesaj = (connection.client.futures_position_information(symbol='IOSTUSDT')[0]['unRealizedProfit'])

            mesaj = mesaj + " __ " + (connection.client.futures_account_balance()[1]['balance'])
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

        stochasticRsiF, stochasticRsiS = generateStochasticRSI(close_array, timeperiod=14)

        bbands = ta.BBANDS(close_array * 100, timeperiod=20, nbdevup=2,
                           nbdevdn=2,
                           # Moving average type: simple moving average here
                           matype=0)

        upper, middle, lower = [b / 100 for b in bbands]
        print(lower[-1], middle[-1], upper[-1])
        print(stochasticRsiF[-1], stochasticRsiS[-1])

        if 35 < stochasticRsiF[-1] :
            yirmibes=0



        if 25 > stochasticRsiF[-1] and yirmibes==0:
            os.system("C:\\Users\\bisho\\PycharmProjects\\nenra\\venv\\Scripts\\python.exe  C:\\Users\\bisho\\PycharmProjects\\nenra\\mdb\\msggonder.py '"  "hazırlan__*" + str(close[-1]) + "'")
            os.system("C:\\Users\\bisho\\PycharmProjects\\nenra\\venv\\Scripts\\python.exe  C:\\Users\\bisho\\PycharmProjects\\nenra\\mdb\\msggonderdilek.py '"  "hazırlan__*" + str(close[-1]) + "'")
            yirmibes=1

        if 11 > stochasticRsiF[-1] and yirmibes==1:
            order = connection.client.futures_create_order(symbol=symbol, positionSide='LONG', side='BUY',
                                                           type='MARKET', quantity='3')
            orderid = order['orderId']
            time.sleep(3)
            order = connection.client.futures_get_order(symbol=symbol, orderId=orderid)

            print(order)
            fiyat1 = float(order['avgPrice']) *1.003
            fiyat2 = float(order['avgPrice']) *1.004
            #fiyat3 = float(order1['avgPrice']) + 0.000300

            fiyat = float("{:.3f}".format(fiyat1))
            order = connection.client.futures_create_order(symbol=symbol, positionSide='LONG', side='SELL',
                                                           type='LIMIT', timeInForce='GTC', quantity='1',
                                                           price=fiyat)

            fiyat = float("{:.3f}".format(fiyat2))
            order = connection.client.futures_create_order(symbol=symbol, positionSide='LONG', side='SELL',
                                                           type='LIMIT', timeInForce='GTC', quantity='2',
                                                           price=fiyat)

            os.system("C:\\Users\\bisho\\PycharmProjects\\nenra\\venv\\Scripts\\python.exe  C:\\Users\\bisho\\PycharmProjects\\nenra\\mdb\\msggonder.py '"  "spot_al__*" + str(close[-1]) + "'")
            os.system("C:\\Users\\bisho\\PycharmProjects\\nenra\\venv\\Scripts\\python.exe  C:\\Users\\bisho\\PycharmProjects\\nenra\\mdb\\msggonderdilek.py '"  "grafiğe_bak_ona_göre_al__*" + str(close[-1]) + "'")
            yirmibes=2

        if 13 < stochasticRsiF[-1]:
            time.sleep(10)
            print("..........................1")
        else:
            pass
            #os.system("C:\\Users\\bisho\\PycharmProjects\\nenra\\venv\\Scripts\\python.exe  C:\\Users\\bisho\\PycharmProjects\\nenra\\mdb\\msggonder.py '"  "__*" + str(close[-1]) + "'")

        # Alım şartı
        if stochasticRsiF[-1] < stochasticRsiS[-1] < 12 and aldi < 1:
            print("al", low[-1])

            al = 1
            #os.system('afplay ' + './images/ses.wav -v 0.7')
            zaman = 0.5
        # alım emri
        if al == 1 and stochasticRsiF[-1] > stochasticRsiS[-1] and stochasticRsiF[-1] > 2 and stochasticRsiF[-1] < 12:

            order = connection.client.futures_create_order(symbol=symbol, positionSide='LONG', side='BUY',
                                                           type='MARKET', quantity='15')
            orderid = order['orderId']

            # print(orderid)
            al = 0
            aldi = aldi + 1
            time.sleep(3)
            order = connection.client.futures_get_order(symbol=symbol, orderId=orderid)

            print(order)
            fiyat1 = float(order['avgPrice']) *1.004
            fiyat2 = float(order['avgPrice']) *1.004
            #fiyat3 = float(order1['avgPrice']) + 0.000300

            fiyat = float("{:.3f}".format(fiyat1))
            order = connection.client.futures_create_order(symbol=symbol, positionSide='LONG', side='SELL',
                                                           type='LIMIT', timeInForce='GTC', quantity='10',
                                                           price=fiyat)

            fiyat = float("{:.3f}".format(fiyat2))
            order = connection.client.futures_create_order(symbol=symbol, positionSide='LONG', side='SELL',
                                                           type='LIMIT', timeInForce='GTC', quantity='5',
                                                           price=fiyat)

            zaman = 1.0
            os.system("C:\\Users\\bisho\\PycharmProjects\\nenra\\venv\\Scripts\\python.exe  C:\\Users\\bisho\\PycharmProjects\\nenra\\mdb\\msggonder.py '"  "__*" + str(fiyat) + "'")
            os.system("C:\\Users\\bisho\\PycharmProjects\\nenra\\venv\\Scripts\\python.exe  C:\\Users\\bisho\\PycharmProjects\\nenra\\mdb\\msggonderdilek.py '"  "__*" + str(fiyat) + "'")
            time.sleep(300)
            subprocess.Popen('C:\\Users\\bisho\\PycharmProjects\\nenra\\venv\\Scripts\\python.exe binenraalımens5.py', shell=True)
            print("çıktım")
            break
