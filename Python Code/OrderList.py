def mysort(l):
    list_l = len(l)

    for i in range(list_l):
        for j in range(0,list_l-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
                #aux = l[j]
                #l[j] = l[j+1]
                #l[j+1] = aux


num_list =[3,5,1,7,4,9,-5,12,76,34,21,-46]

mysort(num_list)

print(num_list)