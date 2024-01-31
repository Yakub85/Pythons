import time, datetime
epochsecond = time.time()
print(epochsecond)

t= time.ctime(epochsecond)
print(t)

dt = datetime.datetime.today()
print(f"Current Date:{dt.day}/{dt.month}/{dt.year}")
print(f"Current Time:{dt.hour}:{dt.minute}:{dt.second}")
