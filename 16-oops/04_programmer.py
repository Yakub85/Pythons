#Create Getter and Setter methods
class Programmer:
    
    #Setter Methods
    def setName(self,n):
        self.name = n
    
    #Getter Methods
    def getName(self):
        return self.name
    
    def setSallery(self,s):
        self.sallery = s  
        
    def getSallery(self):
        return self.sallery
    
    def setTechnologies(self,techs):
        self.technologies = techs  
        
    def getTechnologies(self):
        return self.technologies
    
p1 = Programmer()
p1.setName("Yaqub Ansari")
p1.setSallery(50000)
p1.setTechnologies(["C/C++","Python","JavaScript"])

print(p1.getName())
print(p1.getSallery())
print(p1.getTechnologies())