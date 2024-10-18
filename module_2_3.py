my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
ind = 0
#print (ind)
dl = len (my_list)
cikl = int ( my_list[ind] )
#print (cikl)
while cikl >= 0 :
    if cikl != 0 :
        print(cikl)
    ind = ind + 1
    cikl = int(my_list[ind])
    if ind == dl :
        break
    else :
        continue