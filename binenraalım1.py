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


if __name__ == '__main__':
    file = "credantial.txt"
    connection = BinanceConnection(file)
    client = connection.client

    #    symbol = 'BTCUSDT'
    symbol = 'MBLUSDT'
    interval = '1m'
    limit = 360
    tekalim = 600
    fiyat = 0.017000
    # order = connection.client.order_limit_sell(symbol=symbol, quantity=1000, price='0.021650')
    # order = connection.client.order_limit_buy(symbol=symbol, quantity=500, price='0.021190')
    # print(order)

    """
    order=client.get_order(symbol=symbol, orderId=73449257)
    print(order['executedQty'],order['status'])
    if float(order['executedQty'])>450:
        print("alındı")
        order = client.order_limit_sell(symbol=symbol, quantity=500, price='0.022010')
        print(order)


    mbl1=client.get_open_orders(symbol=symbol)
    print(mbl1)
    for mbl in mbl1:
        [print(key, ':', value) for key, value in mbl.items()]
        


    order = connection.client.create_margin_order(
        symbol=symbol,
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=tekalim,
        price=fiyat,
        isIsolated='TRUE')
    print(order)
  #  orderid = order['orderId']
  
  
              try:
                order=connection.client.futures_create_order(symbol='BTCUSDT',positionSide='SHORT',  side='BUY', type='MARKET', quantity='0.1')
            except:
                print("yoooook")


"""
    # connection.islemgetir(symbol)
    # connection.islemgetir1(symbol)

    print("...........")


    #   os.system("python mdb/msggonder.py '"+order+"'")

    # orderid="81374407"
    # order=connection.client.get_order(symbol=symbol, orderId=orderid)
    # order = connection.client.get_margin_order(symbol=symbol, orderId=orderid,isIsolated='TRUE')
    # order = connection.client.get_margin_order(symbol=symbol, origClientOrderId=orderid, isIsolated='TRUE')
    # print(order)
    #  connection.client.futures_change_margin_type(symbol='BTCUSDT', marginType='ISOLATED')
    # connection.client.futures_change_leverage(symbol='BTCUSDT',leverage=10)
    # a=connection.client.futures_account_trades()
    # connection.islemgetirfuture('BTCUSDT')
    # order=connection.client.futures_create_order(symbol='BTCUSDT',side='BUY', type='MARKET', quantity='0.001')
    # order=connection.client.futures_get_order(symbol='BTCUSDT',orderId=18942304439)
    # print(order['avgPrice'])
    # pprint.pprint(order)
    # fiyat=str(float(order['avgPrice'])+20.0)
    # order = connection.client.futures_create_order(symbol='BTCUSDT', side='SELL', type='LIMIT',timeInForce='GTC', quantity='0.008',price=fiyat)

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
        if ordersayi < 30:
            mesaj = (connection.client.futures_position_information(symbol='BTCUSDT')[0]['unRealizedProfit'])

            mesaj = mesaj + " __ " + (connection.client.futures_account_balance()[1]['balance'])
            break

        print("sipariş sayısı 7 emir verilemiyor")
        time.sleep(30)

    while True:
        # 10 saniye bekliyoruz. Sürekli sorgu göndermeye gerek yok.
        time.sleep(zaman)

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

        if 20 < stochasticRsiF[-1]:
            time.sleep(5)
            print("..........................1")

        # Alım şartı
        if stochasticRsiF[-1] < stochasticRsiS[-1] < 11 and aldi < 1:
            print("al", low[-1])
            al = 1
            #os.system('afplay ' + './images/ses.wav -v 0.7')
            zaman = 0.3
        # alım emri
        if al == 1 and stochasticRsiF[-1] > stochasticRsiS[-1] and stochasticRsiF[-1] > 3 and stochasticRsiF[-1] < 17:

            order = connection.client.futures_create_order(symbol='BTCUSDT', positionSide='LONG', side='BUY',
                                                           type='MARKET', quantity='0.001')
            orderid = order['orderId']

            # print(orderid)
            al = 0
            aldi = aldi + 1
            time.sleep(3)
            order = connection.client.futures_get_order(symbol='BTCUSDT', orderId=orderid)

            print(order)
            fiyat1 = float(order['avgPrice']) + 65.0
            fiyat2 = float(order['avgPrice']) + 70.0
            #fiyat3 = float(order1['avgPrice']) + 0.000300

            fiyat = float("{:.2f}".format(fiyat1))
            order = connection.client.futures_create_order(symbol='BTCUSDT', positionSide='LONG', side='SELL',
                                                           type='LIMIT', timeInForce='GTC', quantity='0.001',
                                                           price=fiyat)

            #fiyat = float("{:.2f}".format(fiyat2))
            #order = connection.client.futures_create_order(symbol='BTCUSDT', positionSide='LONG', side='SELL', type='LIMIT', timeInForce='GTC', quantity='0.001',  price=fiyat)

            #fiyat= float("{:.6f}".format(fiyat3))
            #order = connection.client.futures_create_order(symbol='IOSTUSDT',positionSide='LONG', side='SELL', type='LIMIT',timeInForce='GTC', quantity='150',price=fiyat)

            zaman = 1.0
            # os.system("python mdb/msggonder.py '" + str(fiyat) + "  satacak...'")
            time.sleep(80)
            subprocess.Popen('C:\\Users\\bisho\\PycharmProjects\\nenra\\venv\\Scripts\\python.exe binenraalım1.py', shell=True)
            print("çıktım")
            break
