"""Script for scraping missing data from Google Books API"""
import os
import datetime
import requests
import json
import pandas as pd
import numpy as np
from typing import Dict

"""
Instructions: 

1. Run script after replace API_KEY and START 
2. Record index script stopped at and let the next person know

"""

# Replace with your API key
API_KEY = [#"AIzaSyCFw_Swc8HiLh7qri1PLVRGDjChNfsMNjw",
           #"AIzaSyAOxUnS3WzsM1tuZkDnlopaBHQyPWcwmAs",
           #"AIzaSyCalbnS5jeGOZP2VIEwpBI0upryR3MDMqA",
           #"AIzaSyABJauHLzk90FlhBrMeU7mxG-cIWAt_zNs",
           #"AIzaSyB3xqviQy-Xvo1WVleUXixX2JLEvrWXF2Q",
           "AIzaSyC4OKjNyeXy5an3YF9Pmkuyh_xEWETm3Og",
           "AIzaSyBacJhtWccHveVOj3JLYAC1OcJRqNDroCo",
           "AIzaSyDIq-XHe0hLgi3_pNwSLItO0vNHnVezutI",
           "AIzaSyBFCnJuM7eELiDsjS-LsDJMSYdFImvB2B8",
           "AIzaSyBPLH0uoFtMpPcDlIuaAVVmPdmxRU_FeYM",
           "AIzaSyCVFrp9gOsvG125UhRkKqRK47zIFt7t9l8",
           "AIzaSyApwmU4CEBnrde4fSGTsY5u72xFweXG_kg",
           #"AIzaSyAevtLyR3LyO9iNGqqckpCxC5qPfy4dQJY",
           #"AIzaSyBukwnIGd5XOv5scP_xqsxIAwoWqtJsJpw",
           #"AIzaSyCsZMzc2w0l437ULnR5rWRYa2G9eh9PvRQ",
           #"AIzaSyBjb9uV6UMHpZLfNLA2ylV9vBhR1d1jb7g",
           #"AIzaSyDSSARKpZrrm5_q8JlnGv-clnf-2xpeQEM",
           #"AIzaSyCk-EWPCS1advNKcBstHvl9mUBLGQrWYR8"
           ]


           
# Replace with updated index
START = 22000
QUERYLIMIT = 1000

column_mapping = {
    'language_code': 'language',
    'description': 'description',
    'authors': 'authors',
    'publisher': 'publisher',
    'publication_day': 'publishedDate',
    'publication_month': 'publishedDate',
    'publication_year': 'publishedDate',
    'num_pages': 'pageCount'
}

def check_missing_value(val) -> bool:
    """Returns True/False if value is missing/invalid"""

    if isinstance(val, float):
        return np.isnan(val)
    if isinstance(val, str):
        return val == ''
    return val == None

def update_missing_info(df: pd.DataFrame, row: pd.Series, data: Dict) -> None:
    """Updates row with missing values"""

    data['publishedDate'] = pd.to_datetime(data['publishedDate'])

    for col, val in row.items():
        if (col in column_mapping) and (check_missing_value(val)):
            if column_mapping[col] in data:
                if col == 'publication_day': 
                    new_val = data['publishedDate'].day
                elif col == 'publication_month':
                    new_val = data['publishedDate'].month
                elif col == 'publication_year':
                    new_val = data['publishedDate'].year
                else:
                    new_val = data[column_mapping[col]]

                row[col] = new_val
    df.loc[len(df)] = row
        

def scrape_data(df) -> None:
    counter = None
    query_count = 0
    api_idx = 0
    categories = []
    update_df = pd.DataFrame(columns=df.columns)
    error_df = pd.DataFrame(columns=df.columns)

    try:
        for idx, row in df.iterrows():
            key = API_KEY[api_idx]
            if query_count >= 1000:
                if api_idx == (len(API_KEY)-1):
                    break
                query_count = 0
                api_idx += 1
                key = API_KEY[api_idx]
            query_count += 1
            counter = idx

            if check_missing_value(row['isbn']):
                if check_missing_value(row['isbn13']):
                    isbn = None
                else:
                    isbn = row['isbn13']
            else:
                isbn = row['isbn']

            if isbn:
                url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={key}"
                print(f"{counter}: {url}")
                try:
                    response = requests.get(url)
                    data = response.json()['items'][0]['volumeInfo']
                    update_missing_info(update_df, row.copy(), data)

                    if 'categories' in data:
                        categories.append(data['categories'])
                    else:
                        categories.append([])
                except:
                    print("ERROR")
                    error_df.loc[len(error_df)] = row
            else:
                error_df.loc[len(error_df)] = row
    
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
    print(categories)
    print(update_df)
    update_df['categories'] = categories
    update_df.to_csv('update_df5.csv', index=False)
    error_df.to_csv('error_df5.csv', index=False)
    print(f"Script stopped running at index: {counter}")

    
if __name__ == "__main__":
    df = pd.read_csv('non_missing_df.csv')[START:]
    scrape_data(df)