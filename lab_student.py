# lab_student.py
class LABStudent:

 def _init_(self, name, age, major):
    self.name = name
    self.age = age
    self.major = major

    def introduce(self):
        return f"I am {self.name}, {self.age} years old, majoring in {self.major}."
    
    def study(self):
        return f"{self.name} is studying {self.major}."