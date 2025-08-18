from Person import Person
import utils
import os

class Employee(Person):
    def __init__(self):
        super().__init__()
        self.field_of_work = utils.getStringFromUser("field of work")

        self.salary = utils.getIntFromUser("Salary")

        

    def getFieldOfWork(self):
        return self.field_of_work
    
    def getSalary(self):
        return self.salary

    
 
    def __repr__(self):
        return super().__repr__() + os.linesep + "  Field is: " + self.getFieldOfWork() + os.linesep + "  Salary: " + str(self.getSalary())
    
    def getAsDict(self):
        my_dict = super().getAsDict()
        my_dict["Field of work"] = self.field_of_work
        my_dict["Salary"] = self.salary
        return my_dict
    

if __name__ == "__main__":
    print("Error: This file should not be running. this is a class file")
     


