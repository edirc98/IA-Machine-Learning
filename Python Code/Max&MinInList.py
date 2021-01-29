num_list =[3,5,1,7,-76,9,-5,12,76,34,21,-46]

max_num = num_list[0]
min_num = num_list[0]

for num in num_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("The greatest num is: " + str(max_num))
print("The lowest num is: " + str(min_num))