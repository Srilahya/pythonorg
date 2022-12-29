def divide(a,b):
    try:
        c=a/b
        print(c)
    except:
        print("error")
divide(1,"LAHYA")


class negativeValueError(Exception):
    pass

class HigherValueError(Exception):
    def __str__(self):
        return "amount is greater than the balance"

class bank:
    def __init__(self,account_number,balance,holder_name):
        self.num=account_number
        self.bal=balance
        self.name=holder_name
    def withdraw(self,amount):
        try:
            if (amount <= self.balance):
                print("drawn successfully")

            else:
                raise HigherValueError
        except HigherValueError as ex:
            print(ex)



obj = bank(987654323459,50000,"lahya")
obj.withdraw(100000)