print("Zismail-Dev")
print("Savings calculation program")

while True:
    savings = float(input("Enter the starting amount. : "))

    while savings > 0.10: 
        print(f"Balance: {savings:.2f}")

        percent = int(input("Choose the percentage you want to save. (50, 30, 20, 10): "))
        if percent not in [50, 30, 20, 10]:
            print("Incorrect percentage. Please select. 50, 30, 20, or 10")
            continue

        amount_to_save = (savings * percent) / 100
        savings -= amount_to_save

        print(f"Saving amount: {amount_to_save:.2f}")
        print(f"Balance: {savings:.2f}")

        another_round = input("Want to find more? (y/n): ")
        if another_round.lower() != 'y':
            print("Thank you for using the service. Goodbye program")
            break
