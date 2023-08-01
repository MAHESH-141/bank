# bank operation using oop


## account creation

class bank:
      # create static variable
      bankname="Indian Express Bank"
      branch="A23,BBSR,India"
      
      # create account using constructer
      def __init__(self,username,pan,address):
            self.username=username
            self.pan=pan
            self.address=address
            self.balance=0.0
            print(f'hello {self.username} cong! your account created sucessfully')

## deposit
      def deposit(self,amount):
            self.balance=self.balance+amount
            print(f'{amount} deposited sucessfully')


## withdraw
      def withdraw(self,amount):
            if amount<self.balance:
                  self.balance=self.balance-amount
                  print(f'{amount} withdraw sucessfully')
      
            else:   
                  print('insufficent fund......')         


## ministatement
      def ministatement(self):
                  print(f'your account balance is {self.balance}')


print(f'welcome to {bank.bankname},{bank.branch}')    
# collect user data for account creation        
username=input('enter your name:') 
pan=input('enter pan card number:')
address=input('enter your address:') 
            
b=bank(username,pan,address)     # object creation based on user provided data


while True:
      print('please select any option')
      print('1.deposite\n 2.withdraw\n 3.ministatement\n 4.stop')
      option=int(input(''))
      
      if option==1:
            amount=float(input('enter deposited amount:'))
            b.deposit(amount)
      
      if option==2:
         amount=float(input('enter deposited amount:'))
         b.withdraw(amount)   
      
      if option==3:
            b.ministatement()
            
      if option==4:
            print('thans for using indian express bank')      
            break
      else:
            print('invalid option plz select a valid option\n')