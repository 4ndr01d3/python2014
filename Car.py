class Car:
    brand=None
    model=None
    year=None
    engine=None
    def __init__(self, brand, model, year,engine):
        self.brand = brand
        self.model = model
        self.year  = year    
        self.engine = engine
        
    def toString(self):
        return "BRAND= "+self.brand+"\nMODEL: "+self.model+"\nYEAR: "+self.year+"\nENGINE="+self.engine.toString()