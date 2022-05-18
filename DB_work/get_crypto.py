import psycopg2
from aiogram import types


def save_crypto_data_in_file(message: types.Message):
        conn = psycopg2.connect("dbname=crypto user=postgres password=123321666traart")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {message.text}\
                    ORDER BY startat DESC")
        all_data = cur.fetchall()
        with open(rf'E:\prog\prog_py\parsing\Tolik_pr\files_to_send\{message.text}.txt', 'w', encoding='utf-8') as file:
            file.write(str(all_data))

        conn.commit()
        cur.close()
        conn.close()