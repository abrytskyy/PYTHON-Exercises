max_value = 0
min_value = 1000
student_scores = input("Input a list of student scores with 'space' between each score: \n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if student_scores[n] > max_value: max_value = student_scores[n]
  if min_value > student_scores[n]:  min_value = student_scores[n]

print(student_scores)
print(f"Maximum student score is: {max_value}")
print(f"Minimum student score is: {min_value}")