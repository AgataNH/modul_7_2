from faker import Faker
fake = Faker(['pl_PL'])

class Films:
   def __init__(self, title, year, genre, number_of_plays):
       self.title = title
       self.year = year
       self.genre = genre
       self.number_of_plays = number_of_plays
   
   def play(self):
       self.number_of_play += 1
       return self.number_of_play
    
   def show_film(self):
       return f'Film "{self.title} ({self.year})", {self.genre}, {self.number_of_plays}' 

class Series(Films):
   def __init__(self, epizod_number, sezon_number, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.epizod_number = epizod_number
       self.sezon_number = sezon_number

   def play(self):
       number_of_play += 1
       return number_of_play

   def show_series(self):
       return f'Serial "{self.title} {self.sezon_number}{self.epizod_number}", {self.year}, {self.genre}, {self.number_of_plays}' 

def create_titles(film_number, series_number):
    titles_list = []
    for _ in range(film_number):
        film = Films(title = fake.sentence(nb_words=4), year = fake.year(), genre = fake.sentence(nb_words=1, ext_word_list=['dokument', 'komedia', 'dramat']), number_of_plays = fake.random_digit())
        titles_list.append(film)
    for _ in range(series_number):
        series = Series(title = fake.sentence(nb_words=2), sezon_number = fake.numerify(text = 'S0%'), epizod_number = fake.numerify(text = 'E0%'), year = fake.year(), genre = fake.sentence(nb_words=1, ext_word_list=['dokumentalny', 'komediowy', 'historyczny']), number_of_plays = fake.random_digit())
        titles_list.append(series)    
    return titles_list

for item in create_titles(2, 3):
    print(item.show_film())
    print(item.show_series())


