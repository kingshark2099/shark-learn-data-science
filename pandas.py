# object creation
fav_movies = pd.Series(["Interstellar", 
                        "Little Women",
                        "Se7en",
                        "Avengers: Endgame",
                        "Drive My Car",
                        "Parasite",
                        "In the Mood for Love",
                        "Burning"])
year = pd.Series([2014, 2019, 1995, 2019, 2021, 2019, 2000, 2018])
dates = pd.date_range("20020929", periods=3)
movies = pd.DataFrame({"Name": fav_movies, "Year":year, "Rate":5})
watched = pd.read_csv('watched.csv')

# viewing data
fav_movies.head()
fav_movies.tail(3)
movies.describe() # statistic summary of the data (number)
movies.index
movies.columns
movies.set_index("Year").sort_index()

# Convert pandas to numpy
movies.to_numpy() # get 2D list contains [movies, year]

# selection
movies["Name"]
movies[0:2]
movies.loc[:,["Name"]]
movies.loc[watched.Year>2010] # watched.Year == watched["Year"]
movies.at[1, "Name"]  
movies.iloc[3] # get the fourth entry
movies.iloc[:4, 0:2] # get entry index 0-3 and column 0-1

