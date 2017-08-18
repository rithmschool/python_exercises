import psycopg2
import psycopg2.extras

def connect():
    conn = psycopg2.connect("dbname=flask-sql-snacks-test")
    return conn

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS snacks (id serial PRIMARY KEY, name text, kind text);")
    # cur.execute("insert into snacks (name, kind) values (%s, %s)", ("apple", "fruit"))
    # cur.execute("insert into snacks (name, kind) values (%s, %s)", ("M&Ms", "chocolate"))
    conn.commit()
    connect().close()

def close():
    connect().close()

# Implement these methods!

def find_all_snacks():
    conn = connect()
    cur = conn.cursor()
    cur.execute("select * from snacks")
    snack_list = cur.fetchall()
    cur.close()
    conn.close()
    return snack_list

def create_snack(name, kind):
    conn = connect()
    cur = conn.cursor()
    cur.execute("insert into snacks (name, kind) values (%s, %s)", (name, kind))
    conn.commit()
    cur.close()
    conn.close()

def find_snack(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("select * from snacks where snacks.id = %s", (id,))
    snack = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return snack

def edit_snack(name, kind, id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("update snacks set name = %s, kind = %s where snacks.id = %s", (name, kind, id))
    conn.commit()
    cur.close()
    conn.close()

def remove_snack(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("delete from snacks where snacks.id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()