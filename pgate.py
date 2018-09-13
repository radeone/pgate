import ccxt
# load config.py which has apikeys
import config

# initiate exchanges
kraken = ccxt.kraken(config.krakenApi)
bitmex = ccxt.bitmex(config.bitmexApi)
broker = ccxt._1broker(config.brokerApi)
# get kraken balances and add them together in usd
print("kraken:")
kbal = kraken.fetch_total_balance()
kusd = kbal['USD']+kbal['BTC']*kraken.fetch_ticker('BTC/USD')['last']
print(kusd)

# get bitmex balance in usd
print("bitmex:")
mexbal = bitmex.fetch_total_balance()
mexusd = mexbal['BTC']*bitmex.fetch_ticker('BTC/USD')['last']
print(mexusd)

# get 1broker balance in usd
print("1broker:")
brobal = broker.fetch_balance()
brousd = float(brobal['info']['net_worth'])*bitmex.fetch_ticker('BTC/USD')['last']
print(brousd)

# print grand total
total = kusd+mexusd+brousd
print("grand total:")
print(total)
