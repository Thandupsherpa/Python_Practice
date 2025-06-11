# with open("file.txt") as f:
#     char = f.read()
#     vowels = "AEIOUaeiou"
#     count = 0
#     for i in char:
#         if i in vowels:
#             count+=1
        
# print(f" There are {count} numbers of vowels")    

def checkVowels(file):
    with open(file) as f:
        data = f.read()
        vowels = "AEIOUaeiou"
        count = 0
        for i in data:
            if i in vowels:
                count+=1
        return count
        
print(checkVowels("file.txt"))