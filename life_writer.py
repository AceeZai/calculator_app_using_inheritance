class LifeWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_lines(self):
        output_file = open(self.filename, "r")

        while True:
            line_input = input("Enter line: ")
            output_file.write(line_input + "\n")

            more_lines = input("Are there more lines y/n? ")

            if more_lines.lower() == "n":
                break

        output_file.close()
        print("File writing complete.")
l