from pyqradar.utils.flask import app, render_template


@app.route("/chests", methods=["GET"])
def chests():
    return render_template("chests.html")
