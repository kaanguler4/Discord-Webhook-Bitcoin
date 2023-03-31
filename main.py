from binance.client import Client
from time import sleep
from discord_webhook import DiscordWebhook
import requests

API_KEY = ''
SECRET_KEY = ''

client = Client(API_KEY, SECRET_KEY)
 
def live_price():
    price = client.get_symbol_ticker(symbol='BTCUSDT')
    print(f"Anlık Fiyat: {'BTCUSDT'}: {price['price']}")
    webhook_url = 'webhook url'
    # Mesajınızı oluşturun
    message = f"{'BTCUSDT'} fiyatı {price['price']} USDT"
    # Webhook'u post edin
    requests.post(webhook_url, data={"content": message})


while True:
    price = client.get_symbol_ticker(symbol='BTCUSDT')
    live_price()
    sleep(1000)
