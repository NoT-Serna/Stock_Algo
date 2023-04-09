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


menu =  """
    Welcome to Stock_Algo 

    1.Create market order 
    2.Create limit order

    Select an option:
    """
option = int(input(menu))

def stock_menu(option):
    while(option != -1):
        if(option == 1):
            print("Creating market order.....")
            create_market_order()
        elif(option == 2):
            print("Creating limit order....")
            create_limit_order()
        elif(option == 0):
            print("Return to menu")
        break





if __name__ == "__main__":
    stock_menu(option)