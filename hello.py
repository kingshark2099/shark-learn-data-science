import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# git fetch && git merge origin/main

# get all columns names
watched.columns.tolist() 
ratings.columns.tolist()

# sorted data by Name
movies_watched = watched.sort_values('Name').reset_index()
movies_watchlist = watchlist.sort_values('Name').reset_index()

# access data using indexing
watched.iloc[0] # index [row, column]
watchlist.sort_values('Name').iloc[:3, 1]
watched.iloc[[1, 10, 100], :]
watchlist.loc[0, "Name"]
watchlist.loc[:, ['Name', 'Year']]

# set index
watched.sort_values('Year').set_index("Year")
watchlist.sort_values('Name').set_index("Name")

# conditional
# get movies released in 2020 and sorted by name
watched.loc[watched.Year == 2020].sort_values("Name")
# get movies released in or after 2010 decade whose ratings are or above 4
ratings.loc[(ratings.Year>= 2020) & (ratings.Rating >= 4.0)]
# get movies released after 2020 or before 2000
watched.loc[(watched.Year > 2020) | (watched.Year < 2000)]
# get movies released in 2010 & 2020 and remove Letterboxd URL and Date columns
ratings.loc[ratings.Year.isin([2010, 2020]), ['Name', 'Year','Rating']].sort_values('Year').set_index('Year')
