from animals import Animal
from animals import Freshwater
from animals import Identifiable


class RiverDolphin(Animal, Freshwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "River dolphin", {
                        "Trout", "Mackarel", "Salmon", "Sardine"}, {"River", "Coastline"}, 13)
        Freshwater.__init__(self)
        Identifiable.__init__(self)

    # @property
    # def prey(self):
    #     return self.prey

    def feed(self, prey):
        if prey in self.prey:
            print(f'The dolphin ate {prey} for a meal')
        else:
            print(f'The dolphin rejects the {prey}')

    def __str__(self):
        return f'Dolphin {self.id}. Eeee EeeEEeeeeEE!'
