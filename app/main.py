"""CloudPulse Telemetry API module."""
import os
import logging
from flask import Flask, Response, jsonify

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

NODE_NAME = os.getenv("NODE_NAME", "Worker-Alpha")
APP_ENV = os.getenv("APP_ENV", "Development")
APP_PORT = int(os.getenv("PORT", "5000"))


@app.route("/")
def get_status() -> Response:
    """Return service health status and runtime environment metadata."""
    logger.info("Health check requested on node: %s", NODE_NAME)
    return jsonify({
        "service": "CloudPulse Telemetry API",
        "status": "ONLINE",
        "node": NODE_NAME,
        "environment": APP_ENV,
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT)
