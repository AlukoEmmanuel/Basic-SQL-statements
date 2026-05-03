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

teams = pd.read_sql(""" select * from Team;
""", conn)
matches = pd.read_sql (""" select * from Match;
""", conn)
MI_wins = pd.read_sql(""" select * from Match where Match_winner == 7; """, conn)
print ("Teams in database:")
print(teams)
print("Matches won by MI:")
print(MI_wins)
MI_S8_S9 = pd.read_sql(""" select * from Match where season_id = 8 or season_id = 9; """, conn)
print("Matches in season 8 and 9:")
print(MI_S8_S9)
conn.close()