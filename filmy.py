from faker import Faker
fake = Faker(['pl_PL'])

class Films:
   def __init__(self, title, year, genre, number_of_plays):
       self.title = title
       self.year = year
       self.genre = genre
       self.number_of_plays = number_of_plays
   
   def play(self):
       self.number_of_plays += 1
       return self.number_of_plays
    
   def show_film(self):
       return f'Film "{self.title} ({self.year})", {self.genre}, {self.number_of_plays}' 

class Series(Films):
   def __init__(self, epizod_number, sezon_number, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.epizod_number = epizod_number
       self.sezon_number = sezon_number

   def play(self):
       number_of_plays += 1
       return number_of_plays

   def show_series(self):
       return f'Serial "{self.title} {self.sezon_number}{self.epizod_number}", {self.year}, {self.genre}, {self.number_of_plays}' 

def create_titles(film_number, series_number):
    titles_list = []
    for _ in range(film_number):
        film = Films(title = fake.sentence(nb_words=4), year = fake.year(), genre = fake.sentence(nb_words=1, ext_word_list=['dokument', 'komedia', 'dramat']), number_of_plays = fake.random_int(0, 100))
        titles_list.append(film)
    for _ in range(series_number):
        series = Series(title = fake.sentence(nb_words=2), sezon_number = fake.numerify(text = 'S0%'), epizod_number = fake.numerify(text = 'E0%'), year = fake.year(), genre = fake.sentence(nb_words=1, ext_word_list=['dokumentalny', 'komediowy', 'historyczny']), number_of_plays = fake.random_int(0, 100))
        titles_list.append(series)    
    titles_list = sorted(titles_list, key=lambda title: title.number_of_plays, reverse = True)
    return titles_list

titles = create_titles(5, 5)

print("Biblioteka filmów:")
for element in titles:
    if isinstance(element, Series):
        print(element.show_series())
    elif isinstance(element, Films):
        print(element.show_film())

def get_movie():
    film_list = []
    for element in titles:
        if isinstance(element, Films):
            film_list.append(element)
    return film_list

def get_series():
    series_list = []
    for element in titles:
        if isinstance(element, Series):
            series_list.append(element)
    return series_list

def search(search_title):
    for element in titles:
        if element.title == search_title:
            if isinstance(element, Series):
                return element.show_series()
            elif isinstance(element, Films):
                return element.show_film()
            else:
                return "Nie ma takiego filmu w bibliotece"

def top_titles(top):
    return titles[0:top] 

import datetime

date = datetime.date.today()

print()
print(f"Najpopularniejsze filmy i seriale dnia: {date}")
print(top_titles(3))