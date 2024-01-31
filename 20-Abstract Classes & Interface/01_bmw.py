from abc import abstractmethod,ABC
class BMW(ABC):
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        print("Starting the car") 
    
    def stop(self):
        print("Stopping the car")   
    
    @abstractmethod
    def drive(self):
        pass    
        
class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled, make, model, year):
        BMW.__init__(self,make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled
        
    def display(self):
        print(self.cruiseControlEnabled)
    #overidng start function
    def start(self):
        super().start()
        print("Button Start") 
    def drive(self):
        print("ThreeSeries is being driven")

class FiveSeries(BMW):
    def __init__(self,parkingAssistEnabled, make, model, year):
        #using super() method self not include in constructor
        super().__init__(make, model, year)
     
        self.parkingAssistEnabled = parkingAssistEnabled
    def drive(self):
        print("FiveSeries is being driven")


        
threeSeries=ThreeSeries(True,"BMW","328i","2018")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.display()
print("===================")
fiveSeries = FiveSeries(True,"BMW","328i","2019")
print(fiveSeries.parkingAssistEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)
fiveSeries.drive()
