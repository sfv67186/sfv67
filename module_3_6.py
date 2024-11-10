
def calculate_structure_sum (data_structure) :
    global result_tmp
#   Анализ первого элемента - list
    if isinstance (data_structure [0], list) :
        list_ = data_structure [0]
        for i in range(len(list_)):
            if isinstance(list_[i], int) and i == 0 :
                result_tmp = list_ [i]
            elif isinstance(list_[i], int) :
                result_tmp += list_ [i]
#   Анализ второго элемента - dict
    elif isinstance(data_structure[0], dict) :
        dict_ = data_structure [0]
        dict_k = list(dict_.keys())
        for i in range (len(dict_)):
            if isinstance(dict_k [i], str):
                result_tmp += len(dict_k[i])
            else :
                result_tmp += dict_k [i]
            if isinstance(dict_[dict_k[i]], str):
                result_tmp += len(dict_[dict_k[i]])
            else :
                result_tmp += dict_[dict_k[i]]
#   Анализ третьего элемента - tuple
    elif isinstance(data_structure[0], tuple) :
        tuple_ = data_structure [0]
        for i in range (len(tuple_)):
            if isinstance(tuple_ [i], str):
                result_tmp += len(tuple_ [i])
            elif isinstance(tuple_ [i], int):
                result_tmp += tuple_ [i]
                continue
            elif isinstance(tuple_ [i], list):
                list_ = tuple_ [i]
                for j in range ( len (list_)) :
                    if isinstance(list_ [j], str):
                        result_tmp += len(list_[j])
                    elif isinstance(list_ [j], int):
                        result_tmp += list_ [j]
#   Анализ пятого элемента - tuple
                    elif isinstance(list_ [j], set):
                        list_l = list (list_[j])
                        for k in range (len (list_l)) :
                            if isinstance (list_l [k], str) :
                                result_tmp += len(list_l [k])
                            elif isinstance (list_l [k], int) :
                                result_tmp += list_l [k]
                            elif isinstance (list_l [k], tuple) :
                                list_lt = list (list_l[k])
                                for l in range(len(list_lt)):
                                    if isinstance(list_lt [l], str):
                                        result_tmp += len(list_lt [l])
                                    elif isinstance(list_lt [l], int):
                                        result_tmp += list_lt [l]
                                    elif isinstance(list_lt [l], tuple):
                                        list_ltf = list(list_lt[l])
                                        for m in range(len(list_ltf)):
                                            if isinstance(list_ltf[m], str):
                                                result_tmp += len(list_ltf[m])
                                            elif isinstance(list_ltf[m], int):
                                                result_tmp += list_ltf[m]
                                    else:
                                        return result_tmp
            elif isinstance(tuple_ [i], dict):
                dict_ = tuple_ [i]
                dict_k = list(dict_.keys())
                for j in range (len (dict_)):
                    if isinstance(dict_k[j], str):
                        result_tmp += len(dict_k[j])
                    else:
                        result_tmp += dict_k[j]
                    if isinstance(dict_[dict_k[j]], str):
                        result_tmp += len(dict_[dict_k[j]])
                    else:
                        result_tmp += dict_[dict_k[j]]
#   Анализ четвёртого элемента - str
    elif isinstance (data_structure[0], str):
        result_tmp += len(data_structure[0])
    if len (data_structure) > 1 :
        data_structure.pop (0)
        return calculate_structure_sum (data_structure)
    else :
        return result_tmp


data_structure = [ [1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum ( data_structure)
print (result)
