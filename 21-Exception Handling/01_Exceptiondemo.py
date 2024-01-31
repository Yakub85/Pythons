import logging

logging.basicConfig(filename="mylog.log",level=logging.DEBUG)
try:
    # a,b=[int(x) for x in input("Enter two number:").split()]
    f = open("myfile","w")
    a = int(input("Enter first number: "))
    b = int(input("Enter first number: "))
    logging.info("Division in progress")
    c = a / b
    f.write("Writing %d into file"%c)
   
    # print(c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero number")
    logging.error("Division by zero")
    
else:
    print("You have entered a non zero number")    
finally: 
    f.close()   
    print("File Close")
print("code after the exception")