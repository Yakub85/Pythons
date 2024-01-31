#use parameterized constructor
class Course:
    #constructor method with parameters
    def __init__(self,name,ratings):
        self.name = name
        self.ratings = ratings
    
        
c1 = Course("Java",[1,2,3,4,5])
print(c1.name)
print(c1.ratings)

c1 = Course("Python",[1,2,3,4,5])
print(c1.name)
print(c1.ratings)
        