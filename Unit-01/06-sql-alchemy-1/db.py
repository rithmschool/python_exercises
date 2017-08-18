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
def get_all_snacks():
	conn = connect()
	cur = conn.cursor()
	cur.execute("SELECT * FROM snacks")
	snacks = cur.fetchall()
	cur.close()
	conn.close()
	return snacks

def add_snack(name,kind):
	conn = connect()
	cur = conn.cursor()
	cur.execute("INSERT INTO snacks (name,kind) VALUES (%s,%s)", (name,kind))
	conn.commit()
	cur.close()
	conn.close()

def find_snack(id):
	conn = connect()
	cur = conn.cursor()
	cur.execute("SELECT * FROM snacks WHERE id=%s", [id])
	one_snack = cur.fetchone()
	cur.close()
	conn.close()
	return one_snack

def edit_snack(name, kind, id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE snacks SET name=(%s), kind=(%s) where id=(%s)", [name,kind,id])
    conn.commit()
    cur.close()
    conn.close()

def delete_snack(id):
	conn = connect()
	cur = conn.cursor()
	cur.execute("DELETE FROM snacks WHERE id=%s",[id])
	conn.commit()
	cur.close()
	conn.close()
	return delete_snack




