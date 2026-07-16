class Movie:
    def __init__(self, name, director, rating):
        self.name = name
        self.director = director
        self.rating = rating

    def display(self):
        print("Movie:", self.name)
        print("Director:", self.director)
        print("Rating:", self.rating)


m = Movie("3 Idiots", "Rajkumar Hirani", 9)
m.display()