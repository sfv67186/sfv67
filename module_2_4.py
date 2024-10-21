from os import abort

print ("Вариант 1")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers :
    if i == 1 :
        continue
    elif i == 2 :
        primes.append (i)
    elif i == 3 :
        primes.append (i)
    elif i == 5 :
        primes.append (i)
    elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0 :
        not_primes.append (i)
    else :
        primes.append(i)
print (primes)
print (not_primes)

print ()

print ("Вариант 2")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers :
    if i == 1 :
        continue
    elif i == 2 :
        primes.append(i)
        continue
    else :
        for j in numbers :
            x = False
            if j == 1:
                continue
            elif i == j :
                break
            elif i % j == 0 :
                not_primes.append(i)
                x = True
                break
        if x == False :
            primes.append(i)
print (primes)
print (not_primes)