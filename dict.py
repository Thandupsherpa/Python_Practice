try:
    words = {
        "banana":"kera",
        "grapes":"angoor",
        "guava":"ambak"
    }
    word = input("Enter the fruit you want to translate: ")
    print(words[word])
except KeyError:
    print("Error")
    
dict ={
    
}
name1 = input("Enter favourate langauge: ")
name2 = input("Enter favourate langauge: ")
name3 = input("Enter favourate langauge: ")
name4 = input("Enter favourate langauge: ")
dict.update({"than":name1,
             "umesh":name2,
             "ankit":name3,#This key  gets overwrite by the below ankit
             "ankit":name4
             })

print(dict)
print(dict['ankit'])



