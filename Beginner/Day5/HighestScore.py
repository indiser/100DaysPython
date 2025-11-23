student_score=[98,90,87,99,79,69,80]
num=student_score[0]

for score in student_score:
    if score > num:
        num=score

print(f"The Highest number is:{num}")