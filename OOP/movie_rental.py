import random
from faker import Faker
from datetime import date
rental = []

class Movie:
    def __init__(self, title, year, gendre, played):
        self.title = title
        self.year = year
        self.gendre = gendre
        self.played = played
    
    def play(self):
        self.played += 1

    def __str__(self):
        return f'{self.title} {self.year}'

class TvSeries(Movie):
    def __init__(self, title, year, gendre, played, episode, season):
        super().__init__(title, year, gendre, played)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title} S{self.season:02d}E{self.episode:02d}'

def add_movie(title, year, gendre, played, movies_list = rental):
    rental.append(Movie(title,year,gendre,played))
    return rental

def add_tv_series(title, year, gendre, played, episode, season, movies_list = rental):
    rental.append(TvSeries(title, year, gendre, played, episode, season))
    return rental

def get_movies():
    temp = []
    for i in rental:
        if isinstance(i, TvSeries) == False: temp.append(i)
    return temp

def get_series():
    temp = []
    for i in rental:
        if isinstance(i, TvSeries): temp.append(i)
    return sorted(temp, key = lambda movie: movie.title)
    
def search(lookup_word):
    temp = []
    for i in rental:
        if lookup_word.lower() in i.title.lower():
            temp.append(i)
    return sorted(temp, key = lambda tv: tv.title)

def generate_views(movie_list = rental):
    movie = random.randint(1, len(rental))
    views = random.randint(1,100)

    for x in range(views):
        rental[movie - 1].play()
    
    return rental

def ten_times(func):
    for x in range(10):
        return func()

def top_titles(how_many):
    movies = sorted(rental, key = lambda k: k.played, reverse = True)
    return movies[:how_many]

def add_full_season(title, year, gendre, season, episodes):
    for episode in range(1, episodes + 1):
        rental.append(TvSeries(title, year, gendre, 0, episode, season))


faker = Faker()
print("Biblioteka filmów")

rental.append(Movie('The Green Mile', 1999, 'Drama', 0))
rental.append(Movie('The Shawshank Redemption', 1994, 'Drama', 0))
rental.append(Movie('Forrest Gump', 1994, 'Comedy', 0))
rental.append(Movie('Leon', 1994, 'Drama', 0))
rental.append(Movie('Requiem for a Dream', 2000, 'Drama', 0))

rental.append(TvSeries('Games of Thrones', 2011, 'Drama', 0, 1,1))
rental.append(TvSeries('House Md', 2004, 'Drama', 0, 2,2))
rental.append(TvSeries('Breaking Bad', 2008, 'Drama', 0, 3,3))
rental.append(TvSeries('Friends', 1994, 'Comedy', 0, 4,4))
rental.append(TvSeries('Sherlock', 2010, 'Drama', 0, 5,5))
rental.append(TvSeries('Stranger Things', 2016, 'Drama', 0, 6,6))

add_full_season('McDonald', 2004, 'Drama', 1, 20)

for x in range(1000):
    generate_views()

for movie in rental:
    print(f'{movie} {movie.played}')
    
print(f"Najpopularniejsze filmy i seriale dnia {date.today()}")

top_3 = top_titles(3)
for i in top_3:
    print(i)