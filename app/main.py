from fastapi import FastAPI
from app.ecb import fetch_ecb_rates
from app.db import save_rates, get_conn

app = FastAPI()

@app.get("/rates")
def get_rates():
    # Fetch fresh ECB rates and save to DB
    rates = fetch_ecb_rates()
    save_rates(rates)
    return rates

@app.get("/convert")
def convert(amount: float, from_currency: str, to_currency: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT rate FROM currency_rates WHERE currency=%s", (from_currency,))
    from_rate = cur.fetchone()
    if not from_rate:
        return {"error": f"{from_currency} not found"}
    cur.execute("SELECT rate FROM currency_rates WHERE currency=%s", (to_currency,))
    to_rate = cur.fetchone()
    if not to_rate:
        return {"error": f"{to_currency} not found"}
    cur.close()
    conn.close()
    converted = amount / from_rate[0] * to_rate[0]
    return {"amount": amount, "from": from_currency, "to": to_currency, "converted": converted}