from tradingview_ta import TA_Handler, Interval

class Screener():

    def __init__(self, symbol, screener, exchange):
        self.symbol = symbol
        self.screener = screener
        self.exchange = exchange
        self.interval = None
        self.data = None
    
    def detailed_search(self):
        interval_mapping = {
            "1m": Interval.INTERVAL_1_MINUTE,
            "5m": Interval.INTERVAL_5_MINUTES,
            "15m": Interval.INTERVAL_15_MINUTES,
            "30m": Interval.INTERVAL_30_MINUTES,
            "1h": Interval.INTERVAL_1_HOUR,
            "2h": Interval.INTERVAL_2_HOURS,
            "4h": Interval.INTERVAL_4_HOURS,
            "1d": Interval.INTERVAL_1_DAY,
            "1W": Interval.INTERVAL_1_WEEK,
            "1M": Interval.INTERVAL_1_MONTH
        }

        interval_constant = interval_mapping.get(self.interval)
        if interval_constant:
            self.data = TA_Handler(
                symbol=self.symbol,
                screener=self.screener,
                exchange=self.exchange,
                interval=interval_constant
            )

            if self.data:
                return self.data.get_analysis().summary
            else:
                return "No data available"
        else:
            return "Invalid interval specified"
    
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

def run():
    symbol = input("Choose the ticker for analysis: ")
    screener = input("Choose where the asset is being screened (america, crypto, etc.): ")
    exchange = input("Market of circulation: ")
    interval = input("Time of analysis (1m, 5m, 15m, 30m, 1h, 2h, 4h, 1d, 1W, 1M): ")

    asset = Screener(symbol, screener, exchange)
    asset.interval = interval
    asset.detailed_search()
    
    print(asset.search())
    print(asset.show_search())

if __name__ == "__main__":
   run()
