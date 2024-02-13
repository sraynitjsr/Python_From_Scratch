def loops():
    # For loop
    print("For Loop Example:")
    for i in range(5):
        print(i)

    # While loop
    print("\nWhile Loop Example:")
    count = 0
    while count < 5:
        print(count)
        count += 1

    # Nested loop
    print("\nNested Loop Example:")
    for i in range(3):
        for j in range(2):
            print(i, j)

    # Loop with break
    print("\nLoop with Break Example:")
    for i in range(5):
        print(i)
        if i == 2:
            break

    # Loop with continue
    print("\nLoop with Continue Example:")
    for i in range(5):
        if i == 2:
            continue
        print(i)
