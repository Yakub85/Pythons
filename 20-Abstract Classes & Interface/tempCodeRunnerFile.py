class FiveSeries(BMW):
    
    def __init__(self,parkingAssistEnabled, make, model, year):
        #using super() method self not include in constructor
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled
        
    def drive(self):
        print("FiveSeries is being driven")


        