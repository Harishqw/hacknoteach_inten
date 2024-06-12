#Program to create an ATM.

print("Welcome to KASH Bank")
a=input("Enter your name:")
b=int(input("Enter your mobile number:"))
c=int(input("Enter your Aadhar card number:"))
d=input("Enter your email address:")
p=int(input("Enter a 4 digit pin of your choice:"))
print('''Congratulations!
you have successfully opened an account in our bank.
our bank has a policy of having a minimum balance of 100 when any new account is open ,so we request you to lodge certain amount''')
x=input("Want to enter online ATM(yes/check privacy policy):")
if x=="yes":                    #if-else statement.
    e=int(input('Enter the amount to be deposited:'))
    if e<100:                  
        print("MINIMUM AMOUNT IS 100. For further information contact the nearest KASH branch.")
    else:                       
        print('Amount deposited')
        y=0
        while y==0:             #while loop 
            f=input('Do you want to continue banking(yes/no):')
            if f=="yes":        #if-elif-else statement.
                print('''Select from following options:-
                Statement[s]
                Withdrawal[w]
                Remittance[r]
                Change PIN[p]
                LOG OUT[l]''')
                g=input("Your choice:")
                if g=="s":
                    print("Your bank balance is:",e)
                elif g=="w":
                    h=int(input("Enter the amount to be withdrawn:"))
                    if e<h:
                        print('INSUFFICIENT BALANCE!')
                    else:
                        e=e-h
                        print("Your current balance is:",e)
                        print("A message is sent to your registered mobile number.")
                elif g=="r":
                    i=int(input("Enter the amount to be remitted:"))
                    e=e+i
                    print("Your current bank balance is:",e)
                elif g=="p":
                    j=int(input("Enter your old pin:"))
                    if j==p:
                        k=int(input("Enter a new 4 digit password:"))
                    else:
                        print("Incorrect password!")
                elif g=="l":
                    print("You have logged out successfully:")
                    break           #break-A jump statement.
                else:
                    print('Invalid option')
            else:
                break
else:
    print('''Our online banking system is highly encrypted and designed especially for your quick and safe access.
you need not worry about the crackers online fetching for benefits. We have thousands of highly paid intellectual hackers for the encryption purpose.
Happy online banking.''')
print('THANK YOU')
print('Ensure logging out before leaving')