def dictionary():
    # Creating a dictionary
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    
    # Accessing elements
    print(my_dict['a'])  # Output: 1
    print(my_dict['c'])  # Output: 3
    
    # Adding a new key-value pair
    my_dict['f'] = 6
    print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    
    # Length
    print(len(my_dict))  # Output: 6
    
    # Removing a key-value pair
    del my_dict['b']
    print(my_dict)  # Output: {'a': 1, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    
    # Checking for key existence
    print('c' in my_dict)  # Output: True
    print('z' in my_dict)  # Output: False
    
    # Iterating over keys
    for key in my_dict:
        print(key, my_dict[key])
    
    # Iterating over key-value pairs
    for key, value in my_dict.items():
        print(key, value)
