from pyqradar.utils.flask import app, render_template


@app.route("/settings", methods=["GET"])
def settings():
    return render_template("settings.html")
