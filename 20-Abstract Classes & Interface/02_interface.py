from abc import abstractmethod,ABC
class BMW(ABC):#interface class
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
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
    
    def stop(self):
        super().stop()
        print("Button Stop") 
           
    def drive(self):
        print("ThreeSeries is being driven")


class FiveSeries(BMW):
    
    def __init__(self,parkingAssistEnabled, make, model, year):
        #using super() method self not include in constructor
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled
      
    def start(self):
        super().start()
        print("Remote Start") 
    
    def stop(self):
        super().stop()
        print("Remote Stop") 
            
    def drive(self):
        print("FiveSeries is being driven")


        
threeSeries=ThreeSeries(True,"BMW","328i","2018")
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
fiveSeries.start()
fiveSeries.stop()
