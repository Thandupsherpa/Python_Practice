class BankAccount:
    
    def __init__(self,holder,balance):
        self.holder = holder
        self.balance = balance
        
    def deposit(self,amount):
        password = "Thandup@2007"
        username = self.holder
        while True:
            user = input("Enter your username: ")
            passwrd = input("Enter your password: ")
        
            if (user == username and passwrd == password):
              if amount > 0:
                self.balance+=amount
                return f"{amount} added"
              else:
                print("Insufficient amount!!")
            else:
              print("Incorrect password")
        
        
            
        
        
    def withdraw(self,amount):
        password = "Thandup@2007"
        username = self.holder
        user = input("Enter your username: ")
        passwrd = input("Enter your password: ")
        
        
        
        
        if amount<=self.balance:
            self.balance = self.balance - amount
            
    def checkBalance(self):
        print(self.balance)
        
holderOne = BankAccount("Thandup",1000)
print(holderOne.deposit(1000))
print(holderOne.withdraw(1000))
print(holderOne.checkBalance())
        
        