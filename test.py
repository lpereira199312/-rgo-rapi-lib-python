import rapi

apikey={sua api}
secretkey={sua secret key}

# metodo post get price for get snapshot in exchange binance for currency usdt 

rapi.keys(apikey,secretkey)
r = rapi.request("post","/api/v2/snapshots/cost",{'exchange':'binance','currency':'USDT'})
print(r.text)

# metodo get get assets in your watchlist

rapi.keys(apikey,secretkey)
r =rapi.request("get","/api/v2/watchlist/assets","")
print(r.text)
