from pyqradar.utils.flask import app


@app.route("/", methods=["GET"])
def status():
    return ""
