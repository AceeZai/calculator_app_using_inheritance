class IntegerProcessor:
    def __init__(self, input_filename):
        self.input_filename = input_filename

    def process_integers(self):
        try:
            input_file = open(self.input_filename, "r")
        except FileNotFoundError:
            print("Error: integers.txt file not found in project folder.")
            return

        double_file = open("double.txt", "w")
        triple_file = open("triple.txt", "w")

        for number_line in input_file:
            number_line = number_line.strip()

            if number_line == "":
                continue

            number = int(number_line)

            if number % 2 == 0:
                double_file.write(str(number ** 2) + "\n")
            else:
                triple_file.write(str(number ** 3) + "\n")

        input_file.close()
        double_file.close()
        triple_file.close()

        print("Done: files created successfully.")


# RUN (OUTSIDE CLASS)
processor = IntegerProcessor("integers.txt")
processor.process_integers()