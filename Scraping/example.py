import pandas as pd
from pybit import usdt_perpetual

import crypto_scraper as cs

extraction = True
updating = False

session_unauth = usdt_perpetual.HTTP(
    endpoint="https://api-testnet.bybit.com"
)

bybit_scr = cs.ByBit_Scraper(session_unauth)                                                            # Create a ByBit Scraper Object

# Data Extraction
if extraction:                                                   
    bybit_scr.extract_history("ETHUSDT", 15)                                                            # Extract Data
    print(bybit_scr.get_dataframe())                                                                    # Print the final dataframe
    bybit_scr.to_csv(r"C:\Users\axeli\Desktop\Github\crypto-trading\Data Analysis\ETHUSDT 15.csv")      # Save the data in a .csv file

# Data Updating
if updating:
    bybit_scr.set_dataframe(pd.read_csv(r"C:\Users\axeli\Desktop\Github\crypto-trading\Data Analysis\BTCUSDT 5.csv"))   # Read a .csv and set it as dataframe
    bybit_scr.update_history()                                                                                          # Update the dataframe
    bybit_scr.to_csv(r"C:\Users\axeli\Desktop\Github\crypto-trading\Data Analysis\BTCUSDT 5.csv")                       # Save the data in a .csv file