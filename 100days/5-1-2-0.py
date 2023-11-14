student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
print(student_heights)

number=0
summen=0
for hight in student_heights:
    number+=1
    summen=summen + hight
print(number)
print(summen)

average = summen/number
print(average)