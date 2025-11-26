# ATM Simulator

correct_pin = "1234"
balance = 1000.00  

attempts = 3
while attempts > 0:
    pin = input("Please enter your 4-digit PIN: ")

    if pin == correct_pin:
        print("\n✅ PIN accepted. Welcome to your account!\n")

        
        while True:
            print("===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            print("====================")

            choice = input("Please choose an option (1-4): ")

            if choice == "1":
                
                print(f"\n💰 Your current balance is: R{balance:.2f}\n")

            elif choice == "2":
                
                try:
                    deposit = float(input("Enter amount to deposit: R"))
                    if deposit > 0:
                        balance += deposit
                        print(f"✅ You deposited R{deposit:.2f}. New balance: R{balance:.2f}\n")
                    else:
                        print("⚠ Invalid amount. Please enter a positive value.\n")
                except ValueError:
                    print("❌ Invalid input. Please enter a number.\n")

            elif choice == "3":
                
                try:
                    withdraw = float(input("Enter amount to withdraw: R"))
                    if withdraw <= 0:
                        print("⚠ Invalid amount. Please enter a positive value.\n")
                    elif withdraw > balance:
                        print("❌ Insufficient funds. Try a smaller amount.\n")
                    else:
                        balance -= withdraw
                        print(f"✅ You withdrew R{withdraw:.2f}. New balance: R{balance:.2f}\n")
                except ValueError:
                    print("❌ Invalid input. Please enter a number.\n")

            elif choice == "4":
                print("\n👋 Thank you for using our ATM. Goodbye!\n")
                break

            else:
                print("⚠ Invalid selection. Please choose 1-4.\n")

        break  

    else:
        attempts -= 1
        if attempts == 0:
            print("🚫 Too many incorrect attempts. Your card has been blocked.")
        else:
            print(f"❌ Incorrect PIN. You have {attempts} attempts left.\n")