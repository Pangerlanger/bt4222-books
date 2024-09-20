import pandas as pd 
import json

def load_data(file_name):
    count = 0
    data = []
    with open(file_name, 'r') as fin:
        for l in fin:
            d = json.loads(l)
            count += 1
            data.append(d)
    return data


df_interactions = load_data('goodreads_interactions_children.json')
df_interactions = pd.DataFrame(df_interactions)
print(df_interactions)

df_children_books = load_data('goodreads_books_children.json')
df_children_books = pd.DataFrame(df_children_books)
print(df_children_books)

df_reviews_children = load_data('goodreads_reviews_children.json')
df_reviews_children = pd.DataFrame(df_reviews_children)
print(df_reviews_children)