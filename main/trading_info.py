from tradingview_ta import TA_Handler, Interval, Exchange


class Screener():

    def __init__(self, symbol, screener, exchange):
        self.symbol = symbol
        self.screener = screener
        self.exchange = exchange
        self.interval = Interval
        self.data = ()

    

    def detailed_search(self):
        if "1m" in self.interval:
            self.data = TA_Handler(
                symbol= self.symbol,
                screener = self.screener,
                exchange = self.exchange,
                interval = Interval.INTERVAL_1_MINUTE
            )

            return self.data
        
        elif "5m" in self.interval:
            self.data = TA_Handler(
                symbol = self.symbol,
                screener= self.screener,
                exchange = self.exchange,
                interval = Interval.INTERVAL_5_MINUTES
            )

            return self.data
    

    def search(self):
        return f'''
        SUMMARY:
        Asset Picked: {self.symbol}
        Screener: {self.screener}
        Exchange Market: {self.exchange}
        Interval = {self.interval}
        '''

            
    
    def show_search(self):
        r = self.data.get_analysis().summary


def main():
    symbol = input("Choose the ticker for analysis: ")
    screener = input("Choose where the asset is being screened (america,crypto etc..):  ")
    exchange = input("Market of circulation: " )
    interval = input("Time of analysis: ")

    asset = Screener(symbol,screener,exchange)
    asset.detailed_search()
    
    print(asset.search())
    print(asset.show_search())






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
