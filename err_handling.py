def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError:
        print("Error: Invalid operand types!")
    else:
        print("Result:", result)
    finally:
        print("Execution completed.")

divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, 'a')
