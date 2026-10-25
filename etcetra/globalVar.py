
class Account:
    def __init__(self):
        self._balance = 0
    @property
    def balance(self):
        return self._balance
    def deposit(self,n):
        self._balance+=n
    def withdraw(self,n):
        self._balance-=n
    
    
account = Account()
account.deposit(100)
account.withdraw(20)
print(account.balance)