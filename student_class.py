class Student:
    def __init__(self, student_id, student_name, student_rank):
        self.student_id = student_id
        self.student_name = student_name
        self.student_rank = student_rank

    def get_student_id(self):
        return self.student_id

    def set_student_id(self, value):
        self.student_id = value

    def get_student_name(self):
        return self.student_name

    def set_student_name(self, value):
        self.student_name = value

    def get_student_rank(self):
        return self.student_rank

    def set_student_rank(self, value):
        self.student_rank = value



