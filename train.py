class Train:
    seats = 10
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        if(self.seats!=0):
            print(f"There was {self.seats} available  so the seat has been booked for {self.name}")
            Train.seats-=1
        else:
            print("Out of seats")
            
    def status(self):
        print(f"There are {self.seats}  seats available now")
        
            
    @staticmethod
    def info():
        print("Train running under indian railways")
        
passanger1 = Train("Thandup",7365398476)
passanger1.status()
passanger1.info()

passanger2 = Train("Amit",7365398476)
passanger2.status()
passanger2.info()

passanger3 = Train("Ankit",7365398476)
passanger3.status()
passanger3.info()

passanger4 = Train("Umesh",7365398476)
passanger4.status()
passanger4.info()


        