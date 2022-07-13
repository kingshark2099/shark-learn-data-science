import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# git fetch && git merge origin/main

# read data
watched = pd.read_csv('watched.csv')
watchlist = pd.read_csv('watchlist.csv')
ratings = pd.read_csv('ratings.csv')
diary = pd.read_csv('diary.csv')
profile = pd.read_csv('profile.csv')
reviews = pd.read_csv('reviews.csv')
list_anime = pd.read_csv('anime.csv')
list_physics = pd.read_csv('physics-y.csv')
list_revenge = pd.read_csv('revenge-is-the-fuel.csv')
list_women = pd.read_csv('women-in-films.csv')
list_twist = pd.read_csv('when-i-am-not-twisted-by-reality-movies-instead.csv')

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
# get year wacthed
watched.loc[0, "Date"].split("-")
def year(row):
    date = row.Date.split("-")
    row.Date = date[0]
    return row
ratings.apply(year, axis='columns').loc[:, ["Name", "Rating", "Date"]].set_index("Date")

# grouping
# count how many movies each ratings
ratings.groupby("Rating").size()
# group by decades release
def decade(row):
    if row.Year >= 2020: row.Year = "2020s"
    elif row.Year >= 2010: row.Year = "2010s"
    elif row.Year >= 2000: row.Year = "2000s"
    else: row.Year = "1900s"
    return row
# get how many movies each decades
group_by_decade = ratings.apply(decade, axis='columns').sort_values('Year').loc[:,['Name','Year','Rating']]
group_by_decade.rename(columns={'Year': 'Decade'}).groupby("Decade").size() 

# missing values
# find out whether theres a movie without release year data
watched[pd.isnull(watched.Year)]
# changing missing values of Date column with TBA
watched.Date.fillna("TBA")
# get type of column
watched.Date.dtype
watched.Date.astype(str)

# combining
movies = pd.concat([watched, watchlist])
movies

