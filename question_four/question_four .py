# part a
def employee_bonus():

    run = 1

    while run == 1:

        salary =  int(input("Enter your salary amount: "))
        years_of_service =  int(input("Enter your years of service: "))

        if years_of_service > 4:

            net_bonus_amount = int((8/100 * salary))
            
        elif years_of_service== 3:

            net_bonus_amount = int((5/100 * salary))
        else:

           net_bonus_amount = 0

        finalPay = salary + net_bonus_amount    

        print(f"Your net bonus amount is: {net_bonus_amount:,} and your final pay is {finalPay:,}")    

        run = int(input("Press 1 to continue or any number to quit: "))

        if run !=1:
            break


employee_bonus()


# part b
def saccoTransactions():

    accountBalance = 0
    run = 1

    while run == 1:

        print("\nWelcome to, WITU Sacco.")

        
        print('1. Deposit Money')
        print('2. Withdraw Money')
        print('3. Check Balance')


        studentChoice = int(input("Enter your selection(1,2,or 3): "))

      

        if studentChoice == 1:

            print('\n...Processing a deposit transaction...')
            depositAmount =  int(input("Enter amount to be deposited: "))

            
            if depositAmount < 1000:

                print('\nMinimum deposit is 1000')

            else:
                accountBalance += depositAmount

                print(f'Dear student, you have deposited {depositAmount:,} and your new account balance is {accountBalance:,}')


        elif studentChoice == 2:
            print('\n...Processing a withdraw transaction...')
            withdrawAmount =  int(input("Enter amount to be withdrawn: "))

            if accountBalance == 0:

                print("Your balance is 0") 

            elif withdrawAmount < 500:

                print("Mininum withdraw amount is 500")

            elif withdrawAmount > accountBalance:

                print(f"Withdraw failed, insufficient funds")

            else:
                accountBalance -= withdrawAmount
                print(f'Dear student, you have withdrawn {withdrawAmount:,} and your new account balance is {accountBalance:,}')

            
        elif studentChoice == 3:
             print(f'Your account balance is {accountBalance:,}')

            

        else:
            print("You entered  a wrong choice!! Please select 1, 2, or 3\n")


        run = int(input("Enter 1 to continue or any number to exit: "))

        if run!=1:
            print("Thanks for using our sacco")
            break

saccoTransactions()

# part c
X1 = float(input("Enter the value of X1: "))
X2 = float(input("Enter the value of X2: "))
Y1 = float(input("Enter the value of Y1: "))
Y2 = float(input("Enter the value of Y2: "))
d = ((X2 - X1)**2 + (Y2 - Y1)**2)**0.5

print(d)
















