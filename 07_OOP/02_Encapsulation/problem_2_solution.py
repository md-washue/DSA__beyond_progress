class BankAccount:
    def __init__(self,name,account_number, balence):
        self.name=name
        self.account_number=account_number
        self.__balence=balence

    def deposit(self, amount):
        self.__balence= self.__balence+amount
        print(f"Deposit successful: RM{amount}")

    def withdraw(self, amount):

        if(amount>self.__balence):
            print("Insufficient balance!")
        else:
            self.__balence=self.__balence-amount
            print(f"Withdrawal successful: RM{200}")
    def check_balance(self):
        return (print(f"Current balence: RM{1300}"))
        # return self.__balence

    


# account1 = BankAccount("Ali", "ACC001", 1000)
# # account1.balence=10000000000000000
# print(account1.name)
# print(account1.account_number)
# print(account1.balence)

account1 = BankAccount("Ali", "ACC001", 1000)

account1.deposit(500)
account1.withdraw(200)

account1.check_balance()
