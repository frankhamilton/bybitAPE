from time import sleep
from pybit import usdt_perpetual


session_unauth = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com")

ws_linear = usdt_perpetual.WebSocket(
    test=False,
    ping_interval=30,  # the default is 30
    ping_timeout=10,  # the default is 10
    domain="bybit"  # the default is "bybit"
)


def queryAllSymbols():
    symbol_list = []
    symbols = session_unauth.query_symbol()
    for item in symbols['result']:
        symbol_list.append(item['name'])
    return symbol_list

def handle_message(msg):
    print(msg)




while True:
    sleep(1)

