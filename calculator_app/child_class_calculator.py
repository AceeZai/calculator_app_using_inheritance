

class Calculator:

    def _init_(self):
        self.calculation_history = []

    def display_menu(self):
        print("\n===== SIMPLE CALCULATOR =====")
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")
        print("5 - View History")
        print("=============================")

    def get_valid_number(self, input_message):
        while True:
            try:
                user_input = float(input(input_message))
                return user_input
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def save_history(self, first_number, second_number, operation_symbol, result_value):
        history_entry =  {first_number} {operation_symbol} {second_number} {secpnd_number} = {result_value}""
    def multiply_numbers(self, first_number, second_number):
        return first_number * second_number

    def divide_numbers(self, first_number, second_number):
        if second_number == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return first_number / second_number