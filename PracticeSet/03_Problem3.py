# using for loop
list1 = []
for i in range(1,101):
    if(i%3 == 0 and i%5 == 0):
        list1.append(i)
        
print(list1)

# using list comprehension
numbers = [x for x in range(1,101) if x%3==0 and x%5==0]
print(numbers)


num = [y**2 for y in range(1,11)]
print(num)

num = [y**3 for y in range(1,11)]
print(num)