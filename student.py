# Add these methods to class student - full_name, year_of_birth, initials. Create two 
# instances and verify the work as expected
class Student :
    # name = "Cheko"
    # age = 20
    # country = "Kenya"
    school = "Akirachix"
    def __init__(self,first_name,last_name,age,country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def greet(self):
        return f"Hello {self.age} year old {self.name} from {self.country} welcome to the {self.school}."

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def year_of_birth(self):
        yob = 2022 - self.age
        return yob
    
    def initials(self):
        a = f"{self.first_name[0]} {self.last_name[0]}"
        b = a.upper()
        return b
