from datetime import datetime
import time
import psycopg2


def saver_to_db(crypto: str, *items):
    start = time.time()
    print(f"Начало записи данных в БД: {start}")
    conn = psycopg2.connect("dbname=crypto user=postgres password=123321666traart")
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {crypto}\
                (startAt timestamp PRIMARY KEY, open_ real, low_ real, high_ real, close_ real, count_of_deals bigint);")
    conn.commit()
    cur.close()
    conn.close()
    conn = psycopg2.connect("dbname=crypto user=postgres password=123321666traart")
    cur = conn.cursor()
    j = 0
    try:
        for item in items[0]:
            date_time = datetime.fromtimestamp(item['startAt'])
            open_ = item['open']
            low_ = item['low']
            high_ = item['high']
            close_ = item['close']
            count_of_deals = item['volume']
            try:
                cur.execute(f"INSERT INTO {crypto} VALUES (%s, %s, %s, %s, %s, %s)",
                            (date_time, open_, low_, high_, close_, count_of_deals))
                conn.commit()
            except Exception as ex:
                print(f"Данные не записались, ошибка: {ex}, зачения:{item}")
                break

            j += 1
            if j % 500 == 0:
                print(f"В базу занесено {j} строк")
        cur.close()
        conn.close()
        print("Успех!")
        print(f"Затраченное время: {time.time() - start}")
    except Exception as ex:
        print(f"Непредвиденная ошибка! {ex}")
