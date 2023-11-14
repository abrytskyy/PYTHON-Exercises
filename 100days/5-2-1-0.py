student_scores = input("Input a list of student scores devided by 'space':").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

print(student_scores)
max_score = 0
min_score = 10000
for score in student_scores:
    if score > max_score:
        max_score = score
    if score<min_score:
        min_score = score

print(min_score)
print(max_score)



