sub1  = int(input("Enter marks 1: "))
sub2  = int(input("Enter marks 2: "))
sub3  = int(input("Enter marks 3: "))

total = (sub1+sub2+sub3)/3

if(total>=30):
    print(f"pass {total}")
elif(total<30):
    print(f"fail {total}")
else:
    print("invalid marks")