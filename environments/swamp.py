from attributes import Stagnant
from environments import Biome

class Swamp(Biome, Stagnant):

    def __init__(self):
        Biome.__init__(self, "Swamp", 12, 8, "Stagnant Freshwater")
        Stagnant.__init__(self)

    def add_animal(self, animal):
        try:
            if len(self.animals) < self.animal_capacity:
                if hasattr(animal, "aquatic") and (hasattr(animal, "current_speed") and animal.current_speed == 0):
                    if animal.age >= animal.minimum_release_age:
                        self.animals.append(animal)
                        print(f'{animal.species} [{animal.id}] was added to the swamp!')
                        input('Please press enter to continue...')
                    else:
                        raise ArithmeticError(f'{animal.species} [{animal.id}] is only {animal.age} months old.  That\'s too young to be released!')
                else:
                    raise AttributeError(f'{animal.species} [{animal.id}] cannot live in a swamp!')
            else:
                raise Exception(f'Not enough room for {animal.species} [{animal.id}]!')
        except (ArithmeticError, AttributeError, Exception) as err:
            print(err)
            raise
            input('Press enter to continue...')

    def add_plant(self, plant):
        try:
            if len(self.plants) < self.plant_capacity:
                if plant.current_speed == 0:
                    self.plants.append(plant)
                    print(f'{plant.species} was added to the swamp!')
                    input('Press enter to continue...')
                else:
                    raise AttributeError('Plant cannot grow in the swamp!')
            else:
                raise AttributeError('Swamp has already reached plant capacity!')
        except AttributeError as err:
            print(err)
            input('Press enter to continue...')
