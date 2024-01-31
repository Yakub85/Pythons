s = input('Enter a string ')
print(s[::-1])
s = input('Enter a string ')
i = len(s)-1
res =''
while i>=0:
    res =res+s[i]
    i-=1
print(res)