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

# functions and maps
# get all the release year from wacthed movies
watched.Year.unique()
# counting how many movies i watched each year
watched.Year.value_counts()
# using apply() to get ratings/10
def rate(row):
    row.Rating = row.Rating + 5.0
    return row
rated_movies = ratings.apply(rate, axis='columns').sort_values("Rating", ascending=False)
rated_movies.loc[:,["Name", "Year","Rating"]].set_index("Year")

# grouping
# count how many movies each ratings
ratings.groupby("Rating").size()

# missing values
# find out whether theres a movie without release year data
watched[pd.isnull(watched.Year)]
# changing missing values of Date column with TBA
watched.Date.fillna("TBA")
# get type of column
watched.Date.dtype
watched.Date.astype(str)
# get year wacthed
watched.loc[0, "Date"].split("-")
def year(row):
    date = row.Date.split("-")
    row.Date = date[0]
    return row
ratings.apply(year, axis='columns').loc[:, ["Name", "Rating", "Date"]].set_index("Date")

