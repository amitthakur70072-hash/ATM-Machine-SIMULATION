class InsufficientBalanceError(Exception):
    pass

class InvalidPINError(Exception):
    pass


balance = 5000
PIN = 1234
attempts = 3

# -------- PIN Authentication --------
while attempts > 0:
    try:
        user_pin = int(input("Enter your 4-digit PIN: "))
        if user_pin != PIN:
            attempts -= 1
            raise InvalidPINError("❌ Wrong PIN")
        else:
            print("✅ Login successful!")
            break

    except ValueError:
        print("❌ Please enter numbers only")

    except InvalidPINError as e:
        print(e)
        print(f"Attempts left: {attempts}")

    except KeyboardInterrupt:
        print("\n❌ Program interrupted by user")
        exit()

else:
    print("🚫 Card blocked. Too many wrong attempts.")
    exit()

# -------- ATM Menu --------
while True:
    try:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("💰 Current Balance:", balance)

        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                raise InsufficientBalanceError("❌ Insufficient Balance")
            if amount <= 0:
                raise ValueError("❌ Invalid amount")
            balance -= amount
            print("✅ Please collect your cash")
            print("💰 Remaining Balance:", balance)

        elif choice == 3:
            amount = int(input("Enter amount to deposit: "))
            if amount <= 0:
                raise ValueError("❌ Invalid amount")
            balance += amount
            print("✅ Amount deposited successfully")
            print("💰 Updated Balance:", balance)

        elif choice == 4:
            print("👋 Thank you for using ATM. Bye!")
            break

        else:
            print("❌ Invalid menu choice")

    except ValueError as e:
        print("❌ Invalid input. Enter numbers only")

    except InsufficientBalanceError as e:
        print(e)

    except ZeroDivisionError:
        print("❌ Math error occurred (division by zero)")

    except KeyboardInterrupt:
        print("\n❌ Session cancelled by user")
        break

    except Exception as e:
        print("❌ Unexpected error:", e)