from flask import Flask,render_template,Blueprint,request, redirect, url_for, session,flash,jsonify
from db import *
import pymysql
from datetime import datetime

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
def lookup_size():
    selected_date = request.args.get('selected_date')
    if request.method == "POST":
      prodLine = request.form['size']
    return redirect(url_for('weeklyplan.Weeklyplan',prodLine=prodLine,selected_date=selected_date))

@weeklyplan.route('/get_selected_date', methods=['POST'])
def get_selected_date():
    selected_date = request.form['selected_date']
    dateTimeObj = datetime.strptime(selected_date, "%m/%d/%Y")
    # Process the selected_date as needed, e.g., store in database or perform some calculation
    # You can also send a response back to the client if necessary
    response_data = {'message': 'Date received successfully!'}

    return redirect(url_for('weeklyplan.Weeklyplan',selected_date=dateTimeObj))

@weeklyplan.route("/weeklyplan")
def Weeklyplan():
        global productionLinegb
        productionLine = request.args.get('prodLine')
        datestart = request.args.get('selected_date')
        if productionLine is None :
            productionLine = productionLinegb
            if datestart is None:
              datestart = '2023-01-01'
              dateTimeObj = datetime.strptime(datestart, "%Y-%m-%d")
              datestart = dateTimeObj
        elif datestart is None:
            datestart = '2023-01-01'
            dateTimeObj = datetime.strptime(datestart, "%Y-%m-%d")
            datestart = dateTimeObj

        productionLinegb = productionLine
        server()
        cur = con.cursor()
        sql = "SELECT * FROM sku WHERE lineproduction =%s"
        cur.execute(sql,(productionLine))
        sku = cur.fetchall()
        plan = RecordPlan(datestart,productionLine)
        print(plan)
        return render_template ("planpage/weeklyplan.html",sku=sku,record_plan=plan)

def RecordPlan(date,productionline):
      line = productionline
      start_date = date
      server()
      cur = con.cursor()
      sql = "SELECT * FROM recordplan WHERE lineproduction =%s AND date_production =%s"
      cur.execute(sql,(line,start_date))
      plan = cur.fetchall()
      return plan