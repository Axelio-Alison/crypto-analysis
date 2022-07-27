import pandas as pd
from pybit import usdt_perpetual

import crypto_scraper as cs

session_unauth = usdt_perpetual.HTTP(
    endpoint="https://api-testnet.bybit.com"
)

bybit_scr = cs.ByBit_Scraper(session_unauth)
bybit_scr.extract_history("BTCUSDT", 5)
print(bybit_scr.get_dataframe())
bybit_scr.to_csv()
