# Currency Conversion API

## Description
A **private FastAPI-based Currency Conversion API** that:  
- Fetches daily exchange rates from the **European Central Bank (ECB)**  
- Stores them in a **PostgreSQL database** (hosted on Supabase)  
- Allows conversion between currencies using the latest rates  

---

## How it Works
1. Fetches **daily ECB exchange rates** (EUR base)  
2. Stores or updates the rates in the database  
3. Provides FastAPI endpoints:

| Endpoint | Description |
|----------|-------------|
| `GET /rates` | Fetches latest rates and saves to the database |
| `GET /convert?amount=<amount>&from_currency=<from>&to_currency=<to>` | Converts an amount between two currencies |

---

## Access
- Currently exposed **only locally** (`127.0.0.1`)  
- To use it elsewhere, **clone the repo** and set up your own `.env` with database credentials  
- `.env` is **excluded** to protect sensitive info  

---

## Example Usage

```python
import requests

response = requests.get(
    "http://127.0.0.1:8000/convert",
    params={"amount": 100, "from_currency": "USD", "to_currency": "EUR"}
)
print(response.json())
