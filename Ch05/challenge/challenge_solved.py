"""Calculate the minimal and maximal distance driven from the data at
    taxi.csv.xz
Consume as little memory as possible and don't load more than 50,000 rows at a
time.
"""
import pandas as pd

def solved():
    df = pd.read_csv('taxi.csv.xz', usecols=['trip_distance'], chunksize=50_000)
    revs = (sdf.agg(['min','max']) for sdf in df)
    df = pd.concat(revs, axis=1)
    print(df.loc['max',:].max())
    print(df.loc['min', :].min())
