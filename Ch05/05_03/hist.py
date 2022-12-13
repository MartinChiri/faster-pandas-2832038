import pandas as pd
df = pd.read_csv('taxi.csv.xz', usecols=['VendorID', 'total_amount'], chunksize=100_000)
revs = []
for sdf in df:
    rev = sdf.groupby('VendorID').sum()
    revs.append(rev)
# revs
# pd.concat(revs)
# pd.concat(revs).groupby(level=0)
print(pd.concat(revs).groupby(level=0).sum())
