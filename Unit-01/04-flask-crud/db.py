import psycopg2

def connect():
  c = psycopg2.connect("dbname=aggregates_exercise user=theoryium")
  return c
  
def get_all_snacks():
  conn = connect()
  cur = conn.cursor()
  cur.execute("SELECT * FROM snacks ORDER BY id ASC")
  snacks = cur.fetchall()
  cur.close()
  conn.close()
  return snacks

def add_snack(name,kind):
	conn = connect()
	cur = conn.cursor()
	cur.execute ("INSERT INTO snacks (name,kind) VALUES (%s, %s)", (name,kind))
	conn.commit()
	cur.close()
	conn.close()

def find_snack(id):
	conn = connect()
	cur = conn.cursor()
	cur.execute ("SELECT * FROM snacks WHERE id=%s",(id,))
	snacks = cur.fetchone()
	conn.commit()
	cur.close()
	conn.close()
	return snacks

def update_snack(name,kind,snack_id):
	conn = connect()
	cur = conn.cursor()
	cur.execute ("UPDATE snacks SET name=%s , kind=%s WHERE id=%s", [name, kind, snack_id])
	conn.commit()
	cur.close()
	conn.close()

def delete_snack(id):
	conn = connect()
	cur = conn.cursor()
	cur.execute ("DELETE FROM snacks WHERE id=%s", (id,))
	conn.commit()
	cur.close()
	conn.close()