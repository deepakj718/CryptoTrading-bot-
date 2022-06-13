
from json.tool import main
from multiprocessing.spawn import _main
import websocket
import json
from constants import WEBSOCKET_URL


def on_open(ws):
    print('opened connection')
    
def on_close(ws):
    print('closed connection')

def on_message(ws,message):
    jsn_msg = json.loads(message)

    candle = jsn_msg['k'] # price data

    is_closed = candle['x'] #is the candle price closed
    print(candle)

    if is_closed:
        print(candle['c']) # closing price

ws = websocket.WebSocketApp(WEBSOCKET_URL, on_open = on_open, on_close = on_close, on_message = on_message )
ws.run_forever()

    

    


    

