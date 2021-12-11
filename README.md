#  Scraper and Login Automator for Zerodha Kite
![Build](https://github.com/vrishank97/kitescraper/actions/workflows/python-package-conda.yml/badge.svg)
## Installing the library

You can install the release via pip

```
pip install kitescraper
```
## API usage

```python
from kitescraper.login import KiteHelper
from kitescraper.scrape import KiteScraper

kitehelper = KiteHelper(apikey="", apisecret="", username="", password="", pin="")

kite = kitehelper.GetKite()

scraper = KiteScraper(kite)

symbols = ["RELIANCE", "ACC", "HDFCBANK"]

for symbol in symbols:
    s = scraper.GetInstrumentTokenforSymbol(symbol)
    df = scraper.GetSymbolHistoricalData(instrument_token=s, start='2016-01-01', end='2021-05-01', interval='minute')
    df.to_csv("{}.csv".format(symbol))
```
