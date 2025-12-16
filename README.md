This is a private FastAPI-based Currency Conversion API that fetches daily exchange rates from the European Central Bank (ECB) and stores them in a PostgreSQL database (hosted on Supabase). It allows conversion between currencies using the latest available rates.

🔹 How it works
Fetches daily ECB exchange rates (EUR base).

Stores or updates the rates in the Supabase/PostgreSQL database.

Exposes FastAPI endpoints:

Endpoint	Description
GET /rates	Fetches the latest rates and saves them to the database.
GET /convert?amount=<amount>&from_currency=<from>&to_currency=<to>	Converts an amount between two currencies using stored rates.

🔹 Access
The API is currently only exposed locally (127.0.0.1) for private use.

Others can use this API by cloning the repository and setting up their own .env file with database credentials.

The .env file is excluded from the repository to protect private database access.
