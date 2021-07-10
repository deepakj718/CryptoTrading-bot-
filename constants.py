import os
import cbpro

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

# env vars
API_SECRET = os.environ.get("API_SECRET")
API_KEY = os.environ.get("API_KEY")
API_PASS = os.environ.get("API_PASS")
API_URL = os.environ.get("API_URL")
WEBSOCKET_URL = os.environ.get("WEBSOCKET_URL")
COIN_SYMBOL = os.environ.get("COIN_SYMBOL")

# coinbase client
AUTH_CLIENT = cbpro.AuthenticatedClient(
    key=API_KEY,
    b64secret=API_SECRET,
    passphrase=API_PASS,
    api_url=API_URL
)

CURRENCY = "USD"
WEBSOCKET_CLIENT  = cbpro.WebsocketClient(
    url=WEBSOCKET_URL,
    products=f"{COIN_SYMBOL}-{CURRENCY}",
    channels=["ticker"]
)

# algo parameters
RSI_PERIOD = 11
RSI_OVERBOUGHT = 84
RSI_OVERSOLD = 30
MACD_FASTPERIOD= 12
MACD_SLOWPERIOD = 26
MACD_SIGNALPERIOD = 9

# coinbase
BUY_AMOUNT_IN_DOLLARS = 20
