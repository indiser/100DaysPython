with open("file1.txt") as filp:
    contents1=filp.readlines()
    list1=[line.strip() for line in contents1]

with open("file2.txt") as filp:
    contents2=filp.readlines()
    list2=[line.strip() for line in contents2]



result=[int(num) for num in list1 if num in list2]
print(result)