"""
module_9_3
"""
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))
# Применил функцию min(), чтобы избежать возможную ошибку типа "out of range" для не равныъ по длине списков

print(list(first_result))
print(list(second_result))
