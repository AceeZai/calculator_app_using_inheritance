class LifeWriter:
    def __init__(self):
        self.filename = r"C:\Users\Acee Zai Mendez\PycharmProjects\PythonProject\mylife.txt"

    def write_lines(self):
        with open(self.filename, "w") as output_file:
            while True:
                line_input = input("Enter line: ")
                output_file.write(line_input + "\n")

                more_lines = input("Are there more lines y/n? ")
                if more_lines.lower() == "n":
                    break
        print("File writing complete at:", self.filename)

life_writer = LifeWriter()
life_writer.write_lines()