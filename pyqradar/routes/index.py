from pyqradar.utils.flask import app, render_template


@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def index():
    return render_template("index.html")
