class bankAccount:
    def __init__(self,balance):
        self.__balance = balance 

    def show_balance(self):
        print(self.__balance)

account = bankAccount(5000)
account.show_balance()