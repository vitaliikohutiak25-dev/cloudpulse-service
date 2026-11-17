import os
from flask import Flask, jsonify

app = Flask(__name__)
node_name = os.getenv("NODE_NAME", "Worker-Alpha")
env = os.getenv("APP_ENV", "Development")

@app.route("/")
def home():
    return jsonify({
        "service": "CloudPulse Telemetry API",
        "status": "ONLINE",
        "node": node_name,
        "environment": env
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
