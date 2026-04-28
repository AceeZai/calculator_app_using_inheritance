from calculator import Calculator

class Calculator:
    def add_numbers(self, first_number, second_number):
        return first_number + second_number

    def subtract_numbers(self, first_number, second_number):
        return first_number - second_number

    def multiply_numbers(self, first_number, second_number):
        return first_number * second_number

    def divide_numbers(self, first_number, second_number):
        if second_number == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return first_number / second_number