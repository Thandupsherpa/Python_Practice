num1  =int(input("Enter number: "))
num2 =int(input("Enter number: "))
num3  =int(input("Enter number: "))
if(num1>num2 and num1>num3):
    print(f"gratest is: {num1}")
elif(num2>num1 and num2>num3):
    print(f"gratest is: {num2}")
elif(num3>num1 and num3>num2):
    print(f"gratest is: {num3}")
else:
    print("invalid")
