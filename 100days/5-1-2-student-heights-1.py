# 🚨 Don't change the code below 👇
#sum = 0
student_heights = input("Input a list of student heights separated by 'space' ").split()
for n in range(0, len(student_heights)):
   student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
  total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
  number_of_students += 1

average = round(total_height / number_of_students)
print(f"The average height is {average}")
