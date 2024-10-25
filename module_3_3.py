def print_params(a = 1, b = 'строка', c = True) :
    print (a, b, c)

print_params()
print_params(a = 1)
print_params(b = 'строка', c = True)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ( "Да", 1, False)
values_dict = { "a" : True, "b" : "Привет", "c" : 11}

print ()

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ("Привет", True)

print ()

print_params(*values_list_2, 42)