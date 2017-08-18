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
	cur.commit()
	cur.close()
	conn.close()

def find_all_snacks():
    pass

def create_snack(name, kind):
    pass

def find_snack(id):
    pass

def edit_snack(name, kind, id):
    pass
def remove_snack(id):
    pass