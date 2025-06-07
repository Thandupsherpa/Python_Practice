import random
computer = random.randint(1,100)
print(computer)
you = int(input("Enter a number between 1-100: "))

for i in range(1,101):
    if(computer == you):
        print("****You won****")
        print(f"computer choosed {computer} you choosed {you} too")
        break
    else:
        print("You lose")
        print("Retry")
        break
