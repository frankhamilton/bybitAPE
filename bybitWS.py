from time import sleep
from pybit import inverse_perpetual, usdt_perpetual

ws_inverseP = inverse_perpetual.WebSocket(
    test=False,
    ping_interval=30,  # the default is 30
    ping_timeout=10,  # the default is 10
    domain="bybit"  # the default is "bybit"
)

session_unauth = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com")


def queryAllSymbols():
    symbol_list = []
    removed = ["BTCUSDT", "USDCUSDT"]
    symbols = session_unauth.query_symbol()
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


def index_weights():
    return


while True:
    sleep(1)
