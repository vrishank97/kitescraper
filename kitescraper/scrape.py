import kiteconnect
import pandas as pd
from calendar import monthrange
from time import sleep
from tqdm import tqdm

class KiteScraper( object ):
    def __init__( self, kite ):
        self.kite = kite

    def GetInstruments(self):
        return self.kite.instruments()

    def GetPositions(self):
        return self.kite.positions()

    def GetHoldings(self):
        return self.kite.holdings()
    
    def GetMargins(self):
        return self.kite.margins()

    def GetHistoricalPeriods(self, start, end):
        return [ (i.to_pydatetime(), self.last_day_of_month(i).to_pydatetime()) for i in pd.date_range(start, end, freq='MS').tolist()]
        
    def GetSymbolHistoricalData(self, instrument_token, start='2016-01-01', end='2021-05-01', interval='minute'):
        data = []
        for i in tqdm(self.GetHistoricalPeriods(start, end), desc="Downloading..."):
            data.append(pd.DataFrame.from_dict(self.kite.historical_data(instrument_token, from_date=i[0], to_date=i[1], interval=interval)))
            sleep(1)
        return pd.concat(data, ignore_index=True)

    def last_day_of_month(self, date_value):
        return date_value.replace(day = monthrange(date_value.year, date_value.month)[1])