# lesson 10.11.2021
# OOP
import random

class TvShow():
    def __init__(self, title, genre, seasons, platform, actors):
        self.title = title
        self.genre = genre
        self.seasons = seasons
        self.platform = platform
        self.actors = actors

Vikings = TvShow('Vikings', 'Action', 6, 'Netflix', ['Ragnar', 'Lagratha', 'Bjorn'])
print(Vikings.__dict__)
# print(vars(Vikings))

The_100 = TvShow('The100', 'Action', 5, 'Netflix', ['Octavia', 'Gaha', 'Clarke'])
print(The_100.__dict__)
# print(vars(The_100))

class Person:
    def __init__(self, id=0, name='Incognito'):
        print('new person was created')
        self.id = id
        self.name = name

    def __str__(self):
        # this is default
        # return str(type(self)) + ' object at 0x0000027B2E009520'
        # return str(random.randint(50, 100))
        return f'Person (id = {self.id} name = "{self.name}")'

danny = Person(1, 'danny')
print(danny) # same as print(danny.__str__())
suzi = Person(2, 'suzi')
print(suzi)


