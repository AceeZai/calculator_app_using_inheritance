class LifeWriter:
    def __init__(self):
        self.filename = r"C:\Users\Acee Zai Mendez\PycharmProjects\PythonProject\mylife.txt"

    def write_lines(self):
        with open(self.filename, "w") as output_file:
            while true

        output_file = open(self.filename, "w")

        while True:
            line_input = input("Enter line: ")
            output_file.write(line_input + "\n")

            more_lines = input("Are there more lines y/n? ")

            if more_lines.lower() == "n":
                break

print("Writing file to:", self.filename)
