def calculate_simple_interest(principal, rate_of_interest, time_period):
    return (principal * rate_of_interest * time_period) / 100

def calculate_compound_interest(principal, rate_of_interest, time_period):
    amount = principal * (1 + rate_of_interest / 100) ** time_period
    compound_interest = amount - principal
    return compound_interest, amount

def get_positive_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Main function to run the program
def main():
    print("Welcome to the Interest Calculator!")

    while True:
        # Get user choice for interest calculation type
        print("\nChoose the type of interest calculation:")
        print("1. Simple Interest")
        print("2. Compound Interest")
        choice = input("Enter 1 or 2: ")

        # Get principal, rate of interest, and time period
        principal = get_positive_input("Enter the principal amount: ")
        rate_of_interest = get_positive_input("Enter the rate of interest (in %): ")
        time_period = get_positive_input("Enter the time period (in years): ")

        # Calculate and display the result
        if choice == '1':
            simple_interest = calculate_simple_interest(principal, rate_of_interest, time_period)
            total_amount = principal + simple_interest
            print(f"\nThe Simple Interest is: {simple_interest}")
            print(f"The Total Amount (Principal + Interest) is: {total_amount}")
        elif choice == '2':
            compound_interest, amount = calculate_compound_interest(principal, rate_of_interest, time_period)
            print(f"\nThe Compound Interest is: {compound_interest}")
            print(f"The Total Amount (Principal + Compound Interest) is: {amount}")
        else:
            print("Invalid choice! Please choose 1 or 2.")

        # Ask if the user wants to perform another calculation
        another_calculation = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            print("Thank you for using the Interest Calculator!")
            break

# Run the program
if __name__ == "__main__":
    main()
