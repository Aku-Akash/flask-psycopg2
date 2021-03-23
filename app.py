import os
from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
import psycopg2

from models import serialize

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
conn = psycopg2.connect("dbname=testing user=anish")
cur = conn.cursor()


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/add")
def add_test():
    id = request.args.get('id')
    name=request.args.get('name')
    score=request.args.get('score')
    try:
        cur.execute("""INSERT INTO tests (id,name,score) values (%s,%s,%s);""", (id,name,score))
        return "score added. score id={}".format(id)
    except Exception as e:
	    return(str(e))

@app.route("/getall")
def get_all():
    try:
        cur.execute("""SELECT * FROM tests;""")
        tests = cur.fetchall()
        return  jsonify([serialize(e) for e in tests])
    except Exception as e:
	    return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        cur.execute("""SELECT * FROM tests WHERE id = %s;""", (id_,))
        test = cur.fetchall()
        return serialize(test)
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':
    app.run()