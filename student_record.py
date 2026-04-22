class StudentRecord:
    def __init__(self, input_filename):
        self.input_filename = input_filename

    def find_highest_gwa(self):
        input_file = open(self.input_filename, "r")

        highest_student_name = ""
        highest_gwa_value = -1

        for student_line in input_file:
            parts = student_line.strip().split()

            gwa_value = float(parts[-1])
            student_name = " ".join(parts[:-1])

            if gwa_value > highest_gwa_value:
                highest_gwa_value = gwa_value
                highest_student_name = student_name

        input_file.close()

        print("Top Student:", highest_student_name)
        print("GWA:", highest_gwa_value)

# RUN
student_record = StudentRecord("students.txt")
student_record.find_highest_gwa()