class Employee:
    salary = ()
    def __init__(self,salary):
        self.salary = salary
        
    def increment(self,incrementPercent):
        newSal = self.salary + (self.salary*incrementPercent/100)
        return newSal
        
emp1 = Employee(500000)
print(emp1.increment(10))
    