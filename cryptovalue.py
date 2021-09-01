# -*- coding: utf-8 -*-
"""
Created on Wed Sep 01 15:08:45 2021

@author: GabrielNoeGomes
"""

import cryptocompare as cpt

while True:
    try:

        # Ask for the cryptocoins
        crypto = input('Crypto: ')
        crypto2 = input(f'{crypto} to?: ')

        # Get the value and return it
        cryptovalue = cpt.get_avg(crypto, currency=crypto2, exchange='Binance')
        print(cryptovalue['PRICE'])

    except:

        break
