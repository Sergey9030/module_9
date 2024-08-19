def apply_all_func(int_list, *functions):
    rtn = {}
    for i in functions:
        try:
            rtn.update({i.__name__: i(int_list)})
        except TypeError:
            print(f'{i.__name__}({int_list}): Неверный тип данных')
    return rtn

print('1:')
print(apply_all_func([6, 20, 15, 9], min, max, len, sum, sorted))
print('2:')
print(apply_all_func([6, '20', 15, 9], min, max, len, sum, sorted))
print('3:')
print(apply_all_func([6, 20, 15, 9], max, min))
print('4:')
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
