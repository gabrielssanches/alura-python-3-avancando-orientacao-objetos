class Media:
    def __init__(self, name, year):
        self.__name = name.title()
        self._year = year
        self._likes = 0

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name.title()

    def like(self):
        self._likes += 1

class Series(Media):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self._seasons = seasons

    def __str__(self):
        return f"{self.name} ({self._year}) seasons:{self._seasons} likes:{self._likes}"

class Movie(Media):
    def __init__(self, name, year, length):
        super().__init__(name, year)
        self._length = length

    def __str__(self):
        return f"{self.name} ({self._year}) length:{self._length} min likes:{self._likes}"

class Playlist():
    def __init__(self, name, list):
        self.__name = name
        self.__list = list

    @property
    def name(self):
        return self.__name

    def __getitem__(self, item):
        return self.__list[item]

    def __len__(self):
        return len(self.__list)

avengers = Movie("Avengers", 2019, 180)
seinfeld = Series("seinfeld", 1991, 9)


print(avengers)
print(seinfeld)

avengers.name = "avengers - Infinity wars"
print(avengers)

avengers.like()
avengers.like()
avengers.like()

seinfeld.like()
seinfeld.like()
seinfeld.like()
seinfeld.like()
seinfeld.like()

play_list = [avengers, seinfeld]

for media in play_list:
    print(media)

playlist = Playlist("MyFlix", play_list)

print(f"{playlist.name} has {len(playlist)} medias")
for media in playlist:
    print(media)
