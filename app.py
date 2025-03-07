import sqlite3
from datetime import datetime

import requests
from flask import Flask, jsonify, render_template
from flask_apscheduler import APScheduler
from flask_cors import CORS
from pydantic import BaseModel

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)


class ExchangeRate(BaseModel):
    currency: str
    code: str
    codein: str
    name: str
    high: float
    low: float
    bid: float
    ask: float
    timestamp: str


def fetch_exchange_rates():
    url = "https://economia.awesomeapi.com.br/json/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao buscar dados da API")
        return None


def create_database():
    conn = sqlite3.connect("exchange_rates.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS exchange_rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency TEXT,
            code TEXT,
            codein TEXT,
            name TEXT,
            high REAL,
            low REAL,
            bid REAL,
            ask REAL,
            timestamp TEXT
        )
    """
    )
    conn.commit()
    conn.close()


def insert_data(data):
    conn = sqlite3.connect("exchange_rates.db")
    cursor = conn.cursor()
    for key, value in data.items():
        exchange_rate = ExchangeRate(
            currency=key,
            code=value["code"],
            codein=value["codein"],
            name=value["name"],
            high=float(value["high"]),
            low=float(value["low"]),
            bid=float(value["bid"]),
            ask=float(value["ask"]),
            timestamp=datetime.fromtimestamp(int(value["timestamp"])).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        )
        cursor.execute(
            """
            INSERT INTO exchange_rates (currency, code, codein, name, high,
            low, bid, ask, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                exchange_rate.currency,
                exchange_rate.code,
                exchange_rate.codein,
                exchange_rate.name,
                exchange_rate.high,
                exchange_rate.low,
                exchange_rate.bid,
                exchange_rate.ask,
                exchange_rate.timestamp,
            ),
        )
    conn.commit()
    conn.close()


def query_data():
    conn = sqlite3.connect("exchange_rates.db")
    cursor = conn.cursor()
    cursor.execute(
        """
                   SELECT * FROM exchange_rates ORDER BY timestamp
                   DESC LIMIT 10
                   """
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


@app.route("/exchange_rates")
def get_exchange_rates():
    data = query_data()
    return jsonify(data)


@app.route("/")
def home():
    return render_template("index.html")


def main():
    create_database()
    data = fetch_exchange_rates()
    if data:
        insert_data(data)
        print("Dados inseridos com sucesso!")
    else:
        print("Nenhum dado inserido.")


if __name__ == "__main__":
    main()
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.add_job(id="Scheduled Task", func=main, trigger="interval", seconds=180)
    scheduler.start()

    app.run(host="0.0.0.0", port=5000, debug=True)
