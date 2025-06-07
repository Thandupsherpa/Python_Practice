with open("file.txt") as f:
    content = f.read()
    # print(lines)
    if("show" in content):
        print("found")
    else:
        print("Not found")