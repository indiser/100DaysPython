import random
names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

scores={student:random.randint(1,100) for student in names}

passed_students={student:score for (student,score) in scores.items() if score > 50}
print(passed_students)