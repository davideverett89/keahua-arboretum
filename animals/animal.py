import random
from attributes import Identifiable

class Animal(Identifiable):

    def __init__(self, species, prey, location, minimum_release_age):
        Identifiable.__init__(self)
        self.__species = species
        self.__prey = prey
        self.__location = location
        self.__minimum_release_age = minimum_release_age
        self.__age = random.randrange(1, 16)

    @property
    def species(self):
        return self.__species

    @property
    def prey(self):
        return self.__prey

    @property
    def location(self):
        return self.__location

    @property
    def minimum_release_age(self):
        return self.__minimum_release_age

    @property
    def age(self):
        return self.__age

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The {self.species} ate {prey} for a meal')
        else:
            print(f'The {self.species} rejects the {prey}')

    def move(self, propulsion, speed):
        return f"{self.species} moves at {speed} meters/sec by {propulsion}"

    def __str__(self):
        return f'{self.species} {self.id} says: '