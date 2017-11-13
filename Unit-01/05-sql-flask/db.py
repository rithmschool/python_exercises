import psycopg2
import psycopg2.extras

def connect():
    conn = psycopg2.connect("dbname=flask-sql-snacks")
    return conn

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS snacks (id serial PRIMARY KEY, name text, kind text);")
    conn.commit()
    conn.close()

def close():
    connect().close()

# Implement these methods!

def find_all_snacks():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM snacks;')
    conn.commit()
    snacks = cur.fetchall()
    conn.close()
    return snacks


def create_snack(name, kind):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO snacks (name, kind) values (%s, %s)", (name, kind))
    conn.commit()
    conn.close()

def find_snack(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * from snacks WHERE id = %s;", (id,))
    conn.commit()
    snack = cur.fetchone()
    conn.close()
    return snack

def edit_snack(name, kind, id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE snacks SET name = %s, kind = %s WHERE id = %s;", (name, kind, id))
    conn.commit()
    conn.close()

def remove_snack(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM snacks WHERE id = %s", (id,))
    conn.commit()
    conn.close()