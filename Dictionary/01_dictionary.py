# student={
#     "name":"Yaqub",
#     "id":"A-8280"
# }
# print(student)
# print(type(student))

# # print(student["name"])
# student["name"]="Yaqub Ansari"
# # print(student["name"])

# # print(student.get("id"))

# # print(student.keys())
# # print(student.values())
# # print(student.items())
# student["course"]="MCA"
# student["age"]=24
# s=student.copy()
# print(student.clear())
# print(s.popitem())

lst=[1,2,3,4,2,2,3,3,3,1,4]
d={}
for i in lst:
    d[i]=lst.count(i)
    

for k,v in d.items():
   print(f"{k} occurrence {v} times.")
