import rapi

apikey={your-api-key}
secretkey={your-secret-key}

# method POST get price for get snapshot in exchange binance for currency usdt 

rapi.keys(apikey,secretkey)
r = rapi.request("POST","/api/v2/snapshots/cost",{'exchange':'binance','currency':'USDT'})
print(r.text)

# method GET get assets in your watchlist

rapi.keys(apikey,secretkey)
r =rapi.request("GET","/api/v2/watchlist/assets","")
print(r.text)
