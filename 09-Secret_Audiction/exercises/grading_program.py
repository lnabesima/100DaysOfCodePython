import pprint

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

student_grades = {}

for student in student_scores:
    student_grade = ""
    student_score = student_scores[student]
    if 91 <= student_score <= 100:
        student_grade = "Outstanding"
    elif 81 <= student_score <= 90:
        student_grade = "Exceeds Expectations"
    elif 71 <= student_score <= 80:
        student_grade = "Acceptable"
    else:
        student_grade = "Fail"
    student_grades[student] = student_grade

# 🚨 Don't change the code below 👇
pprint.pprint(student_grades)
