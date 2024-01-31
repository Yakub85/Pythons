from datetime import*


d = date(2024,1,16)
t = time(22,6)

dt = datetime.combine(d,t)
print(dt)