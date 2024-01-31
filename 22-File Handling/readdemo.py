f = open("sample.txt","r")
print(f.read())
f.seek(0)
i=0
while i < 3:
    print(f.readline())
    i = i+1
f.seek(0)
print(f.readline())


