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


@app.route('/db_insert')
def inserting():
    # connect to db
    conn = psycopg2.connect("postgres://mayra_lab10_db_user:SgYmkCNREibUmkY09jyIj3aMpN5SI0AX@dpg-cgdj88prh17rd85us37g-a/mayra_lab10_db")
    # cursor to execute SQL
    cur = conn.cursor()
    # insert basketball data
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    # commit changes from cursor to db
    conn.commit()
    # close db
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def selecting():
    # connect to db
    conn = psycopg2.connect("postgres://mayra_lab10_db_user:SgYmkCNREibUmkY09jyIj3aMpN5SI0AX@dpg-cgdj88prh17rd85us37g-a/mayra_lab10_db")
    # cursor to execute SQL
    cur = conn.cursor()
    # query data from db
    cur.execute('''
    SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    # close db
    conn.close()
    # put data in table
    response_string = ""
    response_string += "<table>"
    for player in records:
        response_string += "<tr>"
        for info in player:
            response_string += "<td>{}</td>".format(info)
        response_string += "</tr>"
    response_string += "</table>"
            
    return response_string


@app.route('/db_drop')
def dropping():
    # connect to db
    conn = psycopg2.connect("postgres://mayra_lab10_db_user:SgYmkCNREibUmkY09jyIj3aMpN5SI0AX@dpg-cgdj88prh17rd85us37g-a/mayra_lab10_db")
    # cursor to execute SQL
    cur = conn.cursor()
    # drop Basketball table for db
    cur.execute('''
    DROP TABLE Basketball;
    ''')
    # commit changes from cursor to db
    conn.commit()
    # close db
    conn.close()
    return "Basketball Table Successfully Dropped"