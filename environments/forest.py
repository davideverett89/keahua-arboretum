from environments import Biome


class Forest(Biome):

    def __init__(self):
        super().__init__("Forest", 32, 20, {"Rainy", "Shady"})

    def add_animal(self, animal):
        try:
            if len(self.animals) < self.animal_capacity:
                if hasattr(animal, "terrestrial") and (hasattr(animal, "is_reptile") or hasattr(animal, "is_mammal")):
                    if animal.age >= animal.minimum_release_age:
                        self.animals.append(animal)
                        print(f'{animal.species} [{animal.id}] was added to the forest!')
                        input('Please press enter to continue...')
                    else:
                        raise ArithmeticError(f'{animal.species} [{animal.id}] is only {animal.age} months old.  That\'s too young to be released!')
                else:
                    raise AttributeError(f'{animal.species} [{animal.id}] cannot live in a forest!')
            else:
                raise Exception(f'Not enough room for {animal.species} [{animal.id}]!')
        except (ArithmeticError, AttributeError, Exception) as err:
            print(err)
            raise
            input('Press enter to continue...')

    def add_plant(self, plant):
        try:
            if len(self.plants) < self.plant_capacity:
                if plant.sunlight.lower() == 'shade':
                    self.plants.append(plant)
                    print(f'{plant.species} was added to the forest!')
                    input('Press enter to continue...')
                else:
                    raise AttributeError('Plant cannot grow in the forest!')
            else:
                raise AttributeError('Forest has reached plant capacity!')
        except AttributeError as err:
            print(err)

            input('Press enter to continue...')
