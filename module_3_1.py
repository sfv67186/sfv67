calls = 0

def count_calls ():
    global calls
    calls = calls + 1

def string_info (string) :
    count_calls()
    a = len (string)
    string_u = string.upper ()
    string_l = string.lower ()
    tuple_1 = (a, string_u, string_l)
    return tuple_1

def is_contains (string, list_to_search) :
    count_calls()
    string_1 = string.lower()
    for i in range (len (list_to_search)) :
        a = list_to_search [i].lower()
        if a == string_1 :
            x = True
        else :
            x = False
    return x

print (string_info ("Фуфло"))
print (string_info ("TV"))
print (is_contains ("DrWEB", ["WEBinfo", "drIVER", "drweb"]))
print (is_contains ("DrWEB", ["printer", "TV"]))
print (calls)