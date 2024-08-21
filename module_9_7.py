"""
module_9_7
"""
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for divider in range(2, result // 2 + 1):
            if result % divider == 0:
                print("Составное")
                return result
        print("Простое")
        return result
    return wrapper


@is_prime
def sum_three(n1, n2, n3):
    return n1 + n2 + n3


result = sum_three(2, 3, 6)
print(result)

result1 = sum_three(12, 13, 35)
print(result1)
