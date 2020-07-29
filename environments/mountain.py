from environments import Biome


class Mountain(Biome):

    def __init__(self):
        super().__init__("Mountain", 4, 6, "High Elevation")

    def add_animal(self, animal):
        try:
            if len(self.animals) < self.animal_capacity:
                if hasattr(animal, "is_mammal") and hasattr(animal,"wing_count"):
                    if animal.age >= animal.minimum_release_age:
                        self.animals.append(animal)
                        print(f'{animal.species} [{animal.id}] was added to the mountain!')
                        input('Please press enter to continue...')
                    else:
                        raise ArithmeticError(f'{animal.species} [{animal.id}] is only {animal.age} months old.  That\'s too young to be released!')
                else:
                    raise AttributeError(f'{animal.species} [{animal.id}] cannot live on a mountain!')
            else:
                raise Exception(f'Not enough room for {animal.species} [{animal.id}]!')
        except (ArithmeticError, AttributeError, Exception) as err:
            print(err)
            raise
            input('Press enter to continue...')

    def add_plant(self, plant):
        try:
            if len(self.plants) < self.plant_capacity:
                if plant.sunlight.lower() == "partial" and plant.insecticide_resistance.lower() == "high":
                    self.plants.append(plant)
                    print(f'{plant.species} was added to the mountain!')
                    input('Press enter to continue...')
                else:
                    raise AttributeError('Plant cannot grow on the mountain!')
            else:
                raise AttributeError(
                    'Mountain has already reached plant capacity!')
        except AttributeError as err:
            print(err)

            input('Press enter to continue...')
