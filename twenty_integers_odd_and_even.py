#Separate even and odd numbers from numbers.txt

class NumberSeparator:
    def __init__(self, filename):
        self.filename = filename

    def separate_even_odd(self):
        even_file = open("even.txt", "w")
        odd_file = open("odd.txt", "w")
        file = open(self.filename, "r")

        for line in file:
            num = int(num.strip())
            if num % 2 == 0:
                even_file.write(str(num) + "\n")
            else:
                odd_file.write(str(num) + "\n")
