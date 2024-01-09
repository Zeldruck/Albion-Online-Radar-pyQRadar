from pyqradar.utils.flask import app, render_template


@app.route("/raw", methods=["GET"])
def raw():
    return render_template("raw.html")
