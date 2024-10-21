kl = int ( input ( "Введите число от 3 до 20: "))
while kl > 20 or kl < 3 :
    if kl < 3 or kl > 20 :
        print ()
        print ("Вы ввели неверное число.")
        print ()
        kl = int(input("Введите число от 3 до 20: "))
    else :
        break
cod = []
for i in range (1, 10) :
    for j in range (2, 20) :
        temp = int (i + j)
        if kl % temp == 0 :
            cod.append([i, j])




print (cod)