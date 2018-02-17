def get_summ(one, two, delimeter=' '):
    lowercase_string = str(one) + str(delimeter) + str(two)
    uppercase_string = lowercase_string.upper()
    return uppercase_string

example = get_summ('hello', 'world')


print(example)