from .biome import Biome


class River(Biome):

    def __init__(self):
        Biome.__init__(self, "River", 6, 1, "Fresh Water")
        

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                self.animals.append(animal)
        except AttributeError:
            print("Cannot add non-aquatic, or saltwater animals to a river")
                
            input('Press enter to continue')

    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add plants that require brackish water or stagnant water to a river biome")
