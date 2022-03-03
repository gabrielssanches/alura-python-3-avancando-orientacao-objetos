class Media:
    def __init__(self, name, year):
        self.__name = name.title()
        self._year = year

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name.title()

class Series(Media):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self._seasons = seasons

    def __str__(self):
        return f"{self.name} ({self._year}) seasons:{self._seasons}"

class Movie(Media):
    def __init__(self, name, year, length):
        super().__init__(name, year)
        self._length = length

    def __str__(self):
        return f"{self.name} ({self._year}) length:{self._length} min"



avengers = Movie("Avengers", 2019, 180)
seinfeld = Series("seinfeld", 1991, 9)


print(avengers)
print(seinfeld)

avengers.name = "avengers - Infinity wars"
print(avengers)
