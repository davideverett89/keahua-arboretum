import os
from environments import River


def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Forest")
    print("6. Mountain")

    choice = input("Choose your habitat > ")

    if choice == "1":
        river = River()
        arboretum.rivers.append(river)
    if choice == "2":
        pass
