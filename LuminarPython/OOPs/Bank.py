class Bank:
    def __init__(self,accno,name,balance,bankname):
        self.accno=accno
        self.name=name
        self.balance=balance
        self.bankname=bankname
    def withdraw(self,amount):
        if(self.balance<amount):
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print("The remaining balance is",self.balance)
    def deposit(self,amount):
        self.balance+=amount
        print("The remaining balance is",self.balance)
    def balanceEnquiry(self):
        print("Account Number",self.accno)
        print("Name",self.name)
        print("Balance",self.balance)
        print("Bankname",self.bankname)
obj=Bank(1001,"Arjun",50000,"Sbi")
obj.withdraw(27000)
obj.balanceEnquiry()
