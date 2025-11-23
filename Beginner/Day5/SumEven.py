target=int(input("Enter The target number: \n"))
sum=0
for i in range(2,target+1,2):
    sum+=i

print(f"The sum of all even numbers upto {target} is:{sum}")