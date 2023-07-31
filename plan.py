from flask import Flask,render_template,Blueprint,request, redirect, url_for, session,flash

plan = Blueprint('planfilling',__name__)

@plan.route("/planfillingtype")
def Main_activity():
    return render_template ("htmlfile/plantype.html")