from saver_to_db import saver_to_db
from datetime import datetime
import time
import requests


def my_parser(crypto: str):
    now_time = int(datetime.timestamp(datetime.now()))
    i = 0
    if len(crypto) > 0:
        crypto = crypto.upper()
    else:
        return "Please, enter a name of crypto!"
    print(crypto)
    while True:
        URL = f"https://api2.bybit.com/public/linear/market/kline?symbol={crypto}&resolution=60&from={now_time - (125 * 24 * 60 * 60 * (i + 1))}&to={now_time - (125 * 24 * 60 * 60 * i)}"

        HEADERS = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
            'accept': 'application/json'
        }

        response = requests.get(url=URL, headers=HEADERS)
        if response.status_code:
            list_data = response.json()
            if list_data['result'] is None:  # empty result
                URL = f"https://api2.bybit.com/v3/public/instrument/kline/list?symbol={crypto}&resolution=60&from={now_time - (125 * 24 * 60 * 60 * (i + 1))}&to={now_time - (125 * 24 * 60 * 60 * i)}"
                list_data = requests.get(url=URL, headers=HEADERS).json()['result']['list']
            saver_to_db(crypto, list_data)
            if len(list_data) < 3000:
                break

        i += 1
        print(f"Processing...parsed {i} requests")
        time.sleep(3)
    return "success"
