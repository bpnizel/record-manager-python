def getStringFromUser(param: str) -> str:
    user_input = input(param + ": ")
    if user_input == "":
        raise NameError("Error: " + param + " cannot be empty, Try again.")
    elif not user_input.replace(" ", "").isalpha():
        raise NameError("Error: " + param + " must contain only letters.")
    return user_input
    

def getIntFromUser(param: str) -> int:
    user_input = input(param + ": ")
    if user_input == "":
        raise NameError("Error: " + param + " cannot be empty, Try again.")
    user_input = user_input.replace(",", "") 
    if not user_input.isdigit():
        raise TypeError("Error: " + param + " must be a number," + user_input + " is not a number.")
    return int(user_input)




if __name__ == "__main__":
    name = getStringFromUser("Name")
    field_of_study = getStringFromUser("Field of study")
    field_of_work = getStringFromUser("Field of work")
    print(name, field_of_study, field_of_work)

