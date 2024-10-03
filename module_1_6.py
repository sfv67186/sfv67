# Словари

my_dict = {'Sergey':1967, 'Elena':1962, 'Sasha':1998}
print (my_dict)
print (my_dict['Sergey'])
print (my_dict.get('Nastya'))
my_dict.update({'Nastya':1983, 'Elena_V':1974})
print (my_dict.pop('Sergey'))
print (my_dict)

# Множества

print ()
my_set = {1, 'core', True, (1, 2, 3), 1, 2, 3}
print (my_set)
my_set.add(22)
my_set.add(33)
my_set.remove (1)
print (my_set)