first = int (input ("Введите чисоло: "))
second = int (input ("Введите второе чисоло: "))
third = int (input ("Введите третье чисоло: "))
if first == second and third == second :
    print ("3")
elif first != second and first != third and second != third :
    print ('0')
else:
    print ("2")