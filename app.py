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
