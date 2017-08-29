import psycopg2

def connect():
    c = psycopg2.connect("dbname=flask_sql")
    return c

