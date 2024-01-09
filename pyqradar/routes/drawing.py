from pyqradar.utils.flask import app, render_template


@app.route("/drawing", methods=["GET"])
def drawing():
    return render_template("drawing.html")
