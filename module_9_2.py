"""
module_9_2
"""
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]
print(first_result)
second_result = [(x, y) for y in second_strings for x in first_strings if len(x) == len(y)]
print(second_result)
first_strings.extend(second_strings)
third_result = {x: len(x) for x in list(first_strings)}
print(third_result)
