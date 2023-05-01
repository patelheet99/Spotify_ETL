import extract
import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import sqlite3

DATABASE_LOCATION = "sqlite:///artists.sqlite"

if __name__ == "__main__":

#Importing the songs_df from the Extract.py
    load_df=extract.return_dataframe()
    print(load_df)
#Loading into Database
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('artists.sqlite')
    cursor = conn.cursor()

    #SQL Query to Create Played Songs
    sql_query_1 = """
    CREATE TABLE IF NOT EXISTS Artist(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    album_name VARCHAR(200),
    release_date VARCHAR(200),
    images VARCHAR(200)
    )
    """
    cursor.execute(sql_query_1)
    print("Opened database successfully")

    #We need to only Append New Data to avoid duplicates
    try:
        load_df.to_sql("Artist", engine, index=False, if_exists='append')
    except:
        print("Data already exists in the database")

    conn.close()
    print("Close database successfully")