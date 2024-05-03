@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')
@app.route("/map")
def map():
    return render_template('map.html')