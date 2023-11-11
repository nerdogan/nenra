import threading
# import redis

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


    def zamangoster(zaman):

        new_time = datetime.fromtimestamp(zaman / 1000)
        new_time_x = new_time.strftime("%d-%m-%y %H:%M:%S")
        # print(new_time_x)
        return new_time_x


    def ortalamaspot(clientx, symbol, hane):

        elma = clientx.get_open_orders(symbol=symbol)
        print(elma)
        sira = 1
        adet = 0.0
        toplam = 0.0
        elma = clientx.get_open_orders(symbol=symbol)
        for sip in elma:
            if sip["side"] == "SELL":
                print(sira, sip['orderId'], sip['clientOrderId'], sip['origQty'], "  ", sip['price'])
                adet = adet + float(sip['origQty'])
                toplam = toplam + (float(sip['price']) * float(sip['origQty']))
                sira = sira + 1
                clientx.cancel_order(symbol=symbol, orderId=sip['orderId'])

        print(adet, toplam, toplam / adet)
        time.sleep(1)
        satis = toplam / adet
        fiyat = float("{:.{}f}".format(satis, hane))
        order = clientx.create_order(symbol=symbol, side='SELL',
                                     type='LIMIT', timeInForce='GTC',
                                     quantity=adet,
                                     price=fiyat)


    def ortalamalong(clientx, symbol, hane):
        elma = clientx.futures_position_information(symbol=symbol)
        miktar = (elma[1]['positionAmt'])
        satis = float(elma[1]['entryPrice']) * 1.0
        print(miktar, satis)

        adet = 0.0
        toplam = 0.0
        elma = clientx.futures_get_open_orders(symbol=symbol)
        for sip in elma:
            if sip["positionSide"] == "LONG" and sip['side'] == 'SELL':
                print(sip['origQty'], "  ", sip['price'])
                adet = adet + float(sip['origQty'])
                toplam = toplam + (float(sip['price']) * float(sip['origQty']))

        print(adet, toplam, toplam / adet)


    def ortalamashort(clientx, symbol, hane):
        elma = clientx.futures_position_information(symbol=symbol)
        miktar = (elma[2]['positionAmt'])
        satis = float(elma[2]['entryPrice']) * 1.0
        print(miktar, satis)

        adet = 0.0
        toplam = 0.0
        elma = clientx.futures_get_open_orders(symbol=symbol)
        for sip in elma:
            if sip["positionSide"] == "SHORT" and sip['side'] == 'BUY':
                print(sip['origQty'], "  ", sip['price'])
                adet = adet + float(sip['origQty'])
                toplam = toplam + (float(sip['price']) * float(sip['origQty']))

        print(adet, toplam, toplam / adet)


    def sipgetir(clientx, symbol):
        elma = clientx.futures_position_information(symbol=symbol)
        miktar = (elma[1]['positionAmt'])
        satis = float(elma[1]['entryPrice']) * 1.0
        print(miktar, satis)

        elma = clientx.futures_get_all_orders(symbol=symbol, limit=1000)
        print(elma)
        sira = 0
        adet = 0.0
        toplam = 0.0
        for sip in elma:
            if sip["positionSide"] == "LONG" and sip['side'] == 'BUY' and sip['origQty'] == '0.5':
                print(sira, zamangoster(sip['time']), zamangoster(sip['updateTime']), sip['origQty'], "  ",
                      sip['avgPrice'], sip['clientOrderId'])
                adet = adet + float(sip['origQty'])
                toplam = toplam + (float(sip['avgPrice']) * float(sip['origQty']))
                sira = sira + 1

        try:
            print(adet, toplam, toplam / adet)
        except:
            pass


    def ortalamasat(clientx, symbol, hane):
        elma = clientx.futures_position_information(symbol=symbol)
        miktar = (elma[1]['positionAmt'])
        satis = float(elma[1]['entryPrice']) * 1.0
        print(miktar, satis)

        adet = 0.0
        toplam = 0.0
        elma = clientx.futures_get_open_orders(symbol=symbol)
        for sip in elma:
            if sip["positionSide"] == "LONG" and sip['side'] == 'SELL':
                print(sip['origQty'], "  ", sip['price'])
                adet = adet + float(sip['origQty'])
                toplam = toplam + (float(sip['price']) * float(sip['origQty']))
                clientx.futures_cancel_order(symbol=symbol, orderId=sip['orderId'])

        print(adet, toplam, toplam / adet)
        time.sleep(1)
        satis = toplam / adet
        fiyat = float("{:.{}f}".format(satis, hane))

        order = clientx.futures_create_order(symbol=symbol, positionSide='LONG', side='SELL',
                                             type='LIMIT', timeInForce='GTC',
                                             quantity=adet,
                                             price=fiyat)


    def ortalamaal(clientx, symbol, hane):
        elma = clientx.futures_position_information(symbol=symbol)
        miktar = (elma[0]['positionAmt'])
        satis = float(elma[0]['entryPrice']) * 1.0
        print(miktar, satis)

        adet = 0.0
        toplam = 0.0
        elma = clientx.futures_get_open_orders(symbol=symbol)
        for sip in elma:
            if sip["positionSide"] == "SHORT" and sip['side'] == 'BUY':
                print(sip['origQty'], "  ", sip['price'])
                adet = adet + float(sip['origQty'])
                toplam = toplam + (float(sip['price']) * float(sip['origQty']))
                clientx.futures_cancel_order(symbol=symbol, orderId=sip['orderId'])

        print(adet, toplam, toplam / adet)
        time.sleep(1)
        satis = toplam / adet
        fiyat = float("{:.{}f}".format(satis, hane))

        order = clientx.futures_create_order(symbol=symbol, positionSide='SHORT', side='BUY',
                                             type='LIMIT', timeInForce='GTC',
                                             quantity=adet,
                                             price=fiyat)


    # ortalamasat(client,symbol = "PEOPLEUSDT",hane=5)
    # sipgetir(client, symbol="ENSUSDT")

    # ortalamalong(client, symbol="TOMOUSDT",hane=4)
    # ortalamashort(client1, symbol="ENSUSDT",hane=3)
    # ortalamaal(client, symbol="PEOPLEUSDT",hane=5)

    # ortalamaal(client, symbol="ENSUSDT",hane=3)
    ortalamasat(client, symbol="TOMOUSDT", hane=4)

    # ortalamaal(client, symbol="ENSUSDT",hane=3)
    # ortalamaal(client1, symbol="ENSUSDT",hane=3)

    # ortalama(client, symbol="ENSUSDT",hane=3)

    # ortalamaspot(client, symbol="FORUSDT",hane=5)

    pprint.pprint(client.futures_position_information(symbol="TOMOUSDT")[0]['unRealizedProfit'])

    pprint.pprint(client.futures_position_information(symbol="TOMOUSDT")[1]['unRealizedProfit'])

