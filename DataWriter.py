import pandas as pd
import csv


class DataWriter:
    #Initialize DataWriter with passed dict
    def __init__(self,data,stats):
        self.data=data
        self.stats=stats
    
    def displayData():
        print(self.data)
        
    #Take dict and convert to df before writing to CSV
    def writeToCsv(self):
        df = pd.DataFrame.from_dict(self.data)
        stats = pd.DataFrame.from_dict(self.stats)
        stats.to_csv('data.csv',mode='a',header=True, index=False)
        df.to_csv('data.csv',mode='a',header=True, index=False)
        print("Saved data to data.csv")
        
