import pandas as pd
import glob
import os
from sqlalchemy import create_engine
import urllib
import time

path = "YourPath"
filenames = glob.glob(path + "/*.xlsm")
filenames.sort(key=os.path.getmtime)
len_Ex_file = len(filenames)
print("Number of files in folder: " + str(len_Ex_file))
New_file = []
join = []

max_attempt = 10
for file in filenames:
    dfs = None
    for attempt in range(max_attempt):
        try:
            dfs = pd.read_excel(file, "Sheet2")
        except PermissionError:
            print("PermissionError on read attempt", attempt)
            time.sleep(300)
    if dfs is None:
        print("Failed to read", file)

    New_file.append(dfs)
    join = pd.concat(New_file)

connection_string = (
        'Driver={};'
        'Server= ;'
        'Database=;'
        'UID=;'
        'PWD=;'
        'Trusted_Connection=;')

connection_uri = F"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"
engine = create_engine(connection_uri)
join.to_sql("DB_name", engine, if_exists="replace", index=False)
print("All files updated")
