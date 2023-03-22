import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    # connect to db
    conn = psycopg2.connect("postgres://mayra_lab10_db_user:SgYmkCNREibUmkY09jyIj3aMpN5SI0AX@dpg-cgdj88prh17rd85us37g-a/mayra_lab10_db")
    # close db
    conn.close()
    return "Database Connection Successful"


@app.route('/db_create')
def creating():
    # connect to db
    conn = psycopg2.connect("postgres://mayra_lab10_db_user:SgYmkCNREibUmkY09jyIj3aMpN5SI0AX@dpg-cgdj88prh17rd85us37g-a/mayra_lab10_db")
    # cursor to execute SQL
    cur = conn.cursor()
    # create basketball table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    # commit changes from cursor to db
    conn.commit()
    # close db
    conn.close()
    return "Basketball Table Successfully Created"

