studentInfo={
    "Henry":99,
    "John":87,
    "Mary":77,
    "Martha":69,
    "Jenny":88
}

studentGrade={}

for key,value in studentInfo.items():

    if value>90 and value<=100:
        remarks="OutStanding"
        studentGrade[key]=remarks
    elif value > 80 and value <= 90:
        remarks="Exceeds Expectations"
        studentGrade[key]=remarks
    elif value > 70 and value <= 80:
        remarks="Acceptable"
        studentGrade[key]=remarks
    else:
        remarks="Fail"
        studentGrade[key]=remarks

print(studentGrade)