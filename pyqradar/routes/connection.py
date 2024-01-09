from pyqradar.utils.flask import socketio
from pyqradar.utils.logging import LoggerManager

logger = LoggerManager("root")


@socketio.on("connection")
def connection():
    logger.info("openned")
