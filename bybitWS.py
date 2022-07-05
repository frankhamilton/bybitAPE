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
    removed = ["BTCUSDT", "USDCUSDT"]
    symbols = session_unauth.query_symbol()
    for item in symbols['result']:
        if item['name'] in removed:
            continue
        elif item['name'][-4:] == "USDT":
            symbol_list.append(item['name'])

    return symbol_list, handle_message(symbol_list)


def handle_message(msg):
    print(msg)


def liquidations():
    return


def index_weights():
    return

queryAllSymbols()

while True:
    sleep(1)

