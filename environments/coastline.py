from environments import Biome


class Coastline(Biome):

    def __init__(self):
        super().__init__('Coastline', 3, 15, 'Saltwater')

    def add_animal(self, animal):
        try:
            if len(self.animals) < self.animal_capacity:
                if (hasattr(animal, 'cell_type') and animal.cell_type == "hypotonic") or hasattr(animal, 'is_euryhaline'):
                    if animal.age >= animal.minimum_release_age:
                        self.animals.append(animal)
                        print(f'{animal.species} [{animal.id}] was added to the coastline!')
                        input('Please press enter to continue...')
                    else:
                        raise ArithmeticError(f'{animal.species} [{animal.id}] is only {animal.age} months old.  That\'s too young to be released!')
                else:
                    raise AttributeError(f'{animal.species} [{animal.id}] cannot live on a coastline!')
            else:
                raise Exception(f'Not enough room for {animal.species} [{animal.id}]!')
        except (ArithmeticError, AttributeError, Exception) as err:
            print(err)
            raise
            input('Press enter to continue...')
