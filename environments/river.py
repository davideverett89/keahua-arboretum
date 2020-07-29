from environments import Biome


class River(Biome):

    def __init__(self):
        super().__init__("River", 6, 12, "Fresh Water")

    def add_animal(self, animal):
        try:
            if len(self.animals) < self.animal_capacity:
                if animal.age >= animal.minimum_release_age:
                    if hasattr(animal, 'is_euryhaline'):
                        self.animals.append(animal)
                        print(f'{animal.species} [{animal.id}] was added to the river!')
                        input('Please press enter to continue...')
                    elif hasattr(animal, 'aquatic') and (hasattr(animal, "cell_type") and animal.cell_type == "hypertonic"):
                        self.animals.append(animal)
                        print(f'{animal.species} [{animal.id}] was added to the river!')
                        input('Please press enter to continue...')
                    else:
                        raise AttributeError(f'{animal.species} [{animal.id}] cannot live in a river!')
                else:
                    raise ArithmeticError(f'{animal.species} [{animal.id}] is only {animal.age} months old.  That\'s too young to be released!')
            else:
                raise Exception(f'Not enough room for {animal.species} [{animal.id}]!')
        except (AttributeError, ArithmeticError, Exception) as err:
            print(err)
            raise
            input('Press enter to continue')

    def add_plant(self, plant):
        try:
            if len(self.plants) < self.plant_capacity:
                if plant.freshwater and plant.requires_current:
                    self.plants.append(plant)
                    print(f'{plant.species} was added to the river!')
                    input('Press enter to continue...')
                else:
                    raise AttributeError('Plant cannot grow in the river!')
            else:
                raise AttributeError(
                    'River has already reached plant capacity!')
        except AttributeError as err:
            print(err)

            input('Press enter to continue...')