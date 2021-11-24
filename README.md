#  Scraper and Login Automator for Zerodha Kite
## API usage

```python
from ..kitescraper.login import KiteHelper
from ..kitescraper.scrape import KiteScraper

kitehelper = KiteHelper(apikey="12345", 
                        apisecret="abcde", 
                        username="user", 
                        password="pass", 
                        pin="123")

kite = kitehelper.GetKite()

scraper = KiteScraper(kite)


for symbol in [738561, 5633]:
    df = scraper.GetSymbolHistoricalData(instrument_token=symbol, 
                                        start='2016-01-01', 
                                        end='2021-05-01', 
                                        interval='minute')
    df.to_csv("{}.csv".format(symbol))
```