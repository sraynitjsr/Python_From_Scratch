from functools import reduce

# Sorting a list of tuples by the second element
pairs = [(1, 2), (3, 1), (5, 0), (2, 4)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)

# Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Mapping a list of integers to their squares
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# Combining lists element-wise
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list(map(lambda x, y: x + y, list1, list2))
print(combined)

numbers = [3, 6, 8, 2, 10]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)
