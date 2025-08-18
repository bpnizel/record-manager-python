import pandas as pd 
from Person import Person
from Employee import Employee 
from Student import Student
from Menu_enum import Menu
import utils 

def printEntryDetails(entry_obj: Person | Student | Employee) -> None:
    print(entry_obj) 



def saveNewEntry(entries: dict, index_list: list) -> int:
    person_types = [Person, Employee, Student] 
    for index, class_type in enumerate(person_types):
        print(str(index) + ". " + class_type.__name__)
        
    try:
        user_input = utils.getIntFromUser("Choose a type")

        if user_input < 0 or user_input >= len(person_types):
            print("Error: choice out of range.") 
            return 0
    except (NameError, TypeError) as e:
        print(e)
        return 0
    
    try:
        new_entry = person_types[user_input]()
    except Exception as e:
        print(e)
        return 0
    
    if new_entry.getId() in entries:
        print("Error: ID already exists " + str(new_entry.getId()))
        return 0
    
    entries[new_entry.getId()] = new_entry
    index_list.append(new_entry.getId()) 

    print("ID [" + str(new_entry.getId()) + "] saved successfully")
    return new_entry.getAge()
 

def searchById(entries: dict) -> None:
    wanted_id = utils.getIntFromUser("Please enter the ID you want to look for")

    if wanted_id in entries:

        printEntryDetails(entries[wanted_id])  #Function call
    else:
        print("Error: ID " + str(wanted_id) + " is not saved. ")
 

def printAgesAverage(total_ages: int, entries: dict) -> None:
    if len(entries) == 0:
        print(0)
    else:
        average = total_ages / len(entries)
        print(average)


def printAllNames(entries: dict) -> None:
    if not entries:
        print("There are no names to display right now")
        return 
    for index, entry_obj in enumerate(entries.values()):
        print(str(index) + ". "  +  str(entry_obj.getName()))


def printAllIds(entries: dict) -> None:
    if not entries:
        print("There are no ids to display right now")
        return 
    for index, entry_obj in enumerate(entries.values()):
        print(str(index) + ". " + str(entry_obj.getId()))


def printAllEntries(entries: dict) -> None:
    if not entries:
        print("There are no entries to display right now")
        return 
    
    for index, entry_obj in enumerate(entries.values()):
        print(str(index) + ".")
        printEntryDetails(entry_obj)


def printEntryByIndex(entries: dict, index_list: list) -> None:
    int_index_to_return = utils.getIntFromUser("Please enter the index of entry you want to print")

    last_index = len(entries) - 1
    if int_index_to_return < 0 or int_index_to_return > last_index:
        print ("Error: index out of range. the maximum index allowed is " + str(last_index))
        return
    
    id = index_list[int_index_to_return] 
    printEntryDetails(entries[id]) # Function call


def printAllDataToCSV(entries: dict):
    file_name = input("What is your output file name? ")
    if not file_name.endswith(".csv"):
        file_name += ".csv"

    data_list = []
    for entry_obj in entries.values():
        data_list.append(entry_obj.getAsDict()) 

    df = pd.DataFrame(data_list)
    df.to_csv("C:\\Users\\pnize\\Desktop\\nadav_python\\Advanced\\final_project_advanced\\" + file_name, index=False)
    

def exitProgramEntries() -> bool:
    while True:
        exit_input = input("Are you sure? y/n ") 
        if exit_input == "n":
            return False
        elif exit_input == "y":
            print("Goodbye!") 
            return True


def main() -> None:
    entries = {}
    index_list = []
    total_ages = 0
    while True:
        Menu.printMenu()
        try:
            choice = utils.getIntFromUser("Please enter your choice")
            if choice > len(Menu):
                print("option [" + str(choice) + "] does not exist. please try again")
                continue             
            choice = Menu(choice)
        except Exception as e:
            print(e)
            continue

        if choice == Menu.SAVE_NEW_ENTRY:
            total_ages += saveNewEntry(entries, index_list) 
        elif choice == Menu.SEARCH_BY_ID:
            searchById(entries)
        elif choice == Menu.PRINT_AGES_AVERAGE:
            printAgesAverage(total_ages, entries)
        elif choice == Menu.PRINT_ALL_NAMES:
            printAllNames(entries)
        elif choice == Menu.PRINT_ALL_IDS:
            printAllIds(entries)
        elif choice == Menu.PRINT_ALL_ENTRIES:
            printAllEntries(entries)    
        elif choice == Menu.PRINT_ENTRY_BY_INDEX:
            printEntryByIndex(entries, index_list)
        elif choice == Menu.SAVE_ALL_DATA:
            printAllDataToCSV(entries) 
        elif choice == Menu.EXIT:
            if not exitProgramEntries():
                continue
            break

        input("Press Enter to continue  ") 

try:
    main()
except KeyboardInterrupt:
    print("The program has stopped.")
