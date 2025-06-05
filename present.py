username = input("Enter username: ")
count = len(username)

if(count<10):
    print(f"only has {count} characters")
elif(count>10):
    print("impressive")
else:
    print("invalid")