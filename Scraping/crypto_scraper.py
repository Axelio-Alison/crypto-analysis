import pandas as pd
from time import time

class ByBit_Scraper:

    def __init__(self, bybit_session, dataframe = pd.DataFrame()):
        self.session = bybit_session
        self.set_dataframe(dataframe)
    
    def extract_history(self, symbol, timeframe, logs = True):
        
        self.symbol = symbol
        self.timeframe = timeframe
        start_time = 0

        # Reset Dataframe
        self.dataframe = pd.DataFrame()

        if logs: print(f"{self.symbol} Starting Extraction ...")

        while True:

            # Set Start Time
            if not start_time:
                start_time = int(time())
            else:
                start_time = int(self.dataframe["start_at"].iloc[0])

            # Query Market Price K-line
            hist_data = self.session.query_mark_price_kline(
            symbol = self.symbol,
            interval = self.timeframe,
            from_time = start_time - 60*self.timeframe*200,
            limit = 200
            )['result']

            hist_df = pd.DataFrame(hist_data)
            hist_df.insert(3, 'datetime', pd.to_datetime(hist_df['start_at'], unit = 's'))

            # End Loop Conditions
            if not self.dataframe.empty:
                if hist_df['start_at'].iloc[0] == self.dataframe['start_at'].iloc[0]:
                    if logs: print("Ending Extraciton ...")
                    break
            
            if logs: print(f"\tExtraction Time: {hist_df['datetime'].iloc[0]}")

            # Update Dataframe
            self.dataframe = hist_df.append(self.dataframe, ignore_index = True)

    def update_history(self, logs = True):
        
        self.last_time = self.dataframe['start_at'].iloc[-1]
        
        if logs: print(f"{self.symbol} Starting Updating ...")
        
        while True:

            # Query Market Price K-line
            hist_data = self.session.query_mark_price_kline(
            symbol = self.symbol,
            interval = self.timeframe,
            from_time = self.dataframe['start_at'].iloc[-1] + 60*self.timeframe,
            limit = 200
            )['result']

            hist_df = pd.DataFrame(hist_data)
            hist_df.insert(3, 'datetime', pd.to_datetime(hist_df['start_at'], unit = 's'))

            # print(hist_df)
            
            if logs: print(f"\tExtraction Time: {hist_df['datetime'].iloc[0]}")

            # Update Dataframe
            self.dataframe = self.dataframe.append(hist_df, ignore_index = True)
            # print(self.dataframe)

            # End Loop Conditions
            if (int(time()) - self.dataframe['start_at'].iloc[-1]) < 300:
                if logs: print("Ending Updating ...")
                break

    def set_dataframe(self, dataframe):
        self.dataframe = dataframe

        if not self.dataframe.empty:
            self.symbol = dataframe['symbol'].iloc[0]
            self.timeframe = dataframe['period'].iloc[0]
    
    def get_dataframe(self, ):
        return self.dataframe
    
    def to_csv(self, path = ""):

        print("Creating .csv file ...")

        if path:
            self.dataframe.to_csv(path, index = False)
        else:
            self.dataframe.to_csv(f"{self.symbol} {self.timeframe}.csv", index = False)