class Product:
    
    def __init__(self):
        self.name = 'Keyboard'
        self.description = 'Using typing'
        self.price = 800
    
    def __del__(self):
         print("Inside the destructor")
         
         
    #instance method 
    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)
        
           
p1 = Product()
p1.display()

print("==================")
p2 = Product()
p2.display()

