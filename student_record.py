class StudentRecord:
    def __init__(self, input_filename):
        self.input_filename = input_filename

        for student in input_file:
            parts = student.strip().split()

            gwa_value = int(parts[-1])
            student_name = " ".join(parts[:-1])

            if gwa_value > highest_gwa_value:
                highest_gwa_value = gwa_value

