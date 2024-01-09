from pyqradar.utils.flask import app, render_template


@app.route("/ignorelist", methods=["GET"])
def ignorelist():
    return render_template("ignorelist.html")
