def frozenset_operations():
    # Creating frozensets
    set1 = frozenset([1, 2, 3, 4, 5])
    set2 = frozenset([4, 5, 6, 7, 8])

    # Printing the frozensets
    print("set1 =", set1)
    print("set2 =", set2)

    # Union of frozensets
    union_result = set1.union(set2)
    print("Union:", union_result)

    # Intersection of frozensets
    intersection_result = set1.intersection(set2)
    print("Intersection:", intersection_result)

    # Difference of frozensets
    difference_result = set1.difference(set2)
    print("Difference (set1 - set2):", difference_result)

    # Symmetric difference of frozensets
    symmetric_difference_result = set1.symmetric_difference(set2)
    print("Symmetric Difference:", symmetric_difference_result)
