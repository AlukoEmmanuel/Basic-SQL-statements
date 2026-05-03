import sqlite3
import pandas as pd
database = 'database.sqlite'

conn = sqlite3.connect(database)
print("Opened data successfully!")
tables = pd.read_sql(""" select * from sqlite_master where  type='table';
""", conn)

print("Tables in database:")
print(tables)

matches = pd.read_sql(""" select * from Match;
""", conn)
print("Matches in database:")
print(matches.info())