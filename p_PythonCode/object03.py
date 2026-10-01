class TaipeiBank:
    def __init__(self, balance=0): #初始化方法，預設帳戶餘額為0，建構方法/建構子/constructor
        self.balance = balance #帳戶餘額，初始為0
    def printBalance(self): #一般方法，列印帳戶餘額
        print(f"Current balance: {self.balance}")
t= TaipeiBank(2000) #類別變物件化，跟值初始化餘額
t.printBalance()

