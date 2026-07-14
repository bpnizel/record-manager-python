import os
import utils
class Person: # The first letter  in class Upper 
    def __init__(self):
        self._id = utils.getIntFromUser("Enter ID")  # id value was checked in the main code(func saveNewEntry)
        self._name = utils.getStringFromUser("Name")
        self._age = utils.getIntFromUser("Age")
      

    def getId(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age
    
    def __repr__(self):
        return "  ID: " + str(self.getId()) + os.linesep + "  Name: " + self.getName() + os.linesep + "  Age: " + str(self.getAge()) 

    def getAsDict(self):
        return {"ID": self.getId(),
                "name": self.getName(),
                "age": self.getAge() } 
    


if __name__ == "__main__":
    print("Error: This file should not be running. this is a class file")


