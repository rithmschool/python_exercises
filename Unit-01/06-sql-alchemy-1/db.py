import psycopg2

def connect():
    c = psycopg2.connect("dbname=sql_alchemy_snacks")
    return c






def get_all_snacks():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM snacks;")
    snacks = cur.fetchall()
    cur.close()
    conn.close()
    return snacks


def find_snack_by_id(snack_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM snacks WHERE id=%s;",(snack_id,))
    snacks = cur.fetchone()
    cur.close()
    conn.close()
    return snacks

def remove_snack_by_id(snack_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM snacks WHERE id=%s;",(snack_id,))
    conn.commit()
    cur.close()
    conn.close()
    return None

def update_snack_by_id(snack_id, snack_name, snack_kind):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE snacks SET name=%s and kind=%s WHERE id=%s;",(snack_name, snack_kind, snack_id))
    conn.commit()
    cur.close()
    conn.close()
    return None