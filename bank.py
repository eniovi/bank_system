menu = """
[d] Deposit
[w] Withdraw
[s] Statement
[q] Quit
"""

balance = 0
statement = ""
number_of_withdrawals = 0
VALUE_LIMIT = 500
WITHDRAWAL_LIMIT = 3

while True:
    option = input(menu)

    if option == "d":
        amount = float(input("Enter amount to deposit: "))

        if amount > 0:
            balance += amount
            statement += f"Deposit: R$ {amount:.2f}\n"
        else:
            print("Operation failed! The amount must be positive.")

    elif option == "w":
        amount = float(input("Enter amount to withdraw: "))

        exceed_balance = amount > balance
        exceed_value_limit = amount > VALUE_LIMIT
        exceed_withdrawals = number_of_withdrawals >= WITHDRAWAL_LIMIT

        if exceed_balance:
            print("Operation failed! You have exceeded balance.")
        elif exceed_value_limit:
            print("Operation failed! You have exceeded the withdrawal limit amount.")
        elif exceed_withdrawals:
            print("Operation failed! You have exceeded the maximum number of withdrawals.")
        elif amount > 0:
            balance -= amount
            statement += f"Withdraw: R$ {amount:.2f}\n"
            number_of_withdrawals += 1
        else:
            print("Operation failed! The amount must be positive.")

    elif option == "s":
        print("************** STATMENT **************")
        print("No transactions have been made." if not statement else statement)
        print("--------------------------------------")
        print(f"Balance: {balance:.2f}")
        print("**************************************")

    elif option == "q":
        break

    else:
        print("Invalid option. Please try again.")
