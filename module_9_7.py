def is_prime(funct):
    def wrapper(*args):
        f = funct(*args)
        if (f == 1) or (f == 0):
            raise TypeError('Простота 1 и 0 не определена.')
        for i in range(2, int(f / 2 + 1)):
            if f % i == 0:
                return f'Составное\n{f}'
        return f'Простое\n{f}'
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

def sum_three_1(a, b, c):
    return a + b + c

sum_three_1 = is_prime(sum_three_1)
print(sum_three_1(1, 2, 3))
