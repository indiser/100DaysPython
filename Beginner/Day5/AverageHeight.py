heights=[180,167,193,157,200]
sum=0
number_of_students=0
for height in heights:
    sum+=height

for num in heights:
    number_of_students+=1


average=float(sum/number_of_students)
print(f"Average Heights Of all students is:{average}")