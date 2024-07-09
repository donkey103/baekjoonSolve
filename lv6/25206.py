def gradeToScroe(grade):
  gradeList = ['F', 'None', 'D0', 'D+', 'C0', 'C+', 'B0', 'B+', 'A0', 'A+']
  return gradeList.index(grade) * 0.5

totalScore = 0
totalCredit = 0
for _ in range(20):
  subject, credit, grade = input().split()
  if grade == 'P':
    continue
  else:
    totalCredit += float(credit)
    totalScore += float (credit) * gradeToScroe(grade)

print(totalScore / totalCredit)