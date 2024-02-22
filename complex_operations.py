def complex_operations():
    # Creating complex numbers
    z1 = 2 + 3j
    z2 = complex(4, -5)

    # Printing the complex numbers
    print("z1 =", z1)
    print("z2 =", z2)

    # Addition of complex numbers
    sum_result = z1 + z2
    print("Sum:", sum_result)

    # Subtraction of complex numbers
    difference_result = z1 - z2
    print("Difference:", difference_result)

    # Multiplication of complex numbers
    product_result = z1 * z2
    print("Product:", product_result)

    # Division of complex numbers
    quotient_result = z1 / z2
    print("Quotient:", quotient_result)

    # Getting real and imaginary parts
    real_part = z1.real
    imaginary_part = z1.imag
    print("Real part of z1:", real_part)
    print("Imaginary part of z1:", imaginary_part)

    # Getting conjugate of a complex number
    conjugate_result = z1.conjugate()
    print("Conjugate of z1:", conjugate_result)

    # Absolute value (magnitude) of a complex number
    magnitude_result = abs(z1)
    print("Magnitude of z1:", magnitude_result)
