# create a new class
class User:
    #Attributes are defined in a "magic method" called __init__
    #The first parameter of every method within a class will be self, 
    #and the class's attribute names are also indicated by self..
    #self.<<attribute_name_of_your_choosing>>
    def __init__(self):
        self.name = "Shehab"
        self.email = "shehabhassanien@hotmail.com"
        self.account_balance = 25000000

#instantiate a couple of new users
testUser = User()
devUser = User()

#access the instance's attribute
print(testUser.name) #Shehab

#set the values of the instance's attributes
testUser.name = "Hamza"
print(testUser.name)

# require attributes: when creating a class
class RequireUser:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter
#Now when we want to create users, we must send in the 2 required arguments:
shehab = RequireUser("Shehab Hassanien", "shehabhassanien@gmail.com")
print(shehab.name)	# output: Shehab Hassanien


#Methods
class MethodUser:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

shehab_method = MethodUser("Shehab Hassanien", "shehabhassanien@outlook.com")
shehab_method.make_deposit(100)
shehab_method.make_deposit(200)
shehab_method.make_deposit(50)
print(shehab_method.account_balance)