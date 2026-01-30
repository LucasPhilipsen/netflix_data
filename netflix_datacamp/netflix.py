# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path_netflix = r"C:\Users\ImperadorMaisTemido\Documents\Progamação\Python\netflix_datacamp\netflix_data.csv"
# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv(path_netflix)


ser_filme = netflix_df['type'] == 'Movie'
anos90 = netflix_df[(netflix_df['release_year'] < 2000 ) & (netflix_df['release_year'] >= 1990) & (ser_filme)]
duration = anos90['duration'].mode();
short_movie_count = anos90[(netflix_df['duration'] < 90) & (netflix_df['genre'] == 'Action')];

show_90s_movies = print(f"filmes dos anos 90s: \n{anos90}")
show_duration = print(f'O tempo mais frequente de duração de um filme: {np.array(duration)[0]} Minutos')
show_short_movies_count = print(f'numero de filmes de ação com tempo de duração menor que 90min: {short_movie_count.shape[0]}')

