class NumberSeparator:
    def __init__(self, filename):
        self.filename = filename

    def separate_even_odd(self):
        even_file = open("p1_even-odd/even.txt", "w")
        odd_file = open("p1_even-odd/odd.txt", "w")
        file = open(self.filename, "r")

        for line in file:
            line = line.strip()

            if line == "":
                continue  # skip empty lines

            num = int(line)

            if num % 2 == 0:
                even_file.write(str(num) + "\n")
            else:
                odd_file.write(str(num) + "\n")

        file.close()
        even_file.close()
        odd_file.close()

        print("Even and Odd files created successfully.")


# RUN
obj = NumberSeparator("p1_even-odd/numbers.txt")
obj.separate_even_odd()
