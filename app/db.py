import os
import psycopg2
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # loads .env automatically
print(os.getenv("DB_HOST"))
print(os.getenv("DB_USER"))

def get_conn():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

def save_rates(rates: dict):
    conn = get_conn()
    cur = conn.cursor()
    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS currency_rates (
            currency TEXT PRIMARY KEY,
            rate FLOAT
        )
    """)
    # Upsert rates
    for currency, rate in rates.items():
        cur.execute("""
            INSERT INTO currency_rates(currency, rate)
            VALUES (%s, %s)
            ON CONFLICT(currency) DO UPDATE SET rate = EXCLUDED.rate
        """, (currency, rate))
    conn.commit()
    cur.close()
    conn.close()