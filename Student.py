from Person import Person
import utils
import os 

class Student(Person):
    def __init__(self):
        super().__init__()
        
        self.field_of_study = utils.getStringFromUser("Field of study")
        self.year_of_study = utils.getIntFromUser("year of study") 
        self.score_avg = utils.getIntFromUser("score avg")

     

    def getFieldOfStudy(self):
        return self.field_of_study


    def getYearOfStudy(self):
        return self.year_of_study
    

    def getScoreAvg(self):
        return self.score_avg
    

    def __repr__(self):
        return super().__repr__() + os.linesep + "  Field of study is: " + str(self.getFieldOfStudy()) + os.linesep + "  Year of study is: " + str(self.getYearOfStudy()) + os.linesep + "  Avg is: " + str(self.getScoreAvg())
    

    def getAsDict(self):
        my_dict = super().getAsDict()
        my_dict["Field of study"] = self.field_of_study
        my_dict["year of study"] = self.year_of_study
        my_dict["score avg"] = self.score_avg 
        return my_dict
    

if __name__ == "__main__":
    print("Error: This file should not be running. this is a class file")

