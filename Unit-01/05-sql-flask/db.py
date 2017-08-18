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
    connect().close()

def close():
    connect().close()

# Implement these methods!

def find_all_snacks():
    conn = connect()
    cur = conn.cursor()
    cur.execute("select * from snacks")
    snacks = cur.fetchall()
    cur.close()
    conn.close()
    return snacks

def create_snack(name, kind):
    conn = connect()
    cur = conn.cursor()
    cur.execute("insert into snacks (name, kind) values (%s, %s)", (name,kind))
    conn.commit()
    cur.close()
    conn.close()

def find_snack(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("select * from snacks where id=(%s)", (id,))
    found_snack = cur.fetchone()
    cur.close()
    conn.close()
    return found_snack

def edit_snack(id, name, kind):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE snacks SET name=(%s), kind=(%s) where id=(%s)", (name,kind,id))
    conn.commit()
    cur.close()
    conn.close()

def remove_snack(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("delete from snacks where id=(%s)", (id,))
    conn.commit()
    cur.close()
    conn.close()