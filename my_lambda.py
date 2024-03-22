numbers = [1, 6, 3, 8, 2, 5]

sorted_numbers = sorted(numbers, key=lambda x: x)
print("Sorted numbers:", sorted_numbers)

append_element = lambda lst, element: lst + [element]
numbers = append_element(numbers, 10)
print("Numbers after appending:", numbers)
