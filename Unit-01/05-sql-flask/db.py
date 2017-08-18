import psycopg2
import psycopg2.extras

def connect():
    conn = psycopg2.connect("dbname=flask-sql-snacks-test")
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
    cur.execute("SELECT * FROM snacks order by id")
    snacks = cur.fetchall()
    connect().close()
    return snacks

def create_snack(name, kind):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO snacks (name, kind) VALUES (%s, %s)", (name, kind))
    conn.commit()
    connect().close()

def find_snack(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM snacks where snacks.id = %s", (id,))
    found_snack = cur.fetchone()
    connect().close()
    return found_snack

def edit_snack(name, kind, id):
    conn=connect()
    cur=conn.cursor()
    cur.execute("UPDATE snacks SET name = (%s), kind = (%s) where snacks.id = %s", (name,kind,id))
    conn.commit()
    connect().close()

    
def remove_snack(id):
    conn=connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM snacks WHERE id = %s", (id,))
    conn.commit()
    connect().close()



















