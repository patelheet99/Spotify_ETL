import datetime
from datetime import datetime,timedelta
import get_token
import pandas as pd
import requests

USER_ID = "" 
TOKEN = get_token.fetch_token()
# Creating an function to be used in other python files
def return_dataframe(): 
    input_variables = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }
    # Download all songs you've listened to "after yesterday", which means in the last 24 hours      
    r = requests.get("https://api.spotify.com/v1/artists/06HL4z0CvFAxyc27GXpf02/albums", headers = input_variables)

    data = r.json()
    album_name = []
    release_date = []
    img=[]
    # Extracting only the relevant bits of data from the json object      
    for song in data["items"]:
        album_name.append(song["name"])
        release_date.append(song["release_date"])
        img.append(song["images"][0]["url"])
        
    # Prepare a dictionary in order to turn it into a pandas dataframe below       
    artist_dict = {
        "album_name" : album_name,
        "release_date": release_date,
        "images":img,
    }
    artist_df = pd.DataFrame(artist_dict, columns = ["album_name", "release_date","images"])
    return artist_df
