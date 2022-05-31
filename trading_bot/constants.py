import os

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
"""AUTH_CLIENT = cbpro.AuthenticatedClient(
    key=API_KEY,
    b64secret=API_SECRET,
    passphrase=API_PASS,
    api_url=API_URL
)"""

# algo parameters
RSI_PERIOD = 6
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
MACD_FASTPERIOD= 12
MACD_SLOWPERIOD = 26
MACD_SIGNALPERIOD = 9

# coinbase
BUY_AMOUNT_IN_DOLLARS = 20
CURRENCY = "USD"
