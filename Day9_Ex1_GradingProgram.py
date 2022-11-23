student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
grade = ""
for key in student_scores:
    if student_scores[key] > 90 and student_scores[key] <= 100:
        grade = "Outstanding"
    elif student_scores[key] > 80 and student_scores[key] <= 90:
        grade = "Exceeds Expectations"
    elif student_scores[key] > 70 and student_scores[key] <= 80:
        grade = "Acceptable"
    elif student_scores[key] <= 70:    
        grade = "Fail"
    student_grades[key] = grade
    
# 🚨 Don't change the code below 👇
print(student_grades)
