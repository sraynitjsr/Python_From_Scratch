class CustomDivisionError(Exception):
    def __init__(self, message):
        super().__init__(message)

def divide_numbers(x, y):
    try:
        if y == 0:
            raise CustomDivisionError("Error: Division by zero!")
        result = x / y
    except CustomDivisionError as e:
        print(e)
    except TypeError:
        print("Error: Invalid operand types!")
    else:
        print("Result:", result)
    finally:
        print("Execution completed.")

divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, 'a')
