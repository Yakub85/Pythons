# x = 12 #global variables
# def display():
#     y=54 #local Variable
#     print(x)
#     print(y)
#
# print(x)
# print(y)
# display()
#how to access global variable
x = 12 #global variables
def display():
    x=54 #local Variable
    print(x)
    print(globals()['x'])

print( x )
z = display
z()