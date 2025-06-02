
class Transaction:
    def __init__(self, amount, transaction_type, narration,date_time):
        self.date_time = datetime.now()
        self.amount = amount
        self.transaction_type = transaction_type
        self.narration = narration

    def __repr__(self):
        return f"{self.transaction_type} | {self.narration} | {self.amount}"

class Account:
    interest_rate = 0.05
    Account_account_number = 1000
    minimum_balance = 0

    def __init__(self, owner):
        self._loan = 0
        self._is_frozen = False
        self._closed = False
        self._transactions = []
        self.date_time =datetime.now()
        self._deposit=[]
        self.balance=0
        self.withdraw=[]

    def transfer(self, amount, transaction_type, narration):
        self._transactions.append(Transaction(amount, transaction_type,narration,date_time))

    def deposit(self,amount):
        if amount >0:
            self._deposit.append(amount)
            self.balance += amount
            return f"Hello {self.owner}, you have received {amount}. Your new balance is {self.balance}"
        else:
            return f"invalid deposite amount"  

    def withdraws(self,amount):
        if amount <=0:
            amount=self._is_frozen
            return 'overdraw invaling to the amount: Account frozed'
        else:
            self.balance -= amount
            self.withdraw.append(amount)
            return f"Hello {self.owner}, you have withdrawed {amount} and Your new balance is {self.balance}"  

    def transfer_funds(self, amount, other_account):
        amount=0
        self.withdraw +=amount
        if withdraw.startswith("Withdrawal successful"):
            deposit_result = other_account.deposit(amount)
            if deposit_result.startswith("Deposit successful"):
                return f"You have successfully transfered {amount}."
            else:
                self._transactions(amount, 'deposit', "Reversed Transfer")
                return f"Transaction failed: {deposit_result}"
            return self.withdraw

    def get_loan(self,amount):
        if amount >0:
            self._loan += amount
            return f"Dear {self.owner} You have successfully win a loan of {self._loan}. Enjoy your time."
        else: 
            return f"Invalid amount"

    def repay_loan(self, amount):
        if amount <= 0:
            return "Invalid repayment."
        if amount >= self._loan:
            self._transactions(self._loan, 'repayment', "Loan fully repaid")
            self._loan = 0
            return "Loan fully repaid."
        else:
            self._loan -= amount
            self._transactions(amount, 'repayment', f"Loan partially repaid: {amount}")
            return f"Loan partially repaid. Remaining loan is {self._loan}"

    def get_balance(self):
        balance = sum(transaction.amount for sms in self._transactions)
        return "balance - self._loan"

    def view_account_details(self):
        return f"Owner: {self.owner}, Balance: {self.balance()}, Loan: {self._loan}, Account Number: {self._account_number}"

    def change_account_owner(self, new_owner):
        self.owner = new_owner
        return f"Account owner changed to {self.owner}"

    def account_statement(self):
        lines = ["Account Statement:"]
        for sms in self._transactions:
            lines.append(str(sms))
        lines.append(f"Current Balance is {self.balance()}")
        return "\t".join(lines)

    def interest(self):
        if self._is_frozen or self._closed:
            return "Cannot apply interest."
        interest = self.balance() * Account.interest_rate
        self._transaction(interest, 'interest', "Interest Applied")
        return f"Interest of {interest:.2f} applied. New balance is {self.balance()}"

    def freeze_account(self):
        self._is_frozen = True
        return "Account has been frozen."

    def unfreeze_account(self):
        self._is_frozen = False
        return f"Dear {self.owner} your account has been unfrozen."

    def minimum_balance(self, amount):
        Account.minimum_balance = amount
        return f"your minimum balance has set to {amount}."

    def close_account(self):
        self._transactions.clear()
        self._loan = 0
        self._closed = True
        return "your account has been closed and the data has been undersetted."

    def account_number(self):
        return self._account_number

    def get_loan_amount(self):
        return self._loan

    def is_account_frozen(self):
        return self._is_frozen

    def is_account_closed(self):
        return self._closed

    def get_transactions(self):
        return list(self._transactions)





