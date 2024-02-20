def maps():
    # Creating a dictionary
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    print("Original dictionary:", my_dict)

    # Accessing elements
    print("Value associated with key 'a':", my_dict['a'])

    # Modifying elements
    my_dict['b'] = 10
    print("Modified dictionary:", my_dict)

    # Adding elements
    my_dict['f'] = 6
    print("Dictionary after adding key-value pair 'f':", my_dict)

    # Removing elements
    removed_value = my_dict.pop('c')
    print("Dictionary after removing key 'c':", my_dict)
    print("Removed value:", removed_value)
