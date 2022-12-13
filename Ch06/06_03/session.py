import pandas as pd
store = pd.HDFStore('stocks.h5')
store.keys()
# ['/stocks']
df = store.stocks
df.columns
# Index(['symbol', 'open', 'high', 'low', 'close', 'adj close', 'volume'], dtype='object')
store.select('stocks', stop=3)
#            symbol      open      high       low     close  adj close    volume
# date                                                                          
# 1962-01-02    IBM  7.713333  7.713333  7.626667  7.626667   0.609973  387200.0
# 1962-01-03    IBM  7.626667  7.693333  7.626667  7.693333   0.615304  288000.0
# 1962-01-04    IBM  7.693333  7.693333  7.613333  7.616667   0.609173  256000.0
s = store.get_storer('stocks')
s.nrows
# 88839
df = store.select('stocks', '(index >= "2010") & (index < "2012")')
df.index.min(), df.index.max()
# (Timestamp('2010-01-04 00:00:00'), Timestamp('2011-12-30 00:00:00'))
df = store.select('stocks', '(index >= "2010") & (index < "2012")', columns=['symbol', 'close',
'volume'])
df.columns
# Index(['symbol', 'close', 'volume'], dtype='object')
