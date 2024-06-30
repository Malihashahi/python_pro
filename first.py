class Car:

    def __init__(self , name , price):
        self.name = name
        self.price = price

    def start(self):
        print(f"{self.name} is start")
    
    def off(self):
        print(f"{self.name} is off now")


        

        

car1= Car("benz" ,"230000")