class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg = msg
        
class TooOldException(Exception):
    def __init__(self,msg):
        self.msg = msg
       
 
def checkEligibility(age):
    if age < 18:
        raise TooYoungException('You have to be 18 or older to apply')
    elif age > 60:
        raise TooOldException('You have to be younger than 60.')
    else:
        print("You are Eligible.") 
     
age = int(input("Enter your age: "))

checkEligibility(age)
     