from environments import Biome

class Grassland(Biome):

    def __init__(self):
        super().__init__("Grassland", 15, 22, {"little Rainfall", "No Shade"})
        

    def add_animal(self, animal):
        try:
            if len(self.animals) < self.animal_capacity:
                if hasattr(animal, 'species_type') and animal.species_type == "bird":
                    if animal.age >= animal.minimum_release_age:
                        self.animals.append(animal)
                        print(f'{animal.species} [{animal.id}] was added to the grassland!')
                        input('Please press enter to continue...')
                    else:
                        raise ArithmeticError(f'{animal.species} [{animal.id}] is only {animal.age} months old.  That\'s too young to be released!')
                else:
                    raise AttributeError(f'{animal.species} [{animal.id}] cannot live in a grassland!')
            else:
                raise Exception(f'Not enough room for this {animal.species} [{animal.id}]!')
        except (ArithmeticError, AttributeError, Exception) as err:
            print(err)
            raise
            input('Press enter to continue...')

    def add_plant(self, plant):
        try:
            if len(self.plants) < self.plant_capacity:
                if plant.sunlight.lower() == "partial" and plant.insecticide_resistance.lower() == "medium":
                    self.plants.append(plant)
                    print(f'{plant.species} was added to the grassland!')
                    input('Press enter to continue...')
                elif plant.sunlight.lower() == "full" and plant.insecticide_resistance.lower() == "high":
                    self.plants.append(plant)
                    print(f'{plant.species} was added to the grassland!')
                    input('Press enter to continue...')
            else:
                raise AttributeError('Grassland has already reached plant capacity!')
        except AttributeError as err:
            print(err)

            input('Press enter to continue...')