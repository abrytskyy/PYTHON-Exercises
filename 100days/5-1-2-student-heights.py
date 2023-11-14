student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
print(student_heights)

print(len(student_heights))
print(sum(student_heights))

average = sum(student_heights)/len(student_heights)
print(average)