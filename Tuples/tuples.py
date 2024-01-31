numbers=(3,1,-1,-3,-5,-7)
d=numbers[1]-numbers[0]

lst=list(numbers)
 
for i in range(3):
   lst.append(lst[-1]+d)

   
print(tuple(lst))   