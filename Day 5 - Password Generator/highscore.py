# Input a list of student scores
student_scores = ["78", "65", "89", "86", "55", "91", "64", "89"]
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# Write your code below this row 👇
highscore = 0
for score in student_scores:
  if score > highscore:
    highscore = score  
print(f"The highest score in the class is: {highscore}")