import requests as r
import os
#from forex_python.converter import CurrencyRates


# Define your API key and location
API_KEY = '7df01151-e6eb-4cd2-9a39-d3ed4d361ba7'
URL = f'https://pro-api.coinmarketcap.com'
# Fetch crypto information
response = r.get(f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest", headers={ "X-CMC_PRO_API_KEY": API_KEY })
data = response.json()

#price = data["data"][0]["quote"]["USD"]["price"]
btc_change = data["data"][0]["quote"]["USD"]["percent_change_1h"]

#c = CurrencyRates()
#usd_to_aud = c.get_rate('USD', 'AUD')
#aud_price = round(price * usd_to_aud, 2)

os.system(f'sketchybar --set btc icon="" label="{round(btc_change, 2)}%"')
