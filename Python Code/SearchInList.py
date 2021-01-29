num_list =[3,5,1,7,4,9]

in_num = int(input("Put a number to check if it is in the list: "))
founded = False
for num in num_list:
    if num == in_num:
        print("The number exists in index " + str(num_list.index(in_num)))
        founded = True
        break
if(founded == False): 
    print("The number is not in the list")