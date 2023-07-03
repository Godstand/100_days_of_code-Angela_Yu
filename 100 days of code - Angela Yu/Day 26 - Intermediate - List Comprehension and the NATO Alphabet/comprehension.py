# student_score = {
#     "Aston": 67
#     "Chika": 56
# }
names = ['Aston', 'Chika', 'Ernest', 'Femi', 'Maxwell', 'Wale']
import random

student_score = {student: random.randint(1, 100) for student in names}
passed_students = {students: score for students, score in student_score.items() if score > 60}
print(student_score)
