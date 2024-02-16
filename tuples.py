def tuples():
    # Creating a tuple
    my_tuple = (1, 2, 3, 4, 5)
    
    # Accessing elements
    print(my_tuple[0])  # Output: 1
    print(my_tuple[2])  # Output: 3
    
    # Slicing
    print(my_tuple[1:4])  # Output: (2, 3, 4)
    
    # Length
    print(len(my_tuple))  # Output: 5
    
    # Concatenation
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    concatenated_tuple = tuple1 + tuple2
    print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)
    
    # Repetition
    repeated_tuple = (1, 2) * 3
    print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)
    
    # Membership
    print(3 in my_tuple)  # Output: True
    print(6 in my_tuple)  # Output: False
    
    # Iteration
    for item in my_tuple:
        print(item)
    
    # Unpacking
    a, b, c, d, e = my_tuple
    print(a, b, c, d, e)  # Output: 1 2 3 4 5
