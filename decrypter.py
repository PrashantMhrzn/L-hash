from key import keys

def get_key(val):
    for key, value in keys.items():
        if val == value:
            return key
    return "key doesn't exist"


def decrypt(lst):
    new_lst = []
    for item in lst:
        if item == ' ':
            new_lst.append(' ')
        elif item == '\n':
            new_lst.append('\n')
        else:
            new_lst.append(get_key(item))

    code = ''
    for i in new_lst:
        code += i
    return code