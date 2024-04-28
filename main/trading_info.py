from tradingview_ta import TA_Handler, Interval

class Screener():

    def __init__(self, symbol, screener, exchange):
        self.symbol = symbol
        self.screener = screener
        self.exchange = exchange
        self.interval = None
        self.data = None
    

    def detailed_search(self):
        if "1m" in self.interval:
            self.data = TA_Handler(
                symbol=self.symbol,
                screener=self.screener,
                exchange=self.exchange,
                interval=Interval.INTERVAL_1_MINUTE
            )
        elif "5m" in self.interval:
            self.data = TA_Handler(
                symbol=self.symbol,
                screener=self.screener,
                exchange=self.exchange,
                interval=Interval.INTERVAL_5_MINUTES
            )

        if self.data:
            return self.data.get_analysis().summary
        else:
            return "No data available"
    

    def search(self):
        return f'''
        SUMMARY:
        Asset Picked: {self.symbol}
        Screener: {self.screener}
        Exchange Market: {self.exchange}
        Interval = {self.interval}
        '''

            
    
    def show_search(self):
        if self.data:
            return self.data.get_analysis().summary
        else:
            return "No data available"


def main():
    symbol = input("Choose the ticker for analysis: ")
    screener = input("Choose where the asset is being screened (america, crypto, etc.): ")
    exchange = input("Market of circulation: ")
    interval = input("Time of analysis (1m or 5m): ")

    asset = Screener(symbol, screener, exchange)
    asset.interval = interval
    asset.detailed_search()
    
    print(asset.search())
    print(asset.show_search())


if __name__ == "__main__":
   main()







'''
def run():
    tesla = TA_Handler(
        symbol = "TSLA",
        screener= "america",
        exchange= "NASDAQ",
        interval = Interval.INTERVAL_5_MINUTES
    )
    print(tesla.get_analysis().summary)
'''



if __name__ == "__main__":
   main()