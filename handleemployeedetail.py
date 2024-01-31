n = int(input("Enter the number of employee"))
employee = {}
for i in range(n):
    name = input('Enter employee name')
    salary = input('Enter employee salary')
    employee[name]=salary
while True:
    name = input('Enter employee name')
    salary = employee.get(name,-1)
    if salary==-1:
        print("Employee does not exist")
    else:
        print('The salary of the employee is ',salary)
    choice = input('Do you want to know the salary of an other emmployee[Yes/No]')
    if choice =='No':
        break