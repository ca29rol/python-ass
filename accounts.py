class Account:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.deposit = []
        self.withdraw = []
        self.minimum_balance = 0
        self.instance_account = []
        self.loans=[]
       
    def deposits(self,amount):
        if amount >0:
            self.deposit.append(amount)
            self.balance += amount
            return f"Hello {self.name}, you have received {amount}. Your new balance is {self.balance}"
        else:
            return f"invalid deposite amount"   

        
    def withdraws(self,amount):
        if amount <=0:
            return 'overdraw invaling to the amount'
        else:
            self.balance -= amount
            self.withdraw.append(amount)
            return f"Hello {self.name}, you have withdrawed {amount} and Your new balance is {self.balance}"      

            
    def transfer(self,amount):
        self.balance -= amount
        self.instance_account.append(amount)
        return f"{amount} transfered to new account and the balance is {self.balance}"   

    def balances(self): 
        return f"Hello {self.name}, your balance is {self.balance}."


    def get_loan(self,amount):
        if amount >0:
            self.minimum_balance += amount
            return f"You have successfully win a loan of {self.minimum_balance}. Enjoy your time."
        else: 
            return f"Invalid amount"

    def repay_loan(self,amount):
        if amount > self.minimum_balance:
            self.loans.append(amount)
            return f"You have successfuly repay your balance"
        else:
            return f"insufficient amount to repay {self.minimum_balance} loan."     

    def account_details(self):
        return f"Hello {self.name}, you have ancount balance of {self.balance}, and you had a loan of {self.minimum_balance} and you repayied {self.loans}."      


    def update(self,new_name):
        self.name == new_name
        return f"Hello {new_name}"

    def account_statement(self):
        return f"Hello {self.new_name} your account balance is {self.balance}"

    def account_statements(self):    
        for i in self.instance_account:
            return f"your have transated {self.instance_account}"

    def interest_calculation(self,time):
        self.balance=self.balance*0.5*time
        return f"{self.balance}"

    def freeze(self,amount):
        if amount>self.balance:
            return f"Your account is freezed"
        else:
            return f"your account is unfreezed"

    def minimum_account_balance(self,amount):
        if amount < 0:
            return "Minimum balance can not be less than 0."
        else:
            self.min_balance = amount
            return f"Minimum balance set to {amount}"

    def close_account(self):
        self.balance = 0
        self.deposit = []
        self.withdraw = []
        self.minimum_balance = 0
        self.instance_account = []
        self.loans=[] 
        return f"Close account"     



    