class Animals:
    def __init__(self):
        pass
        
class Pets(Animals):
    def __init__(self):
        super().__init__()
        pass
        
class Dog(Pets):
    def __init__(self,):
        super().__init__()
    
    @staticmethod    
    def does():
        do = "Barks"
        print(f"THe dog {do}")
        
ani1 = Dog()
ani1.does()