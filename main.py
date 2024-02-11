import sys

def main():
    # Check if the correct number of command line arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <string> <integer> <float> <character>")
        sys.exit(1)

    # Reading command line arguments
    input_string = sys.argv[1]
    input_integer = int(sys.argv[2])
    input_float = float(sys.argv[3])
    input_character = sys.argv[4][0]

    # Printing the inputs
    print("String:", input_string)
    print("Integer:", input_integer)
    print("Float:", input_float)
    print("Character:", input_character)

if __name__ == "__main__":
    main()
