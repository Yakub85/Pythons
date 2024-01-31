from datetime import*
class Project:
    def __init__(self,name,sdate,edate):
        self.name = name
        self.sdate= sdate
        self.edate = edate
        
        self.task=[]
    def addTask(self,task):
        self.task.append(task)

class Task:
    def __init__(self,name,duration):
        self.name=name
        self.duration=duration
        self.resource=[]
    def addResource(self,resource):
        self.resource.append(resource)
       
       
class Resource:
    def __init__(self,name,skill):
        self.name= name
        self.skill = skill


project = Project("AI",date(2024,1,1),date(2024,1,3))
task =Task("Chat Bot",90)
resource = Resource("Yaqub","python")

project.addTask(task)
task.addResource(resource)

for t in project.task:
    print(t.name)
    for r in task.resource:
        print(r.name)
        print(r.skill)


# class Project:
#     def __init__(self,name,startDate,endDate):
#         self.name = name
#         self.startDate = startDate
#         self.endDate = endDate
#         self.task = []
        
#     def addTask(self,task):
#         self.task.append(task)
        
    
# class Task:
#     def __init__(self,name,duration):
#         self.name = name
#         self.duration = duration
#         self.resource = []
        
#     def addResource(self,resource):
#         self.resource.append(resource)
        
        
# class Resource:
#     def __init__(self,name,skill):
#         self.name = name
#         self.skill = skill
        
# project = Project("AI",date(2024,1,1),date(2024,1,3))
# task = Task("Chat Bot",90)
# resource = Resource("John","Python")

# project.addTask(task)
# task.addResource(resource)

# for eachTask in project.task:
#     print(eachTask.name)
#     print(eachTask.duration)
#     for eachResource in eachTask.resource:
#         print(eachResource.name)
#         print(eachResource.skill)