# a hash table applicaton 

def find_anagrams(str_list):
    str_dict = {}
    for s in str_list:
        l = sorted(list(s))
        new_s = ''.join(l)
        if new_s in str_list:
            str_dict[new_s].append(s)
        else:
            str_dict[new_s] = [s]

    ret_list = []
    for v_list in str_dict.values():
        if len(v_list) > 1:
            ret_list += v_list

    return ret_list
