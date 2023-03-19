import alpaca_trade_api as tradeapi
from alpaca_trade_api import REST
import config

api = tradeapi.REST(config.ALPACA_API_KEY, config.ALPACA_API_SECRET_KEY, config.ALPACA_API_BASE_URL)

class Account:
    def __init__(self) -> None:
        self.account_number = ''
        self.cash = ''
        self.equity = ''
        self.regt_buying_power = ""
    




def acc_details():
    a = api.get_account()
    acc_Serna.account_number = getattr(a, 'account_number')
    acc_Serna.cash = getattr(a, 'cash')
    acc_Serna.equity = getattr(a, 'equity')
    acc_Serna.regt_buying_power = getattr(a, 'regt_buying_power')




if __name__ == "__main__":
    acc_Serna = Account()
    acc_details()
    print(acc_Serna.account_number)