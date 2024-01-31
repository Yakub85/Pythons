class OverTheLimitException(Exception):
    def __init__(self,msg) :
        self.msg = msg


def withdraw(amount):
    if(amount>500):
        raise OverTheLimitException("You can't withdraw more than 500$ per day.")
    else:
        print("Succesfully Withdraw")
withdraw(600)