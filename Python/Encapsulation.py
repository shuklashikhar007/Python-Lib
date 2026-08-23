#Encapsulation OOP in python
class Bankaccount :
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        self.balance -= amount
account = Bankaccount("Shikhar",10000)
account.deposit(50)
print(account.balance)
account.withdraw(1000)
print(account.balance)
