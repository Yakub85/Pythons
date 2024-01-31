#WAP to take a Tuple of Numbers from the keyword and print it's sum and average
t = eval(input("Enter Tuple of Numbers:"))
l = len(t)
sum = 0
for ele in t:
    sum = sum + ele
print("The Sum is: ",sum)
print("The Average is: ",sum/l)