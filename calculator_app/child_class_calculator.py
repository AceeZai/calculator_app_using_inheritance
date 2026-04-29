from calculator_app.parent_class_calculator import Calculator

class AppCalculator(Calculator):

    def __init__(self):
        super().__init__()
        self.calculation_history = []

    def get_valid_number(self, input_message):
        while True:
            try:
                user_input = float(input(input_message))
                return user_input
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def display_menu(self):
        print("\n" + "=" * 30)
        print("      SIMPLE CALCULATOR")
        print("=" * 30)
        print("1 ➜ Addition")
        print("2 ➜ Subtraction")
        print("3 ➜ Multiplication")
        print("4 ➜ Division")
        print("5 ➜ View History")
        print("0  ➜ Exit")
        print("=" * 30)

    def save_history(self, first_number, second_number, operation_symbol, result_value):
        history_entry =  f"{first_number} {operation_symbol} {second_number} = {result_value}"
        self.calculation_history.append(history_entry)

    def show_history(self):
        print("\n===== HISTORY =====")
        if not self.calculation_history:
            print("No calculations yet.")
        else:
            for history_entry in self.calculation_history:
                print(history_entry)

    def run_calculator(self):
        while True:
            self.display_menu()
            user_input = input("Enter your menu choice from 1-5")

            if user_input == "5":
                self.show_history()
                continue

            if user_input not in ["1", "2", "3", "4", "5"]:
                print ("Invalid input. Please enter a valid number.")
                continue

            first_number = self.get_valid_number("Enter first number: ")
            second_number = self.get_valid_number("Enter second number: ")

            try:
                if user_input == "1":
                    result = self.add_numbers(first_number, second_number)
                    symbol = "+"

                elif user_input == "2":
                    result = self.subtract_numbers(first_number, second_number)
                    symbol = "-"

                elif user_input == "3":
                    result = self.multiply_numbers(first_number, second_number)
                    symbol = "*"

                elif user_input == "4":
                    result = self.divide_numbers(first_number, second_number)
                    symbol = "/"

                else:
                    print("Invalid input. Please enter a valid number.")
                    continue

                print(f"\nResult: {first_number} {symbol} {second_number} = {result}")
                self.save_history(first_number, second_number, symbol, result)

            except ZeroDivisionError as error_message:
                print("Error:", error_message)

            try_again = input("\nDo you want to try again? (yes/no): ").lower()
            if try_again != "yes":
                print("Thank you!")
                break






