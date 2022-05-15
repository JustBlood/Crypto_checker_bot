# "https://api.telegram.org/bot<token>/METHOD_NAME" 5359108498:AAG90AJWZOilNfkzUIuUT_oTdhd6hH5y8Ok
import requests

URL = "https://api.telegram.org/bot5359108498:AAG90AJWZOilNfkzUIuUT_oTdhd6hH5y8Ok"

response = requests.get(url=URL+'/getUpdates?offset=322623911')
print(response.json())
button1 = requests.get()
menu = requests.get(url=URL+'/sendMessage?reply_markup=ReplyKeyboardMarkup[]')