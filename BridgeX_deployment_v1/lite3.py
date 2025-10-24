import sqlite3
import pandas as pd

"""Conecting to my sqlite3 database"""

#connecting to the sqlite database
conn= sqlite3.connect("local_repo.db")

#view all available tables
tables= pd.read_sql_query("SELECT name FROM sqlite_master WHERE type= 'table';", conn)
#print("Available table:\n", tables)

#Getting values from table
df= pd.read_sql_query("SELECT * FROM api_data", conn)
print("\nPreview of stored data: ")
print(df.head())
