from flask import Flask,render_template,Blueprint,request, redirect, url_for, session,flash
from db import *
import pymysql


plan = Blueprint('planfilling',__name__)

def server():
    global con
    con = pymysql.connect(host = HOST,
                        user = USER,
                        password = PASS,
                        database = DATABASE,
                        charset='utf8mb4',
                        port=7741,
                        cursorclass=pymysql.cursors.DictCursor)

@plan.route("/planfillingtype")
def Main_activity():
        server()
        cur = con.cursor()
        sql = "SELECT * FROM sku"
        cur.execute(sql)
        test = cur.fetchall()
        # print(test)
        return render_template ("htmlfile/plantype.html")