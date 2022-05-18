import psycopg2

def get_db_names() -> str:
    conn = psycopg2.connect("dbname=crypto user=postgres password=123321666traart")
    cur = conn.cursor()
    cur.execute("SELECT tablename FROM pg_catalog.pg_tables \
                 WHERE pg_tables.schemaname = 'public'")
    names = cur.fetchall()
    str_names = ''.join([name[0].upper() +'\n' for name in names])
    conn.commit()
    cur.close()
    conn.close()
    return str_names