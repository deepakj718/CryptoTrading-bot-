import json
import pprint
import numpy as np
import logging
import cbpro
import pandas as pd
import ta

from constants import (
    AUTH_CLIENT, RSI_PERIOD, RSI_OVERBOUGHT, RSI_OVERSOLD, MACD_FASTPERIOD, MACD_SLOWPERIOD,
    MACD_SIGNALPERIOD, BUY_AMOUNT_IN_DOLLARS, API_SECRET, API_KEY, API_PASS, API_URL, WEBSOCKET_URL, COIN_SYMBOL,
    CURRENCY
)

class CoinbaseProInteractor():
    """
    Utility class to interact with pro.coinbase.com
    """
    def __init__(self, auth_client) -> None:
        self.auth_client=auth_client
        
    def buy_coin(self, price, size, order_type, product_id):
        """
        Place a buy order on coinbase
        """
        self.auth_client.buy(
            price=price,
            size=size,
            order_type=order_type,
            product_id=product_id
        )
    def sell_coin(self, price, size, order_type, product_id):
        """
        Place a sell order on coinbase
        """
        self.auth_client.sell(
            price=price,
            size=size,
            order_type=order_type,
            product_id=product_id
        )
class WebsocketClientInteractor(cbpro.WebsocketClient):

    def on_open(self):
        self.url = WEBSOCKET_URL
        self.api_key=API_KEY
        self.api_secret=API_SECRET
        self.api_passphrase=API_PASS
        self.channels = ["ticker"]
        self.products = [f"{COIN_SYMBOL}-{CURRENCY}"]
        self.message_count = 0
        self.price_arr = []

    def on_message(self, msg):

        print(json.dumps(msg, indent=4, sort_keys=True))
        if 'price' in msg and 'type' in msg:
            self.price_arr.append(float(msg["price"]))

            if len(self.price_arr) > RSI_PERIOD:
                rsi = ta.momentum.rsi(
                    close =pd.Series(self.price_arr),
                    window= RSI_PERIOD,
                    fillna = True
                )
                """ macd = ta.trend.macd(
                    close = pd.Series(self.price_arr),
                    window_fast = MACD_FASTPERIOD,
                    window_slow = MACD_SLOWPERIOD,
                ) """
                macd_signal = ta.trend.macd_diff(
                    close = pd.Series(self.price_arr),
                    window_fast = MACD_FASTPERIOD,
                    window_slow = MACD_SLOWPERIOD,
                    window_sign = MACD_SIGNALPERIOD,
                    fillna = True
                )
                self.price_arr.clear()
                print(macd_signal)
                print(rsi)


            
            print(self.price_arr)
            self.message_count += 1

    def on_close(self):
        print("-- Goodbye! --")

if __name__ == "__main__":
    wsClient = WebsocketClientInteractor()
    wsClient.start()

"""
closing_prices= []



def on_m(web_socket,message):  #change all json messages from binance api to coinbase api
    global closing_prices
    in_postion = False
    print("recieved message")
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle_stick= json_message['k'] 
    is_closed = candle_stick['x']
    close = candle_stick['c']  #needs to be changed according to coinbase api

    if is_closed:
        print("candle closed at {}".format(close))
        closing_prices.append(float(close)) #append to array with prices
        print('closes')
        print(closing_prices)
        
        if len(closing_prices) > RSI_period: 
            np_arr = np.array(closing_prices)
            rsi = talib.RSI(np_arr,RSI_period) #calculate rsi
            macd,macdsignal,macdhist = talib.MACD(np_arr,MACD_fastperiod,MACD_slowperiod,MACD_signalperiod) #calculate MACD
            print("rsi calculated-")
            print(rsi)
            last_macd = macd[-1]
            last_macd_signal = macdsignal[-1]
            last_rsi= rsi[-1]
            print("the current rsi is {}".format(last_rsi))

            if last_rsi > RSI_overbought and last_macd - last_macd_signal < 0 and macd[-2] - macdsignal[-2] > 0: # check if it is overbought and over the rsi trigger and that macd line has crossed over 
                if in_postion:
                    print("SELL! COLLECTING THE BAG")
                    in_postion = False
                else:
                    print("overbought but we don't have any")
            
            if last_rsi <RSI_oversold and last_macd - last_macd_signal > 0 and macd[-2] - macdsignal[-2] < 0:  # check if it is oversold and under rsi trigger and that macd line has crossed under
                if in_postion:
                    print("oversold but already bought")
                else:
                    #input buy triggers 
                    print("BUY! SHEESH BIG MONEY PLAYS")
                    in_postion = True
                    


ws = websocket.WebSocketApp(socket,on_open=on_o, on_close= on_c, on_message= on_m)
ws.run_forever()
"""
