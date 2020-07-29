from animals import GoldDustDayGecko
from animals import RiverDolphin
from animals import NeneGoose
from animals import Kikakapu
from animals import Pueo
from animals import Ulae
from animals import Opeapea
from animals import HappyFacedSpider
import os


def build_release_animal_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
        "\u001b[47m\u001b[30;1m+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-")
    print("+ C H O O S E  A N I M A L  F O R  R E L E A S E +")
    print(
        "+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-\u001b[0m\n")

    print("\u001b[32m1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider\u001b[0m\n")


def release_animal(arboretum):
    build_release_animal_menu()
    animal = None
    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = GoldDustDayGecko()
    if choice == "2":
        animal = RiverDolphin()
    if choice == "3":
        animal = NeneGoose()
    if choice == "4":
        animal = Kikakapu()
    if choice == "5":
        animal = Pueo()
    if choice == "6":
        animal = Ulae()
    if choice == "7":
        animal = Opeapea()
    if choice == "8":
        animal = HappyFacedSpider()
    build_biome_choices(animal, arboretum, True)


def build_biome_choices(animal, arboretum, space_available):
    available_biomes = list()
    if space_available == False:
        print("****   That biome was not large enough   ****")
        print("****     Please choose another one      ****\n")
    for (key, value) in arboretum.__dict__.items():
        if type(value) is list:
            for index, biome in enumerate(value):
                biome.original_index = index
                biome.arboretum_domain = key
                available_biomes.append(biome)

    if len(available_biomes) == 0:
        print('There are no biomes available.\n')
    else:
        print(
        "\u001b[47m\u001b[30;1m+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++")
        print("+ A  V  A  I  L  A   B   L   E    B  I  O  M  E  S +")
        print(
            "+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++\u001b[0m\n")
        for index, biome in enumerate(available_biomes):
            print(
                f'{index + 1}. {biome} [{biome.id}] ({len(biome.animals)} animals)')
    handle_biome_choice(available_biomes, animal, arboretum)

def handle_biome_choice(available_biomes, animal, arboretum):
    print(f"Choose biome to release {animal.species} [{animal.id}] or enter x to go back.")
    choice = input("> ")
    if choice == "x":
        pass
    else:
        index = int(choice) - 1
        selected_biome = available_biomes[index]
        original_biome_index = selected_biome.original_index
        original_arboretum_domain = selected_biome.arboretum_domain
        try:
            selected_list = arboretum.get_list(original_arboretum_domain)
            selected_list[original_biome_index].add_animal(animal)
        except ArithmeticError:
            input('Press enter to continue...')
            pass
        except AttributeError:
            input('Press enter to continue...')
            os.system('cls' if os.name == 'nt' else 'clear')
            build_biome_choices(animal, arboretum, True)
        except Exception:
            input('Press enter to continue...')
            os.system('cls' if os.name == 'nt' else 'clear')
            build_biome_choices(animal, arboretum, False)