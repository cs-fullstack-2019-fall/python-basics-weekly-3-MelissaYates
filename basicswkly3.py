# Set up main menu command loop
userOption = -1 # declaring userOption as a variable
account_balance = 200.00 # declaring the inital balance of the account
# asking user for option to go on to other questions
userOption = input("Hello, please choose one of following options: \n" "1 Check balance \n""2 Add money to account \n""3 Withdraw money from account \n""4 Quit \n""What will you like to do? \n")

### Overall a very nice job! Your design notes could have used a bit more detail, but your code was
### solid except for using 2 different variables to represent the same running balance (do not need updated_balance variable to stick around)
### GREAT comments and you added some nice touches duing data input and validation.
###
### The updated account value is temporary and doesnt need to be kept around once the updated balance has been calculated.
### Just use one variable for account balance. That's all you need. See below for example of using just account_balance.
# updated_account = 0 # will hold the amount after user has either deposited of withdrawn to display the result

while userOption != '4':
    # If user chooses option 1 display current account balance that user has
    if userOption == '1':     # User selected check balance
        print(f"Your account has ${account_balance} dollars")
        #Ask user would they like to deposit any money into their account Y/N
    elif userOption == '2':
        deposit = input("Would you like to deposit some money? Y/N").upper() ### <<< Nice touch with input handling
        if deposit == 'Y':
            depositAmount = int(input('How much money would you like to deposit?')) # ask user the amount they would like to deposit
            # updated_account = updated_account + account_balance + depositAmount #totals the money after transaction
            account_balance += depositAmount #totals the money after transaction
            # print(f" Your account now holds ${updated_account} dollars.") #prints out total after transaction has been completed
            print(f" Your account now holds ${account_balance} dollars.") #prints out total after transaction has been completed
        else:
            print('Thank you for coming in today.') # false case if user chooses 'N'
    elif userOption == '3':
        withdrawal = int(input("How much money would you like to withdraw today?")) # ask user for amount they wish to withdraw
        if withdrawal<= account_balance:
            account_balance -= withdrawal #holds total after user has entered the amount they wish to withdraw
            # print(f"Your withdrawal amount is ${withdrawal} and your account balance is ${updated_account}") #gives the updated amount after transaction has been completed
            print(f"Your withdrawal amount is ${withdrawal} and your account balance is ${account_balance}") #gives the updated amount after transaction has been completed
        else:
            print("Insufficient funds.") #false case

    userOption = input("Hello, please choose one of following options: \n" "1 Check balance \n""2 Add money to account \n""3 Withdraw money from account \n""4 Quit \n""What will you like to do? \n")
