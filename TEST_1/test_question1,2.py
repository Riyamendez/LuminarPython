import functools
import re

f=open("C:/Users/Mendez/PycharmProjects/PythonDjangoLuminar/TEST_1/test1","r")
emp=[]
for i in f:
    test=i.rstrip("\n").split(",")
    emp.append(test)


class Employee:
    def __init__(self,eid,ename,edesig,mailid,salary):
        self.eid=eid
        self.ename=ename
        self.edesig=edesig
        self.mailid=mailid
        self.salary=salary


emplst=[]
for data in emp:
 obj=Employee(data[0],data[1],data[2],data[3],data[4])
 emplst.append(obj)

salarylst=list(map(lambda sal1:sal1.salary,emplst))

data=functools.reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,salarylst)
print("Maximum Salary:",data)






