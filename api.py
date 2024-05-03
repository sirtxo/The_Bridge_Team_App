from flask import Flask, render_template
from src import covid_dash, hospitals_tb
@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')
@app.route("/map")
def map():
    return render_template('map.html')