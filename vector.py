class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        
    def show(self):
        print(f"The vector is: {self.i}i+{self.j}j")
        
class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
        
    def show(self):
        print(f"The vector is: {self.i}i+{self.j}j+{self.k}k")
        

twoD1 = int(input("Enter the number 1: "))
twoD2 = int(input("Enter the number 2: "))
a = TwoDVector(twoD1,twoD2)
a.show()

threeD1 = int(input("Enter the number 1: "))
threeD2 = int(input("Enter the number 2: "))
threeD3 = int(input("Enter the number 3: "))
b = ThreeDVector(7,8,9)
b.show()

