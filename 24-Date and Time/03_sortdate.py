from datetime import date
import time


startTime= time.perf_counter()


ldate =[]
d1= date(2024,8,12)
d2= date(2021,8,12)
d3= date(2022,5,12)
d4= date(2023,8,12)
d5= date(2024,9,12)

ldate.append(d1)
ldate.append(d2)
ldate.append(d3)
ldate.append(d4)
ldate.append(d5)

ldate.sort()

time.sleep(3)
for d in ldate:
    print(d)
   
   
endTime = time.perf_counter() 
print("Execution Time:",endTime-startTime)


# s = "Hello World!"
# for i in s:
#     print(i,end="")
#     time.sleep(0.2)