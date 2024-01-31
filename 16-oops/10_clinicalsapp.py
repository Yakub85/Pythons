class Patient:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
        self.clinical = []
    def addClinicalData(self,clinical):
        self.clinical.append(clinical)   
 
 
        
class Clinical:
    def __init__(self,componentName,componentValue) :
        self.componentName = componentName
        self.componentValue = componentValue
        
p = Patient('John',35)
c1 = Clinical('bp','88/120')
p.addClinicalData(c1)

c2 = Clinical('HeartRate',60)
p.addClinicalData(c2)
print(p.name)
for eachClinical in p.clinical:
    print(eachClinical.componentName)
    print(eachClinical.componentValue)
    
p1 = Patient('Deo',40)
c3 = Clinical('sugar pp','130/160')
p1.addClinicalData(c3)

c4 = Clinical('sugar ff','70/120')
p1.addClinicalData(c4)
print(p1.name)
for eachClinical in p1.clinical:
    print(eachClinical.componentName)
    print(eachClinical.componentValue)