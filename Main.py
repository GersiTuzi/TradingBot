
import requests



API_URL = "https://www.alphavantage.co/query" 
symbols = ['USDCAD']

for symbol in symbols:
        data = { "function": "TIME_SERIES_INTRADAY", 
        "symbol": symbol,
        "interval" : "30min",
        "datatype": "json", 
        "apikey": "BXE971HIQ45YMM8Z" }
        response = requests.get(API_URL, data) 
        data = response.json()
        print(symbol)
        a = (data['Time Series (30min)'])
        keys = (a.keys())
        for key in keys:
                print(a[key]['2. high'] + " " + a[key]['5. volume'])