"""
    symbol="ENSUSDT"
    adet=1
    fiyat=13.90
    fiyat1=13.80

    order = client.futures_create_order(symbol=symbol, positionSide="LONG", side='SELL',
                                        type="TAKE_PROFIT", timeInForce='GTC',
                                         quantity=adet,stopPrice=fiyat,
                                         price=fiyat)
    pprint.pprint(order)

    order = client.futures_create_order(symbol=symbol, positionSide="LONG", side='SELL',
                                        type="STOP", timeInForce='GTC',
                                         quantity=adet,stopPrice=fiyat1,
                                         price=fiyat1)
    pprint.pprint(order)




    [{'avgPrice': '0',
  'clientOrderId': 'id5OA970GQFOGIYGstR1zj',
  'closePosition': False,
  'cumQuote': '0',
  'executedQty': '0',
  'orderId': 1755765162,
  'origQty': '2',
  'origType': 'LIMIT',
  'positionSide': 'LONG',
  'price': '9.859',
  'priceProtect': False,
  'reduceOnly': True,
  'side': 'SELL',
  'status': 'NEW',
  'stopPrice': '0',
  'symbol': 'ENSUSDT',
  'time': 1657999810869,
  'timeInForce': 'GTC',
  'type': 'LIMIT',
  'updateTime': 1657999810869,
  'workingType': 'CONTRACT_PRICE'},
"""
