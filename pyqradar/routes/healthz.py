from pyqradar.utils.flask import app


@app.route("/healthz", methods=["GET"])
def healthz():
    return "ok"
