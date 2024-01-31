#use parameterized constructor
class Course:
    #constructor method with parameters
    def __init__(self,name,ratings):
        self.name = name
        self.ratings = ratings
    
    #Instance method to calculate avg rating  
    def average(self):
        numberOfRating = len(self.ratings)
        average = sum(self.ratings)/numberOfRating
        print(f'Average Rating for {self.name}is {average}')
        
c1 = Course("Java",[4,5,3,4,5])
print(c1.name)
print(c1.ratings)
c1.average()

c2 = Course("Python",[4,5,5,4,5])
print(c2.name)
print(c2.ratings)
c2.average()