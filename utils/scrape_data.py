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
API_KEY = "AIzaSyCFw_Swc8HiLh7qri1PLVRGDjChNfsMNjw"
# Replace with updated index
START = 0

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

def update_missing_info(df: pd.DataFrame, row: pd.Series, row_idx: int, data: Dict) -> None:
    """Updates DF with missing values"""

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

                df.at[row_idx, col] = new_val
        

def scrape_data(df) -> None:
    counter = None
    query_count = 0
    categories = []
    error_df = pd.DataFrame(columns=df.columns)

    try:
        while query_count <= 1000:
            for idx, row in df.iterrows():
                query_count += 1
                counter = idx
                isbn = row['isbn'] if row['isbn'] else row['isbn13']

                url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={API_KEY}"
                print(url)
                try:
                    response = requests.get(url)
                    data = response.json()['items'][0]['volumeInfo']
                    update_missing_info(df, row, idx, data)

                    if 'categories' in data:
                        categories.append(data['categories'])
                    else:
                        categories.append([])
                except:
                    error_df.loc[len(df)] = row
                    categories.append([])
    
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
    
    df['categories'] = categories
    df.to_csv('missing_update_df.csv', index=False)
    error_df.to_csv('error_df.csv', index=False)
    print(f"Script stopped running at index: {counter}")

    
if __name__ == "__main__":
    df = pd.read_csv('missing_df.csv')[START:]
    scrape_data(df)