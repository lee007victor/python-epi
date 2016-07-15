# Is an anonymous letter constructible?

def is_letter_constructable(str_m, str_l):
    dict_m = {}

    for c in str_m:
        if c not in dict_m:
            dict_m[c] = 1
        else:
            dict_m[c} += 1

    for c in str_l:
        if c not in dict_m:
            return False
        else:
            dict_m[c] -= 1
            if dict_m == 0:
                dict_m.pop(c)

    return True
