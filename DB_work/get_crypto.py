import psycopg2
from aiogram import types
import csv

def save_crypto_data_in_file(message: types.Message):
        conn = psycopg2.connect("dbname=crypto user=postgres password=123321666traart")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {message.text}\
                    ORDER BY startat DESC")
        all_data = cur.fetchall()
        with open(f'files_to_send/{message.text}.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Дата начала промежутка', 'Цена на открытии','Самая низкая цена на промежутке','Самая высокая цена на промежутке','Цена закрытия','Количество сделок'])
            for line in all_data:
                    writer.writerow(line)
        conn.commit()
        cur.close()
        conn.close()