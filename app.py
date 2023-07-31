from flask import Flask,render_template,Blueprint,request, redirect, url_for, session
import pymysql
from datetime import timedelta
from plan import *
from weeklyplan import *

app = Flask(__name__)

app.register_blueprint(plan)
app.register_blueprint(weeklyplan)

@app.route("/")
def Index():
    return render_template("htmlfile/index.html")


if __name__ == '__main__':
    app.run(threaded=True, debug = True, host = "0.0.0.0",port=1000)
