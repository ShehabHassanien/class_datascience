class User:	
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the make_deposit method
    def make_deposit(self, amount):	
    	self.account_balance += amount	
    # adding the make_withdrawal method
    def make_withdrawal(self, amount):	
    	self.account_balance -= amount	# have this method decrease the user's balance by the amount specified
    #display user
    def display_user_balance(self):
        print("User:", self.name, "Balance:", self.account_balance)
    #Transfer
    def transfer_money(self, user, amount):
        self.account_balance -= amount
        print("User 1:", self.name, "Balance:", self.account_balance)
        user.account_balance += amount
        print("User 2:", user.name, "Balance:", user.account_balance)
    
shehab = User("Shehab Hassanien", "shehabhassanien@outlook.com")
hamza = User("Hamza Hassanien", "hamzahassanien@gmail.com")
zainab = User("Zainab Hassanien", "zainabhassanien@yahoo.com")

shehab.make_deposit(100)
shehab.make_deposit(200)
shehab.make_deposit(500)
shehab.make_withdrawal(150)

hamza.make_deposit(1000)
hamza.make_deposit(900)
hamza.make_withdrawal(200)
hamza.make_withdrawal(100)

zainab.make_deposit(5000)
zainab.make_withdrawal(150)
zainab.make_withdrawal(200)
zainab.make_withdrawal(100)

shehab.display_user_balance()
hamza.display_user_balance()
zainab.display_user_balance()
print("-"*50, "transfer 1")
shehab.transfer_money(hamza, 50)
print("-"*50, "transfer 2")
shehab.transfer_money(zainab, 50)