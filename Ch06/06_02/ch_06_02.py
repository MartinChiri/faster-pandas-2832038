import sqlite3
conn = sqlite3.connect('bikes.db')
query = '''
    SELECT name, sql
    FROM sqlite_master
    WHERE type = 'table'
    '''
for name, sql in conn.execute(query):
    print(name, sql)
# bike_rides CREATE TABLE bike_rides(
#   year INT,
#   month INT,
#   day INT,
#   trip_id INT,
#   bike_id INT,
#   duration INT
# )
conn.execute('SELECT MAX(year), MIN(year) FROM bike_rides').fetchall()
# [(2017, 2016)]
import pandas as pd
query = '''
    SELECT year, month, duration
    FROM bike_rides
    '''
df = pd.read_sql(query, conn)
df.groupby(['year', 'month'])['duration'].median()
# year  month
# 2016  1        14.0
#       2        15.0
#       3        14.0
#       5        15.0
#       6        14.0
#       7        15.0
#       8        13.0
#       9        15.0
#       10       16.0
#       11       14.0
# 2017  1        14.0
#       2        16.0
#       3        14.0
#       4        18.0
#       5        18.0
#       6        16.0
#       7        16.0
#       8        13.0
#       9        17.0
#       10       16.0
#       11       18.0
#       12       16.0
# Name: duration, dtype: float64
