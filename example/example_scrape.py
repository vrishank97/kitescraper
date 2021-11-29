from ..kitescraper.login import KiteHelper
from ..kitescraper.scrape import KiteScraper

kitehelper = KiteHelper(apikey="", apisecret="", username="", password="", pin="")

kite = kitehelper.GetKite()

scraper = KiteScraper(kite)

symbols = ["RELIANCE", "ACC", "HDFCBANK"]

for symbol in symbols:
    s = scraper.GetInstrumentTokenforSymbol(symbol)
    df = scraper.GetSymbolHistoricalData(instrument_token=s, start='2016-01-01', end='2021-05-01', interval='minute')
    df.to_csv("{}.csv".format(symbol))