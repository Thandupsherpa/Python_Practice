class Employee:
    # def salary(self,name,amount):
    #     self.name = name
    #     self.amount = amount
    #     print(f"Salary of {name} is {amount}")
    company = "Google"
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
        
        
        
emp1 = Employee("Thandup",120000)
print(emp1.name,emp1.amount,emp1.company)



# emp2 = Employee()
# emp2.salary("Amit",1200000)