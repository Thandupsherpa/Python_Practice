with open("dummytext.txt") as f:
    lines = f.readlines()
    
lineno = 1
for line in lines:
    if("python" in line):
        print(f" Yes found the word python in line {lineno}")
        break
    lineno+=1
else:
    print("Not found")