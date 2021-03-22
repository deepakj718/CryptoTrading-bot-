import websocket, json, pprint, talib, numpy,

socket = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

RSI_period = 11
RSI_overbought = 84
RSI_oversold = 30
MACD_fastperiod= 12
MACD_slowperiod = 26
MACD_signalperiod = 9
trade_symbol = "ETHUSD"
quantity = .01

closing_prices= []
in_postion = False

def on_o(web_socket):
    print("opened connection")

def on_c(web_socket):
    print("closed connection")

def on_m(web_socket,message):
    global closing_prices
    print("recieved message")
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle_stick= json_message['k']
    is_closed = candle_stick['x']
    close = candle_stick['c']

    if is_closed:
        print("candle closed at {}".format(close))
        closing_prices.append(float(close))
        print('closes')
        print(closing_prices)
        
        if len(closing_prices) > RSI_period:
            np_arr = numpy.array(closing_prices)
            rsi = talib.RSI(np_arr,RSI_period)
            macd,macdsignal,macdhist = talib.MACD(np_arr,MACD_fastperiod,MACD_slowperiod,MACD_signalperiod)
            print("rsi calculated-")
            print(rsi)
            last_macd = macd[-1]
            last_macd_signal = macdsignal[-1]
            last_rsi= rsi[-1]
            print("the current rsi is {}".format(last_rsi))

            if last_rsi > RSI_overbought and last_macd - last_macd_signal < 0 and macd[-2] - macdsignal[-2] > 0:
                if in_postion:
                    print("SELL! COLLECTING THE BAG")
                else:
                    print("overbought but we don't have any")
            
            if last_rsi <RSI_oversold and last_macd - last_macd_signal > 0 and macd[-2] - macdsignal[-2] < 0:
                if in_postion:
                    print("oversold but already bought")
                else:
                    print("BUY! SHEESH BIG MONEY PLAYS")


ws = websocket.WebSocketApp(socket,on_open=on_o, on_close= on_c, on_message= on_m)
ws.run_forever()

