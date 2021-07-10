import json
import pprint
import numpy as np
import logging

from constants import (
    AUTH_CLIENT, WEBSOCKET_CLIENT, RSI_PERIOD, RSI_OVERBOUGHT, RSI_OVERSOLD, MACD_FASTPERIOD, MACD_SLOWPERIOD,
    MACD_SIGNALPERIOD, BUY_AMOUNT_IN_DOLLARS
)

class CryptoBot:

    def __init__(self, websocket_client):
        """
        :param websocket_client: websocket client for exchange
        """
        self.websocket_client = websocket_client

    def start_websocket_client(self):
        """
        Use the websocket_client to log realtime data
        """
        self.websocket_client.start()

    def close_websocket_client(self):
        """
        Close the socket
        """
        self.websocket_client.close()


if __name__ == "__main__":
    cb = CryptoBot(WEBSOCKET_CLIENT)
    cb.start_websocket_client()
    #cb.close_websocket_client()

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