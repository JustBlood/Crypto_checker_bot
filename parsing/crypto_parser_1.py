from datetime import datetime
import requests


def parser_1(crypto: str):
    now_time = int(datetime.timestamp(datetime.now()))

    URL = f"https://api2.bybit.com/public/linear/market/kline?symbol={crypto}&resolution=1&from={now_time - 600}&to={now_time}"

    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
        'accept': 'application/json'
    }

    response = requests.get(url=URL, headers=HEADERS)
    if response.status_code:
        list_data = response.json()

        if list_data['result'] is None:  # empty result
            URL = f"https://api2.bybit.com/v3/public/instrument/kline/list?symbol={crypto}&resolution=1&from={now_time - 600}&to={now_time}"
            list_data = requests.get(url=URL, headers=HEADERS).json()
            if list_data['result'] is None:
                return 'error empty result'
    else:
        return 'error status code'
    print(list_data['result']['list'][-1])
    return list_data['result']['list'][-1]