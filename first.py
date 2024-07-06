class User:
    def __init__(self ,firstname ,lastname):
      self.fname = firstname
      self.lname = lastname
    def fullname(self):
       print(f"my fullname is {self.fname}{self.lname}")
  

class Student(User):
    def __init__(self, firstname, lastname ,email):
       super().__init__(firstname, lastname)
       self.email =email
    
    def fullname(self):
       print("I am a student")
       return super().fullname()
    

    
s1 = Student("Maliha " ,"Shahi" ,"maliha@gmail.com")
s1.fullname()