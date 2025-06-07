word = "donkey"
with open("content.txt") as f:
    content = f.read()
with open("content.txt","w") as f:
    newContent = content.replace(word,"###")
    f.write(newContent)