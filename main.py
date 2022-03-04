import time
from tradingview_ta import *

"""https://tvdb.brianthe.dev/"""

def Main():
    time.sleep(1)
    print("Which module would you like to run first? ")
    print("1. Technical Analysis Trading Bot")
    print("2. Ethereum Whale Wallet Tracker\n")
    moduleChoice = input("")
    if moduleChoice == "1":
        TradeBot()
    elif moduleChoice == "2":
        WhaleTracker()
    else:
        print("I'm unsure, try again")


def TradeBot():
    print("Welcome to the trading bot. ")
    # pair = input("What trading pair would you like to use? (E.g BTCUSDT)\n")
    pair = "BTCUSDT"
    """
    Available Intervals: 
    
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
    
    """


    BTC = TA_Handler(
        symbol="BTCUSDT",
        screener = "CRYPTO",
        exchange = "BINANCE",
        interval = Interval.INTERVAL_1_DAY,
        timeout = 3.0
    )

    generic = TA_Handler(
        symbol=pair,
        screener="CRYPTO",
        exchange="BINANCE",
        interval=Interval.INTERVAL_1_DAY,
        timeout=3.0
    )

    analysis = input("What method of TA would you like to use first? (Oscillators [o], Moving Averages [ma), Indicators [i]\n")
    analysis = "i"
    if analysis == "o":
        print(generic.get_analysis().oscillators)
    elif analysis == "ma":
        print(generic.get_analysis().moving_averages)
    elif analysis == "i":
        indiChoice = input("What indicator would you like to use first? (RSI, MACD)\n").lower()

        if indiChoice == "rsi":
            print(generic.get_analysis().indicators["RSI"])
        elif indiChoice == "macd":
            print(generic.get_analysis().indicators["MACD"])
        elif indiChoice == "supertrend":
            print(generic.get_analysis().indicators["supertrend"])
        else:
            print("Unknown, try again.")
    else:
        print("Unknown, try again")


    print(generic.get_analysis())
    print(generic.get_analysis().summary)
    """ Options:
    get_analysis().oscillators
    get_analysis().moving_averages
    get_analysis().indicators
    
    Useful indicators:

    Opening price: analysis.indicators["open"]
    Closing price: analysis.indicators["close"]
    Momentum: analysis.indicators["Mom"]
    RSI: analysis.indicators["RSI"]
    MACD: analysis.indicators["MACD.macd"]

    [
      "name",
      "change",
      "close",
      "change_abs",
      "high",
      "low",
      "volume",
      "Recommend.All",
      "exchange",
      "High.1M",
      "Low.1M",
      "Pivot.M.Camarilla.Middle",
      "Pivot.M.Camarilla.R1",
      "Pivot.M.Camarilla.R2",
      "Pivot.M.Camarilla.R3",
      "Pivot.M.Camarilla.S1",
      "Pivot.M.Camarilla.S2",
      "Pivot.M.Camarilla.S3",
      "Pivot.M.Classic.Middle",
      "Pivot.M.Classic.R1",
      "Pivot.M.Classic.R2",
      "Pivot.M.Classic.R3",
      "Pivot.M.Classic.S1",
      "Pivot.M.Classic.S2",
      "Pivot.M.Classic.S3",
      "Pivot.M.Demark.Middle",
      "Pivot.M.Demark.R1",
      "Pivot.M.Demark.S1",
      "Pivot.M.Fibonacci.Middle",
      "Pivot.M.Fibonacci.R1",
      "Pivot.M.Fibonacci.R2",
      "Pivot.M.Fibonacci.R3",
      "Pivot.M.Fibonacci.S1",
      "Pivot.M.Fibonacci.S2",
      "Pivot.M.Fibonacci.S3",
      "Pivot.M.Woodie.Middle",
      "Pivot.M.Woodie.R1",
      "Pivot.M.Woodie.R2",
      "Pivot.M.Woodie.R3",
      "Pivot.M.Woodie.S1",
      "Pivot.M.Woodie.S2",
      "Pivot.M.Woodie.S3",
      "High.3M",
      "Low.3M",
      "Perf.3M",
      "price_52_week_high",
      "price_52_week_low",
      "High.6M",
      "Low.6M",
      "Perf.6M",
      "High.All",
      "Low.All",
      "Aroon.Down",
      "Aroon.Up",
      "ADR",
      "ADX",
      "ATR",
      "average_volume_10d_calc",
      "Perf.Y",
      "Perf.YTD",
      "W.R",
      "average_volume_30d_calc",
      "average_volume_60d_calc",
      "average_volume_90d_calc",
      "AO",
      "BB.lower",
      "BB.upper",
      "BBPower",
      "change_abs|15",
      "change|15",
      "change_abs|60",
      "change|60",
      "change_abs|1",
      "change|1",
      "change_abs|240",
      "change|240",
      "change_abs|5",
      "change|5",
      "change_from_open_abs",
      "change_from_open",
      "CCI20",
      "DonchCh20.Lower",
      "DonchCh20.Upper",
      "EMA10",
      "EMA100",
      "EMA20",
      "EMA200",
      "EMA30",
      "EMA5",
      "EMA50",
      "gap",
      "HullMA9",
      "Ichimoku.BLine",
      "Ichimoku.CLine",
      "Ichimoku.Lead1",
      "Ichimoku.Lead2",
      "KltChnl.lower",
      "KltChnl.upper",
      "MACD.macd",
      "MACD.signal",
      "market_cap_calc",
      "Mom",
      "Perf.1M",
      "Recommend.MA",
      "open",
      "Recommend.Other",
      "P.SAR",
      "name",
      "ROC",
      "RSI",
      "RSI7",
      "relative_volume_10d_calc",
      "SMA10",
      "SMA100",
      "SMA20",
      "SMA200",
      "SMA30",
      "SMA5",
      "SMA50",
      "Stoch.D",
      "Stoch.K",
      "Stoch.RSI.K",
      "Stoch.RSI.D",
      "UO",
      "Volatility.D",
      "Volatility.M",
      "Volatility.W",
      "VWAP",
      "VWMA",
      "Perf.W",
      "description",
      "name",
      "type",
      "subtype",
      "update_mode",
      "pricescale",
      "minmov",
      "fractional",
      "minmove2",
      "ADX-DI[1]",
      "Rec.WR",
      "AO",
      "AO[1]",
      "close",
      "BB.lower",
      "BB.upper",
      "Rec.BBPower",
      "CCI20",
      "CCI20[1]",
      "EMA10",
      "EMA100",
      "EMA20",
      "EMA200",
      "EMA30",
      "EMA5",
      "EMA50",
      "Rec.HullMA9",
      "Rec.Ichimoku",
      "MACD.macd",
      "MACD.signal",
      "Mom",
      "Mom[1]",
      "P.SAR",
      "open",
      "Candle.AbandonedBaby.Bearish",
      "Candle.AbandonedBaby.Bullish",
      "Candle.Engulfing.Bearish",
      "Candle.Harami.Bearish",
      "Candle.Engulfing.Bullish",
      "Candle.Harami.Bullish",
      "Candle.Doji",
      "Candle.Doji.Dragonfly",
      "Candle.EveningStar",
      "Candle.Doji.Gravestone",
      "Candle.Hammer",
      "Candle.HangingMan",
      "Candle.InvertedHammer",
      "Candle.Kicking.Bearish",
      "Candle.Kicking.Bullish",
      "Candle.LongShadow.Lower",
      "Candle.LongShadow.Upper",
      "Candle.Marubozu.Black",
      "Candle.Marubozu.White",
      "Candle.MorningStar",
      "Candle.ShootingStar",
      "Candle.SpinningTop.Black",
      "Candle.SpinningTop.White",
      "Candle.3BlackCrows",
      "Candle.3WhiteSoldiers",
      "Candle.TriStar.Bearish",
      "Candle.TriStar.Bullish",
      "RSI",
      "RSI[1]",
      "RSI7",
      "RSI7[1]",
      "SMA10",
      "SMA100",
      "SMA20",
      "SMA200",
      "SMA30",
      "SMA5",
      "SMA50",
      "Stoch.K",
      "Stoch.D",
      "Stoch.K[1]",
      "Stoch.D[1]",
      "Rec.Stoch.RSI",
      "Rec.UO",
      "Rec.VWMA",
    ]

    print(BTC.get_analysis().summary)
    Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}
    analysis = get_multiple_analysis(screener="america", interval=Interval.INTERVAL_1_HOUR, symbols=["nasdaq:tsla", "nyse:docn", "nasdaq:aapl"])
    """

def rsi():
    pair = "BTCUSDT"
    print("fCalculating RSI for {pair}")
    generic = TA_Handler(
        symbol=pair,
        screener="CRYPTO",
        exchange="BINANCE",
        interval=Interval.INTERVAL_1_DAY,
        timeout=3.0
    )
    print(generic.get_analysis().indicators["RSI"])


def WhaleTracker():
    print("We trackin")



# TradeBot()
rsi()