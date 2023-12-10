# loads movie data from source to form pandas data frame
import pandas as pd

def load_movies_data():
    movies_df = pd.read_csv(r"C:\Users\dejon\OneDrive\Documents\movies")
    return movies_df