from pyqradar.utils.flask import app


@app.route("/logout", methods=["GET"])
def logout():
    return "ok"
