import requests

API_URL = "https://www.alphavantage.co/query"

symbols = ['USDCAD']
MagasindeKeys = []
MagasinDesPrix = []
tableauDeKeys = ["YGY55JABOFDU3X8Y","BXE971HIQ45YMM8Z","LU8TM1QS01RIUOL2"]


def api(symbol):
    temp1 = 0
    temp2 = 0

    data = {"function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": "30min",
            "datatype": "json",
            "apikey": "YGY55JABOFDU3X8Y"}
    response = requests.get(API_URL, data)
    data = response.json()
    a = (data['Time Series (30min)'])
    keys = (a.keys())
    for key in keys:
        MagasinDesPrix.append(a[key]['2. high'])
        temp2 += 1

    data = {"function": "RSI",
             "symbol": symbol,
             "interval": "30min",
             "time_period": "30",
             "series_type": "close",
             "datatype": "json",
             "apikey": "YGY55JABOFDU3X8Y" }
    response = requests.get(API_URL, data)
    data = response.json()
    a = (data['Technical Analysis: RSI'])
    keys = (a.keys())

    for key in keys:
        if temp1 < temp2:
            MagasindeKeys.append(a[key]['RSI'])
            temp1 += 1

    return MagasindeKeys, MagasinDesPrix


def tradingstrat():
    rsi, prix = api(symbols)
    for key in rsi:
        if float(key) > 70:
            print("SELL ", prix[rsi.index(key)])
        if float(key) < 40:
            print("BUY ", prix[rsi.index(key)])

tradingstrat()
#tableau = api('USDJPY')
#print(tableau)










