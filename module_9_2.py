first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

print('1:')
first_result = [len(x) for x in first_strings if len(x) >= 5]
print(first_result)

print('2:')
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(second_result)

print('3:')
third_result = {x: len(x) for x in first_strings + second_strings if not len(x) % 2}
print(third_result)
