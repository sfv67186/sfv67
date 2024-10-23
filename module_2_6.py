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
for i in range (1, 2) :
    for j in range (2, 20) :
        temp = int (i + j)
        if kl % temp == 0 :
            cod.append(i)
            cod.append(j)
for i in range (2, 3) :
    for j in range (3, 20) :
        temp = int (i + j)
        if kl % temp == 0 :
            cod.append(i)
            cod.append(j)
for i in range (3, 4) :
    for j in range (4, 20) :
        temp = int (i + j)
        if kl % temp == 0 :
            cod.append(i)
            cod.append(j)
for i in range (4, 5) :
    for j in range (5, 20) :
        temp = int (i + j)
        if kl % temp == 0 :
            cod.append(i)
            cod.append(j)
for i in range (5, 6) :
    for j in range(6, 20):
        temp = int (i + j)
        if kl % temp == 0 :
            cod.append(i)
            cod.append(j)
for i in range (6, 7) :
    for j in range (7, 20) :
        temp = int (i + j)
        if kl % temp == 0 :
            cod.append(i)
            cod.append(j)
for i in range (7, 8) :
    for j in range (8, 20) :
        temp = int (i + j)
        if kl % temp == 0 :
            cod.append(i)
            cod.append(j)
for i in range (8, 9) :
    for j in range (9, 20) :
        temp = int (i + j)
        if kl % temp == 0 :
            cod.append(i)
            cod.append(j)
for i in range (9, 10) :
    for j in range (10, 20) :
        temp = int (i + j)
        if kl % temp == 0 :
            cod.append(i)
            cod.append(j)
cod_str = list (map ( str, cod))
print("".join(cod_str))