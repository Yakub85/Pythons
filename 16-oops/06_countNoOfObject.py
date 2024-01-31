class ObjectCounter:
    numberOfObject = 0
    
    def __init__(self):
        ObjectCounter.numberOfObject+=1
        
    @staticmethod
    def displayCount():
        print(ObjectCounter.numberOfObject)

obj1 = ObjectCounter()
obj2 = ObjectCounter()

obj1.displayCount()
obj2.displayCount()