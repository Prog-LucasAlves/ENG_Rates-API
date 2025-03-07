import sqlite3
from datetime import datetime

import requests
from flask import Flask, jsonify, render_template
from flask_apscheduler import APScheduler
from flask_cors import CORS
from pydantic import BaseModel

from db import query_data

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)


@app.route("/exchange_rates")
def get_exchange_rates():
    data = query_data()
    return jsonify(data)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.add_job(id="Scheduled Task", func=home, trigger="interval", seconds=180)
    scheduler.start()

    app.run(host="0.0.0.0", port=5000, debug=True)
