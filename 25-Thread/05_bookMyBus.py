from threading import*

class BookMyBus: 
    
    def __init__(self, availableSeats ):
        self.availableSeats = availableSeats
        # self.l = Lock()
        self.l = Semaphore()
        
        
    def bookTicket(self,seatRequest):
        self.l.acquire()
        print("Total seats available:",self.availableSeats)
        if (self.availableSeats >= seatRequest):
            print("Confirm a seat")
            print("Proccesing the Payment")
            print("Printing the ticket")
            self.availableSeats=self.availableSeats-seatRequest
        else:
            print("Sorry! No seats available")
        self.l.release()   
  
        
obj = BookMyBus(10)
t1 = Thread(target=obj.bookTicket,args=(3,))
t2 = Thread(target=obj.bookTicket,args=(4,))
t3 = Thread(target=obj.bookTicket,args=(6,))

t1.start()
t2.start()
t3.start()