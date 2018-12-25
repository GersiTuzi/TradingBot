import requests
import argparse

API_URL = "https://www.alphavantage.co/query"

symbols = ['USDCAD']
MagasinValeurRSI = []
MagasinDesPrix = []
tableauDeKeys = ["YGY55JABOFDU3X8Y","BXE971HIQ45YMM8Z","LU8TM1QS01RIUOL2", "OGPYF95QNH7KBH3B","29UFVVR0Q0SJUGRC"]


def api(symbol):
    temp1 = 0
    temp2 = 0

    data = {"function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": "30min",
            "datatype": "json",
            "apikey": "OGPYF95QNH7KBH3B"}
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
             "apikey": "29UFVVR0Q0SJUGRC"}
    response = requests.get(API_URL, data)
    data = response.json()
    a = (data['Technical Analysis: RSI'])
    keys = (a.keys())

    for key in keys:
        if temp1 < temp2:
            MagasinValeurRSI.append(a[key]['RSI'])
            temp1 += 1

    return MagasinValeurRSI, MagasinDesPrix


def tradingstrat():
    rsi, prix = api(symbols)
    pipValue= 0
    operation = 0
    initialPrice = 0
    finalPrice = 0
    #if rsi over 70 we sell and buy back when it reaches min value
    for key in rsi:
        if float(key) > 65:
            currentPrice = prix[rsi.index(key)]
            print("SELL ", currentPrice)
            if operation%2 == 0 :
                initialPrice = currentPrice
                print("initialPrice: ", initialPrice)
                operation += 1
        if float(key) < 52:
            currentPrice = prix[rsi.index(key)]
            print("BUY ", currentPrice)
            if operation%2 == 1:
                finalPrice = currentPrice
                operation+=1
                pipValue = float(initialPrice) - float(finalPrice)
                print("finalPrice: ", initialPrice)
                print("PIPVALUE = ", pipValue)

if __name__ == "  main  ":
    parser = argparse.ArgumentParser(prog="main.py")
    parser.add_argument('-a', required=False, help='argument qu on peut ajouter')
    args=parser.parse_args()

def writeInFile(file,string):
    file = open(file,'w',encoding="utf8")
    file.write(string)
    file.close()



tradingstrat()
tableauRSI, prix = api('USDJPY')
print(tableauRSI)
print(prix)










