import re 
str = "Take up one idea. one idea at a time"
res=re.search(r'o\w\w',str)
print(res.group())

res=re.findall(r'o\w\w',str)
print(res)