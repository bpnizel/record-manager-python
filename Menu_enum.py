from enum import Enum, auto

class Menu(Enum):
    SAVE_NEW_ENTRY = auto()
    SEARCH_BY_ID = auto()
    PRINT_AGES_AVERAGE = auto()
    PRINT_ALL_NAMES = auto()
    PRINT_ALL_IDS = auto()
    PRINT_ALL_ENTRIES = auto()
    PRINT_ENTRY_BY_INDEX = auto()
    SAVE_ALL_DATA = auto()
    EXIT = auto()

    # def printMenu() -> None: 
    #     if Menu.SAVE_NEW_ENTRY:
    #         print("1. Save a new entry")
    #     if Menu.SEARCH_BY_ID:
    #         print("2. Search by ID")
    #     if Menu.PRINT_AGES_AVERAGE: 
    #         print("3. Print ages average")
    #     if Menu.PRINT_ALL_NAMES:
    #         print("4. Print all names")
    #     if Menu.PRINT_ALL_IDS:
    #         print("5. Print all IDs")
    #     if Menu.PRINT_ALL_ENTRIES:
    #         print("6. Print all entries")
    #     if Menu.PRINT_ENTRY_BY_INDEX:
    #         print("7. Print entry by index")
    #     if Menu.SAVE_ALL_DATA:
    #         print(". Save all data")
    #     if Menu.EXIT:
    #         print("9. Exit")

    def printMenu() -> None:
        for option in Menu:
            print(f'{option.value}. {option.name.replace("_", " ").title()}')



if __name__ == "__main__": 
    Menu.printMenu()


