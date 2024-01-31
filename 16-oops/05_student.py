class Student:
    
    major = "CSE"
    
    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name
    
s1 = Student(1,"Yaqub Ansari")
s2 = Student(2,"Zafrul Ubaid Ansari")

print(s1.rollno)
print(s1.name)
print(s1.major)
print()
print(s2.rollno)
print(s2.name)
print(s2.major)
        