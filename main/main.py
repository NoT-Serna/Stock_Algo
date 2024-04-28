import requests
import config
import configEx
from trading_info import Screener

ORDER_URL = '{}/v2/orders'.format(config.ALPACA_API_BASE_URL)


class Stock():
    def __init__(self, ticker, qty, side, order_type):
        self.ticker = ticker
        self.qty = qty
        self.side = side
        self.order_type = order_type
        self.data = {}
        self.limit_price = ' '

    def stock_info(self):
        return f"""
            Name of the stock: {self.ticker} 
            Amount selected: {self.qty} 
            Operation selected: {self.side} 
            Type of order: {self.order_type}
        """

    def pick_stock(self, new_ticker):
        self.ticker = new_ticker

    def pick_qty(self, new_qty):
        self.qty = new_qty

    def pick_side(self, new_side):
        self.side = new_side

    def pick_order_type(self, new_order_type):
        self.order_type = new_order_type

    def set_limit_price(self, new_limit_price):
        self.limit_price = new_limit_price

    def stock_data(self):
        self.data = {
            'symbol': self.ticker,
            'qty': self.qty,
            'side': self.side,
            'type': self.order_type,
            'time_in_force': 'day'
        }
        return self.data

    def stock_limit_data(self):
        self.data = {
            'symbol': self.ticker,
            'qty': self.qty,
            'side': self.side,
            'type': self.order_type,
            'time_in_force': 'day',
            'limit_price': self.limit_price
        }
        return self.data

    def create_market_order(self):
        try:
            r = requests.post(ORDER_URL, json=self.data, headers=configEx.HEADERS)
            r.raise_for_status()  # Raise an exception for bad response status
            return r.content
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"

    def create_limit_order(self):
        try:
            self.stock_limit_data()
            r = requests.post(ORDER_URL, json=self.data, headers=configEx.HEADERS)
            r.raise_for_status()  # Raise an exception for bad response status
            return r.content
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"


def main():
    while True:
        menu = """
        Welcome to Stock_Algo 

        1. Create market order 
        2. Create limit order
        3. Analyze stocks
        0. Exit

        Select an option:
        """
        try:
            option = int(input(menu))

            if option == 0:
                print("Exiting...")
                break


            # Market Order
            if option == 1:
                ticker = input("Choose the stock you want to operate: ")
                side = input("Choose the operation you want to proceed with: ")
                qty = input("Choose the amount of stocks for the operation: ")
                m = 'market'
                stock = Stock(ticker, qty, side, m)
                data = stock.stock_data()
                print(data)
                print(stock.stock_info())
                c = input("Type ACCEPT to confirm operation: ")
                if c == "ACCEPT":
                    print("OPERATION COMPLETE !")
                    print(stock.create_market_order())
                else:
                    print("ERROR Try Again !")

            # Limit Order
            elif option == 2:
                ticker = input("Choose the stock you want to operate: ")
                side = input("Choose the operation you want to proceed with: ")
                qty = input("Choose the amount of stocks for the operation: ")
                l = 'limit'
                limit_stock = Stock(ticker, qty, side, l)
                set_price = input("Set the limit price in dollars: ")
                limit_stock.set_limit_price(set_price)
                data = limit_stock.stock_limit_data()

                print(data)
                print(limit_stock.stock_info())
                print_pricelimit = f"""
                    Price Limit: {set_price}$
                """
                print(print_pricelimit.upper())

                c = input("Type ACCEPT to confirm operation: ")
                if c == "ACCEPT":
                    print("OPERATION COMPLETE !")
                    print(limit_stock.create_limit_order())
                else:
                    print(" OPERATION ABORTED!")

            elif option == 3:
                print("Analyzing stocks...")
                symbol = input("Enter the ticker symbol for analysis: ")
                screener = input("Enter the screener (america, crypto, etc.): ")
                exchange = input("Enter the exchange market: ")
                interval = input("Enter the time interval for analysis (1m, 5m, 15m, 30m, 1h, 2h, 4h, 1d, 1W, 1M): ")

                asset = Screener(symbol, screener, exchange)
                asset.interval = interval
                analysis_summary = asset.detailed_search()
    
                print("Analysis Summary:")
                print(analysis_summary)


            else:
                print("Invalid option. Please select a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number for the option.")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
