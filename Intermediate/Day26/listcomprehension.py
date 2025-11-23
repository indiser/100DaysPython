# l=[1,2,3]
# new_list=[n+1 for n in l]
# print(new_list)

# name="Rana"
# letters=[letter for letter in name]
# print(letters)

# num_list=[n*2 for n in range(1,5)]
# print(num_list)


names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
caps_name=[name.upper() for name in names if len(name) > 5]
print(caps_name)