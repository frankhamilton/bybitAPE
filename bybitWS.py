from time import time, sleep
from pybit import inverse_perpetual, usdt_perpetual

ws_inverseP = inverse_perpetual.WebSocket(
    test=False,
    ping_interval=30,  # the default is 30
    ping_timeout=10,  # the default is 10
    domain="bybit"  # the default is "bybit"
)

ws_usdt_perpetual = usdt_perpetual.WebSocket(
    test=False,
    ping_interval=3000,  # the default is 30
    ping_timeout=10,  # the default is 10
    domain="bybit"  # the default is "bybit"
)

session_usdtP = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com")

session_inverseP = inverse_perpetual.HTTP(
    endpoint="https://api.bybit.com")


def queryAllSymbols():
    symbol_list = []
    removed = ["BTCUSDT", "USDCUSDT"]
    symbols = session_usdtP.query_symbol()
    for item in symbols['result']:
        if item['name'] in removed:
            continue
        elif item['name'][-4:] == "USDT":
            symbol_list.append(item['name'])

    return symbol_list


def liquidations():
    ws_inverseP.liquidation_stream(
        handle_liquidations, "BTCUSD"
    )


def BTCUSD_kline():
    ws_inverseP.kline_stream(
        handle_message, "BTCUSD", "5"
    )


def handle_message(msg):
    print(msg)


def handle_liquidations(msg):
    print(msg)


def index_beta():
    symbol_list = queryAllSymbols()
    previous_hour = int(time()) - (60 * 60)
    print(symbol_list)

    for item in symbol_list:
        response = session_usdtP.query_kline(symbol=item, interval=5, limit=12, from_time=previous_hour)


while True:
    sleep(1)
