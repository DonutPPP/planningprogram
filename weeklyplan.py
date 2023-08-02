from flask import Flask,render_template,Blueprint,request, redirect, url_for, session,flash
from db import *
import pymysql


weeklyplan = Blueprint('weeklyplan',__name__)

def server():
    global con
    con = pymysql.connect(host = HOST,
                        user = USER,
                        password = PASS,
                        database = DATABASE,
                        charset='utf8mb4',
                        port=7741,
                        cursorclass=pymysql.cursors.DictCursor)


@weeklyplan.route('/weeklyplanlookup',methods=['POST'])
def lookup():
    if request.method == "POST":
      prodLine = request.form['size']
      print(prodLine)
    print('in')



@weeklyplan.route("/weeklyplan")
def Weeklyplan():
        server()
        cur = con.cursor()
        sql = "SELECT * FROM sku"
        cur.execute(sql)
        sku = cur.fetchall()
        return render_template ("planpage/weeklyplan.html",sku=sku)