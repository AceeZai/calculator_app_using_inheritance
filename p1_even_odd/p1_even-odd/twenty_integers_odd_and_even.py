#Separate even and odd numbers from numbers.txt

class NumberSeparator:
    def __init__(self, filename):
        self.input_filename = filename

    def separate_even_and_odd(self):
        even_file = open("even.txt", "w")
        odd_file = open("odd.txt", "w")
        input_file = open(self.input_filename, "r")

        for number_line in input_file:
            number_value = int(number_line.strip())

            if number_value % 2 == 0:
                even_file.write(str(number_value) + "\n")
            else:
                odd_file.write(str(number_value) + "\n")

        input_file.close()
        even_file.close()
        odd_file.close()

        print("Done creating even.txt and odd.txt")

# RUN
<<<<<<< HEAD:p1_even-odd/twenty_integers_odd_and_even.py
number_separator = NumberSeparator("p1_even_odd/numbers.txt")
number_separator.separate_even_and_odd()
=======
number_separator = NumberSeparator("numbers.txt")
number_separator.separate_even_and_odd()
>>>>>>> 66e5263200f6c133c09607cae7104754049da260:twenty_integers_odd_and_even.py
