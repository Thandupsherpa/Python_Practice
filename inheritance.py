# class Parent:
#     print("i am parent")

# class Clild(Parent):
#     pass

# test = Clild()
# test2 = Parent

# using super()

class ParentTwo:
    def __init__(self,fName,lName):
        self.fName = fName
        self.lName = lName
        
        
class ChildTwo(ParentTwo):
    def __init__(self,course, fName, lName):
        super().__init__(fName, lName)
        self.course = course
        
        
parent = ParentTwo("Thandup","Sherpa")
print(parent.fName,parent.lName)

clild = ChildTwo("Amit","Bhagat","Python")
print(clild.fName,clild.lName,clild.course)

