class Calculaor:
    def __init__(self,n):
        self.n = n
    
    def square(self):
        print(f"The square of {self.n} is {self.n**2}")
    
    def cube(self):
        print(f"The cube of {n} is {self.n**3}")
        
    def squareroot(self):
        print(f"The squareroot of {n} is {n*1/2}")
        
    @staticmethod
    def greet():
        print("Thankyou")
n = int(input("Enter a number: "))
a = Calculaor(n)
a.square()
a.cube()
a.squareroot()
    
        