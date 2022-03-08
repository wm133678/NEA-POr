# Imports
"""import time
import requests
from pycoingecko import CoinGeckoAPI
from os.path import join
import os
import matplotlib.pyplot as plt
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType
import pandas as pd
import matplotlib.pyplot as mpimport numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
from tradingview_ta import *
import pprint
import json
import numpy


# Technical Analysis Module
def TAM():
    # Pair input
    pair = input("\nEnter given trading pair - E.g BTCUSDT\n")
    if pair == "":
        pair = "btcusdt"
        print(f"Chosen pair is {pair.upper()}")
    else:
        print(f"Chosen pair is {pair.upper()}")
    interval = input("\nEnter given time interval - E.g 1m, 15m, 1h, 1d\n")
    if interval == "":
        interval = "1h"
        print(f"Chosen interval is {interval}")
    else:
        print(f"Chosen interval is {interval}")

    asset = TA_Handler(
        symbol=pair,
        screener="CRYPTO",
        exchange="BINANCE",
        interval=interval,
        timeout=3.0
    )

    analysis = input(
        "\nWhat method of TA would you like to use first? (Full Analysis [f], Oscillators [o], Moving Averages [ma), Indicators [i] \n")

    # Oscillators Analysis
    if analysis == "o":
        # pprint.pprint(asset.get_analysis().oscillators)
        oscillators = asset.get_analysis().oscillators
        print("\nOscillators: ")
        AO = oscillators['COMPUTE']['AO']
        print("Awesome Oscillator: " + oscillators['COMPUTE']['AO'])
        ADX = oscillators['COMPUTE']['AO']
        print("Average Directional Index: " + oscillators['COMPUTE']['ADX'])
        BBP = oscillators['COMPUTE']['BBP']
        print("Bull/Bear Power: " + oscillators['COMPUTE']['BBP'])
        CCI = oscillators['COMPUTE']['CCI']
        print("Commodity Channel Index: " + oscillators['COMPUTE']['CCI'])
        MACD = oscillators['COMPUTE']['MACD']
        print("MACD: " + oscillators['COMPUTE']['MACD'])
        Mom = oscillators['COMPUTE']['Mom']
        print("Momentum: " + oscillators['COMPUTE']['Mom'])
        RSI = oscillators['COMPUTE']['RSI']
        print("RSI: " + oscillators['COMPUTE']['RSI'])
        StochRSI = oscillators['COMPUTE']['Stoch.RSI']
        print("Stoch RSI: " + oscillators['COMPUTE']['Stoch.RSI'])
        UO = oscillators['COMPUTE']['UO']
        print("Ultimate Oscillator: " + oscillators['COMPUTE']['UO'])
        WR = oscillators['COMPUTE']['W%R']
        print("Will's Percent Range: " + oscillators['COMPUTE']['W%R'])

        outlook = [AO, ADX, BBP, CCI, MACD, Mom, RSI, StochRSI, UO, WR]
        buy = outlook.count("BUY")
        neutral = outlook.count("NEUTRAL")
        sell = outlook.count("SELL")

        print(f"\nOscillators Buy Outlook: {buy}/10")
        print(f"Oscillators Neutral Outlook: {neutral}/10")
        print(f"Oscillators Sell Outlook: {sell}/10")

    elif analysis == "ma":
        # pprint.pprint(asset.get_analysis().moving_averages)
        jsonMA = asset.get_analysis().moving_averages
        Ichi = jsonMA['COMPUTE']['Ichimoku']
        print("\nIchimoku: " + jsonMA['COMPUTE']['Ichimoku'])

        print("\nExtended Moving Averages:")
        EMA10 = jsonMA['COMPUTE']['EMA10']
        print("EMA10: " + jsonMA['COMPUTE']['EMA10'])
        EMA20 = jsonMA['COMPUTE']['EMA20']
        print("EMA20: " + jsonMA['COMPUTE']['EMA20'])
        EMA30 = jsonMA['COMPUTE']['EMA30']
        print("EMA30: " + jsonMA['COMPUTE']['EMA30'])
        EMA50 = jsonMA['COMPUTE']['EMA50']
        print("EMA50: " + jsonMA['COMPUTE']['EMA50'])
        EMA100 = jsonMA['COMPUTE']['EMA100']
        print("EMA100: " + jsonMA['COMPUTE']['EMA100'])
        EMA200 = jsonMA['COMPUTE']['EMA200']
        print("EMA200: " + jsonMA['COMPUTE']['EMA200'])

        print("\nSimple Moving Averages:")
        SMA10 = jsonMA['COMPUTE']['SMA10']
        print("SMA10: " + jsonMA['COMPUTE']['SMA10'])
        SMA20 = jsonMA['COMPUTE']['SMA20']
        print("SMA20: " + jsonMA['COMPUTE']['SMA20'])
        SMA30 = jsonMA['COMPUTE']['SMA30']
        print("SMA30: " + jsonMA['COMPUTE']['SMA30'])
        SMA50 = jsonMA['COMPUTE']['SMA50']
        print("SMA50: " + jsonMA['COMPUTE']['SMA50'])
        SMA100 = jsonMA['COMPUTE']['SMA100']
        print("SMA100: " + jsonMA['COMPUTE']['SMA100'])
        SMA200 = jsonMA['COMPUTE']['SMA200']
        print("SMA200: " + jsonMA['COMPUTE']['SMA200'])
        emas = [EMA10, EMA20, EMA30, EMA50, EMA100, EMA200]
        buy = emas.count("BUY")
        neutral = emas.count("NEUTRAL")
        sell = emas.count("SELL")

        print(f"\nEMA Buy Outlook: {buy}/10")
        print(f"EMA Neutral Outlook: {neutral}/10")
        print(f"EMA Sell Outlook: {sell}/10")

        smas = [SMA10, SMA20, SMA30, SMA50, SMA100, SMA200]
        buy = smas.count("BUY")
        neutral = smas.count("NEUTRAL")
        sell = smas.count("SELL")

        print(f"\nEMA Buy Outlook: {buy}/10")
        print(f"EMA Neutral Outlook: {neutral}/10")
        print(f"EMA Sell Outlook: {sell}/10")

    elif analysis == "i":
        indiChoice = input("What indicator would you like to use first? (RSI, MACD)\n").lower()
        print("Unfinished")
        if indiChoice == "rsi":
            print(asset.get_analysis().indicators["RSI"])
        else:
            print("Unknown, try again.")
    elif analysis == "f":
        jsonMA = asset.get_analysis().moving_averages
        Ichi = jsonMA['COMPUTE']['Ichimoku']
        print("\nIchimoku: " + jsonMA['COMPUTE']['Ichimoku'])

        print("\nExtended Moving Averages:")
        EMA10 = jsonMA['COMPUTE']['EMA10']
        print("EMA10: " + jsonMA['COMPUTE']['EMA10'])
        EMA20 = jsonMA['COMPUTE']['EMA20']
        print("EMA20: " + jsonMA['COMPUTE']['EMA20'])
        EMA30 = jsonMA['COMPUTE']['EMA30']
        print("EMA30: " + jsonMA['COMPUTE']['EMA30'])
        EMA50 = jsonMA['COMPUTE']['EMA50']
        print("EMA50: " + jsonMA['COMPUTE']['EMA50'])
        EMA100 = jsonMA['COMPUTE']['EMA100']
        print("EMA100: " + jsonMA['COMPUTE']['EMA100'])
        EMA200 = jsonMA['COMPUTE']['EMA200']
        print("EMA200: " + jsonMA['COMPUTE']['EMA200'])

        print("\nSimple Moving Averages:")
        SMA10 = jsonMA['COMPUTE']['SMA10']
        print("SMA10: " + jsonMA['COMPUTE']['SMA10'])
        SMA20 = jsonMA['COMPUTE']['SMA20']
        print("SMA20: " + jsonMA['COMPUTE']['SMA20'])
        SMA30 = jsonMA['COMPUTE']['SMA30']
        print("SMA30: " + jsonMA['COMPUTE']['SMA30'])
        SMA50 = jsonMA['COMPUTE']['SMA50']
        print("SMA50: " + jsonMA['COMPUTE']['SMA50'])
        SMA100 = jsonMA['COMPUTE']['SMA100']
        print("SMA100: " + jsonMA['COMPUTE']['SMA100'])
        SMA200 = jsonMA['COMPUTE']['SMA200']
        print("SMA200: " + jsonMA['COMPUTE']['SMA200'])

        oscillators = asset.get_analysis().oscillators

        print("\nOscillators: ")
        AO = oscillators['COMPUTE']['AO']
        print("Awesome Oscillator: " + oscillators['COMPUTE']['AO'])
        ADX = oscillators['COMPUTE']['AO']
        print("Average Directional Index: " + oscillators['COMPUTE']['ADX'])
        BBP = oscillators['COMPUTE']['BBP']
        print("Bull/Bear Power: " + oscillators['COMPUTE']['BBP'])
        CCI = oscillators['COMPUTE']['CCI']
        print("Commodity Channel Index: " + oscillators['COMPUTE']['CCI'])
        MACD = oscillators['COMPUTE']['MACD']
        print("MACD: " + oscillators['COMPUTE']['MACD'])
        Mom = oscillators['COMPUTE']['Mom']
        print("Momentum: " + oscillators['COMPUTE']['Mom'])
        RSI = oscillators['COMPUTE']['RSI']
        print("RSI: " + oscillators['COMPUTE']['RSI'])
        StochRSI = oscillators['COMPUTE']['Stoch.RSI']
        print("Stoch RSI: " + oscillators['COMPUTE']['Stoch.RSI'])
        UO = oscillators['COMPUTE']['UO']
        print("Ultimate Oscillator: " + oscillators['COMPUTE']['UO'])
        WR = oscillators['COMPUTE']['W%R']
        print("Will's Percent Range: " + oscillators['COMPUTE']['W%R'])
        outlook = [AO, ADX, BBP, CCI, MACD, Mom, RSI, StochRSI, UO, WR]
        buy = outlook.count("BUY")
        neutral = outlook.count("NEUTRAL")
        sell = outlook.count("SELL")

        print(f"\nOscillators Buy Outlook: {buy}/10")
        print(f"Oscillators Neutral Outlook: {neutral}/10")
        print(f"Oscillators Sell Outlook: {sell}/10")

        emas = [EMA10, EMA20, EMA30, EMA50, EMA100, EMA200]
        buy = emas.count("BUY")
        neutral = emas.count("NEUTRAL")
        sell = emas.count("SELL")

        print(f"\nEMA Buy Outlook: {buy}/10")
        print(f"EMA Neutral Outlook: {neutral}/10")
        print(f"EMA Sell Outlook: {sell}/10")

        smas = [SMA10, SMA20, SMA30, SMA50, SMA100, SMA200]
        buy = smas.count("BUY")
        neutral = smas.count("NEUTRAL")
        sell = smas.count("SELL")

        print(f"\nEMA Buy Outlook: {buy}/10")
        print(f"EMA Neutral Outlook: {neutral}/10")
        print(f"EMA Sell Outlook: {sell}/10")

    else:
        print("Defaulting to all")
        jsonMA = asset.get_analysis().moving_averages
        Ichi = jsonMA['COMPUTE']['Ichimoku']
        print("\nIchimoku: " + jsonMA['COMPUTE']['Ichimoku'])

        print("\nExtended Moving Averages:")
        EMA10 = jsonMA['COMPUTE']['EMA10']
        print("EMA10: " + jsonMA['COMPUTE']['EMA10'])
        EMA20 = jsonMA['COMPUTE']['EMA20']
        print("EMA20: " + jsonMA['COMPUTE']['EMA20'])
        EMA30 = jsonMA['COMPUTE']['EMA30']
        print("EMA30: " + jsonMA['COMPUTE']['EMA30'])
        EMA50 = jsonMA['COMPUTE']['EMA50']
        print("EMA50: " + jsonMA['COMPUTE']['EMA50'])
        EMA100 = jsonMA['COMPUTE']['EMA100']
        print("EMA100: " + jsonMA['COMPUTE']['EMA100'])
        EMA200 = jsonMA['COMPUTE']['EMA200']
        print("EMA200: " + jsonMA['COMPUTE']['EMA200'])

        print("\nSimple Moving Averages:")
        SMA10 = jsonMA['COMPUTE']['SMA10']
        print("SMA10: " + jsonMA['COMPUTE']['SMA10'])
        SMA20 = jsonMA['COMPUTE']['SMA20']
        print("SMA20: " + jsonMA['COMPUTE']['SMA20'])
        SMA30 = jsonMA['COMPUTE']['SMA30']
        print("SMA30: " + jsonMA['COMPUTE']['SMA30'])
        SMA50 = jsonMA['COMPUTE']['SMA50']
        print("SMA50: " + jsonMA['COMPUTE']['SMA50'])
        SMA100 = jsonMA['COMPUTE']['SMA100']
        print("SMA100: " + jsonMA['COMPUTE']['SMA100'])
        SMA200 = jsonMA['COMPUTE']['SMA200']
        print("SMA200: " + jsonMA['COMPUTE']['SMA200'])

        oscillators = asset.get_analysis().oscillators
        print("\nOscillators: ")
        AO = oscillators['COMPUTE']['AO']
        print("Awesome Oscillator: " + oscillators['COMPUTE']['AO'])
        ADX = oscillators['COMPUTE']['AO']
        print("Average Directional Index: " + oscillators['COMPUTE']['ADX'])
        BBP = oscillators['COMPUTE']['BBP']
        print("Bull/Bear Power: " + oscillators['COMPUTE']['BBP'])
        CCI = oscillators['COMPUTE']['CCI']
        print("Commodity Channel Index: " + oscillators['COMPUTE']['CCI'])
        MACD = oscillators['COMPUTE']['MACD']
        print("MACD: " + oscillators['COMPUTE']['MACD'])
        Mom = oscillators['COMPUTE']['Mom']
        print("Momentum: " + oscillators['COMPUTE']['Mom'])
        RSI = oscillators['COMPUTE']['RSI']
        print("RSI: " + oscillators['COMPUTE']['RSI'])
        StochRSI = oscillators['COMPUTE']['Stoch.RSI']
        print("Stoch RSI: " + oscillators['COMPUTE']['Stoch.RSI'])
        UO = oscillators['COMPUTE']['UO']
        print("Ultimate Oscillator: " + oscillators['COMPUTE']['UO'])
        WR = oscillators['COMPUTE']['W%R']
        print("Will's Percent Range: " + oscillators['COMPUTE']['W%R'])


        outlook = [AO, ADX, BBP, CCI, MACD, Mom, RSI, StochRSI, UO, WR]
        buy = outlook.count("BUY")
        neutral = outlook.count("NEUTRAL")
        sell = outlook.count("SELL")

        print(f"\nOscillators Buy Outlook: {buy}/10")
        print(f"Oscillators Neutral Outlook: {neutral}/10")
        print(f"Oscillators Sell Outlook: {sell}/10")


        emas = [EMA10, EMA20, EMA30, EMA50, EMA100, EMA200]
        Ebuy = emas.count("BUY")
        Eneutral = emas.count("NEUTRAL")
        Esell = emas.count("SELL")

        print(f"\nEMA Buy Outlook: {Ebuy}/10")
        print(f"EMA Neutral Outlook: {Eneutral}/10")
        print(f"EMA Sell Outlook: {Esell}/10")

        smas = [SMA10, SMA20, SMA30, SMA50, SMA100, SMA200]
        Sbuy = smas.count("BUY")
        Sneutral = smas.count("NEUTRAL")
        Ssell = smas.count("SELL")

        print(f"\nSMA Buy Outlook: {Sbuy}/10")
        print(f"SMA Neutral Outlook: {Sneutral}/10")
        print(f"SMA Sell Outlook: {Ssell}/10")

        # % outlooks
        buyConfidence = buy / (buy + neutral + sell) * 100
        print(f"\nBuy Confidence Oscillators: {round(buyConfidence, 3)}%")
        SbuyConfidence = Sbuy / (Sbuy + Sneutral + Ssell) * 100
        print(f"Buy Confidence SMAs: {round(SbuyConfidence, 3)}%")
        EbuyConfidence = Ebuy / (Ebuy + Eneutral + Esell) * 100
        print(f"Buy Confidence SMAs: {round(EbuyConfidence, 3)}%")

        overallOutlook = (buyConfidence + SbuyConfidence + EbuyConfidence) / 3
        print(f"{pair.upper()} Overall Outlook: {round(overallOutlook, 3)}% Bullish")

# Trade Execution Module
def TEM():
    from dydx.client import Client
    import dydx.constants as consts
    import dydx.util as utils

    # create a new client with a private key (string or bytearray)
    client = Client(
        private_key='627e8bde99597fa66eb1048e301287b9caac74d149f25a6654a7e2ca6012204f',
        node='https://parity.expotrading.com'
    )
    # Get all trading pairs for dydx
    pairs = client.get_pairs()
# Whale Tracker Module


# Necessary Variable Assignment
INTERVAL_1_MINUTE = "1m"
INTERVAL_5_MINUTES = "5m"
INTERVAL_15_MINUTES = "15m"
INTERVAL_30_MINUTES = "30m"
INTERVAL_1_HOUR = "1h"
INTERVAL_2_HOURS = "2h"
INTERVAL_4_HOURS = "4h"
INTERVAL_1_DAY = "1d"
INTERVAL_1_WEEK = "1W"
INTERVAL_1_MONTH = "1M"

TEM()
