# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 09:19:19 2020

@author: CEC
"""

class Employee:
    "Common base class for all employees"
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("total Employee %d" %Employee.empCount)
    def displayEmployee(self):
        print("Name:", self.name,", Salary: ",self.salary)
        
"this would create first object of Employee class"
emp1=Employee("Zara",2000)
emp2=Employee("Manni",5000)
emp3=Employee("Juan",1000)
emp4=Employee("Jose",2000)
emp5=Employee("Maria",3000)
emp6=Employee("Monica",4000)

emp1.displayEmployee()
print("Total Employee %d" % Employee.empCount)