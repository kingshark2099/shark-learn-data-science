# Class
class Movie:
    def __init__(self, name, year, rate):
        self.name = name
        self.year = year
        self.rate = rate
    
    def rating(self):
        print("Name:", self.name)
        print("Year:", self.year)
        print("Rate:", self.rate)
    def favorite(self):
        if self.rate == 5:
            print(self.name, "is my favorite movie")
        else:
            print(self.name, "is not my favorite movie")

# Inheritance
class FavMovie(Movie):
    def __init__(self, name, year, rate):
        # inherit methods and properties
        # super().__init__(self, name, year, rate) or
        Movie.__init__(self, name, year, rate) 
    def text(self):
        print("I give 5 star to", self.name, "(%d)" %self.year)

# create object        
m1 = Movie("Interstellar", 2014, 4.5)        
m1.rating()
m1.favorite()

# modify object properties
m1.rate = 5
del m1.rate

# create object
m2 = FavMovie("Drive My Car", 2021, 5)
m2.favorite()
m2.rating()
m2.text()
