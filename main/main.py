import alpaca_trade_api as tradeapi 
import requests
import config
import configEx
ORDER_URL = '{}/v2/orders'. format(config.ALPACA_API_BASE_URL)




def create_market_order():
    ticker = 'AAPL'
    qty = '2'
    side = 'buy'
    order_type = 'market'

    data = {
        'symbol': ticker,
        'qty': qty,
        'side': side,
        'type': order_type,
        'time_in_force': 'day'


    }

    r = requests.post(ORDER_URL, json = data, headers = configEx.HEADERS)
    return r.content
    

def create_limit_order():
    ticker = 'AAPL'
    qty = '2'
    side = 'buy'
    order_type = 'limit'
    limit_price = '140'

    data = {
        'symbol': ticker,
        'qty': qty,
        'side': side,
        'type': order_type,
        'time_in_force': 'day',
        'limit_price': limit_price
    }

    r = requests.post(ORDER_URL, json = data, headers = configEx.HEADERS)
    return r.content

def stock_menu(n):
    if(n == 1):
        print("Creating market order.....")
        create_market_order()
    elif(n == 2):
        print("Creating limit order....")
        create_limit_order()
    elif(n == 0):
        print("Return to menu")
        stock_menu(n)




if __name__ == "__main__":
    n = int(input("Welcome to Stock_Algo \n Select an option: \n 1.Create market order \n 2.Create limit order  \n Select option: " ))
    stock_menu(n)
    
    """
    print(create_market_order())
    print(create_limit_order())
    """