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

# try:
#     if __name__ == "__main__":
#         person_1 = Person("12345")
#         print(person_1) 
# except Exception as e:
#     print(e) 
    
#     test_id = "1234" 
#     test_name = "test_name"
#     test_age = 90 

#     person = Person( test_id)
#     print(person) 
#     if person.getId() != test_id:
#         print("Error: Age should be " + test_id + " but i got " + person.getId())
#     if person.getName() != test_name:
#         print("Error: Name should be " + test_name + " but i got " + person.getName())
#     if person.getAge() != test_age:
#         print("Error: Height should be " + str(test_age) + " but i got " + str(person.getAge()))
     
