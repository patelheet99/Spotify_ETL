import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import sqlite3

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"

if __name__ == "__main__":

#Importing the songs_df from the Extract.py
#Loading into Database
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('artists.sqlite')
    cursor = conn.cursor()

    #SQL Query to Create Played Songs
    sql_query_1 = """
    SELECT * FROM Artist
    """
    cursor.execute(sql_query_1)
    rows=cursor.fetchall()
    print(rows)

    conn.close()
    