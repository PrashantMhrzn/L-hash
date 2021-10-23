from key import keys

def encrypt(lst):
    new_lst = []
    for item in lst:
        if item == ' ':
            new_lst.append(' ')
        elif item == '\n':
            new_lst.append('\n')
        else:
            new_lst.append(keys.get(item))

    code = ''
    for i in new_lst:
        code += i
    return code