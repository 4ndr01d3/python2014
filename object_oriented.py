import Car

class Engine:
    def __init__(self, capacity, combustible):
        self.combustible  = combustible
        self.capacity  = capacity
    def toString(self):
        s = "\n\tCOMBUSTIBLE: "+self.combustible
        return s + "\n\tCAPACITY: "+str(self.capacity)+"cc"



class Bakkie(Car.Car):
    capacity=None
    def toString(self):
        return Car.Car.toString(self)+"\nCAPACITY: "+self.capacity
    
    
    
myEngine=Engine(2000,"Petrol")

myCar=Car.Car("Mazda","323","1980",myEngine)
#anotherCar=Car("Renault","Clio","2005")
#mybakkie=Bakkie("Toyota","Hilux","2007")
#mybakkie.capacity="2000"
print myCar.toString()
#print anotherCar.toString()
#print mybakkie.toString()
