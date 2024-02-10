from operator import attrgetter

from student_class import Student

# creating student objects from Student class

alice = Student(34, 'Alice', 49)

bob = Student(56, 'Bob', 78)

catherine = Student(67, 'Catherine', 56)

daniel = Student(59, 'Daniel', 45)

esther = Student(78, 'Esther', 34)

fredy = Student(34, 'Fredy', 57)

# list of students
students_list = [alice, bob, catherine, daniel, esther, fredy]

# sorting the students by rank and printing the student names
students_list_sorted_by_rank = sorted(students_list, key=attrgetter('student_rank'))

for student in students_list_sorted_by_rank:
    print(student.get_student_name())

# finding the student with the highest rank
high_rank_student = min(students_list, key=lambda x: x.student_rank)

print(f" {high_rank_student.get_student_name()} has achieved high rank of {high_rank_student.get_student_rank()}")
