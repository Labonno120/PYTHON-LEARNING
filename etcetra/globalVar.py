balance = 0
def deposit(n):
    global balance
    balance+=n
def withdraw(n):
    global balance
    balance-=n
deposit(100)
withdraw(50)
print(balance)