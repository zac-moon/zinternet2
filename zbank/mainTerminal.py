'''
Usercode - the quick login method (a simple sting often just the  2 names)
PIN and Card Number - Details for Card
Formated Name =  e.g. Zac Moon
Account Number - Used to transfer money to other users
'''
loggedIn = False

def bankMenu(usercodeTry, pinTry, cardNumberTry, formattedNameTry, accountNumberTry, loggedIn):
    done = False
    print("--------------------------")
    print("BANK MENU - ZBANK TERMINAL METHOD")
    while not done:
        userFile = "data_files/zbank/balances/" + accountNumberTry + ".txt"
        mode = input("Enter TRANSFER - BALANCE - CASHCHECK - QUIT: ")
        mode = mode.upper()

        with open(userFile) as file:
            balance = file.read()

        if mode == "QUIT":
            done = True

        elif mode == "BALANCE":
            print("Balance: " + balance)

        elif mode == "CASHCHECK":
            print("Sorry, feature not completed yet. Check in later to see how it's going on OR ZMail us at help@zbank.com")

        elif mode == "TRANSFER":
            sendTo = input("Enter Account Number of user you are transferring to: ")
            formattedSendTo = sendTo
            amountTransfer = input("Enter the amount to transfer: ")
            sendTo = "data_files/zbank/balances/" + sendTo + ".txt"
            sendFrom = userFile

            # Open and read the recipient's balance
            with open(sendTo) as file:
                transferToBalance = file.read()
            
            transferToBalance = int(transferToBalance)
            amountTransfer = int(amountTransfer)
            balance = int(balance)

            if amountTransfer > balance:
                print("Insufficient balance to complete the transfer.")
                continue

            # Update the recipient's balance
            newAmount = transferToBalance + amountTransfer
            with open(sendTo, "w") as file:
                file.write(str(newAmount))

            # Update your account balance
            newBalance = balance - amountTransfer

            with open(userFile, "w") as file:
                file.write(str(newBalance))

            with open(userFile) as file:
                balance = file.read()

            print(f"Transferred £{amountTransfer} to {formattedSendTo}. Your new balance: £{newBalance}")


while not loggedIn:
    for i in range(1, 63):
        print(" ")

    print("===========================")
    print("ZBANK Terminal")
    usercodeUsing = input("UserCode: ")
    accountNumberUsing = input("Account Number: ")
    if usercodeUsing == "zacmoon" and accountNumberUsing == "436118":
        bankMenu("zacmoon", "5095", "1234567812345678", "Zac Moon", "436118", True)
    elif usercodeUsing == "testacc"and accountNumberUsing == "783901":
        bankMenu("testacc","1234","8765432187654321","Test Account","783901",True)
    elif usercodeUsing =="lulumoon" and accountNumberUsing =="791224":
        bankMenu("lulumoon","6334","8764921033764978","Lulu Moon","791224",True)
    elif usercodeUsing =="cleomoon" and accountNumberUsing=="334601":
        bankMenu("cleomoon","9666","3764800463349710","Cleo Moon","334601",True)
    else:
        print("Incorrect UserCode or Account Number- Please Try Again")
        loggedIn = False
