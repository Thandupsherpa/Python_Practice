word = ["donkey","kaam","baccha"]
with open("content.txt") as f:
    content = f.read()
    
for i in word:
        content = content.replace(i,"*"*len(i))
with open("content.txt","w") as f:
   
    f.write(content)