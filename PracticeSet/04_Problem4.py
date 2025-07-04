def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
n = int(input("Enter number you want factorial of: "))
print(factorial(n))

def sumnum(m):
    if(m==0 or m==1):
        return 1
    else:
        return m+sumnum(m-1)
    
print(sumnum(4))

def fibonacci(f):
    if(f ==0 ):
        return 0
    elif(f ==1):
        return 1
    else:
        return fibonacci(f-1) + fibonacci(f-2)
print(fibonacci(4))


