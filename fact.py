#Recursive
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)
n = int(input("Enter number: "))
print(factorial(n))
#With loop
def loop(m):
    result = 1
    for i in range(1,m+1):
        result*=i
    return result
m = int(input("Enter number: "))
print(loop(m))