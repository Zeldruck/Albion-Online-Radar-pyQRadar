from waitress import serve

from pyqradar.utils.config import Config
from pyqradar.utils.flask import flask, socketio
from pyqradar.utils.logging import LoggerManager

logger = LoggerManager("root")

if __name__ == "__main__":
    host = Config.get("flask_host", "localhost")
    port = Config.get("flask_port", 5000)

    logger.info(f"Serving on http://{host}:{port}")
    socketio.run(flask, host=host, port=port, debug=False)
