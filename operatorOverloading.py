class Number:
    def __init__(self,n):
        self.n = n
    
    def __add__(self,num):
        return self.n + num.n

    def __sub__(self,num):
        return self.n - num.n
    
    def __mul__(self,num):
        return self.n * num.n
    
    def __truediv__(self,num):
        return self.n / num.n
    
    def __floordiv__(self,num):
        return self.n // num.n
    
num1 = Number(10)
num2 =Number(20)

print(num1-num2)
print(num1+num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)
