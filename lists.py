def lists():
    # Creating a list
    my_list = [1, 2, 3, 4, 5]
    print("Original List:", my_list)

    # Accessing elements
    print("\nAccessing Elements:")
    print("First Element:", my_list[0])
    print("Last Element:", my_list[-1])

    # Slicing
    print("\nSlicing:")
    print("Sliced List:", my_list[1:4])

    # Modifying elements
    print("\nModifying Elements:")
    my_list[2] = 6
    print("Modified List:", my_list)

    # Appending elements
    print("\nAppending Elements:")
    my_list.append(7)
    print("Appended List:", my_list)

    # Removing elements
    print("\nRemoving Elements:")
    removed_element = my_list.pop()
    print("Removed Element:", removed_element)
    print("List after removing last element:", my_list)

    # Concatenating lists
    second_list = [8, 9, 10]
    print("\nConcatenating Lists:")
    concatenated_list = my_list + second_list
    print("Concatenated List:", concatenated_list)

    # List length
    print("\nLength of List:", len(concatenated_list))
