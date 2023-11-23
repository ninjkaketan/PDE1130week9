# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))#type of input data

exam_three = int(input("Input exam grade three: "))#type of input data and "3" changed to "three; str changed to int"

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:#grade changed to grades
  sum = sum + grade

avg = sum / len(grades)#grdes changed to grades

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:#colon added
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C" #double quotes added
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:#elif changed to else
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grades))#changed grade to grades

    print("Average: " + str(avg))

    print("Grade: " + str(letter_grade))#added str
    break #break is added to exit loop
if letter_grade is "F":
    print ("Student is failing.")#brackets added
else:
    print ("Student is passing.")#brackets added
