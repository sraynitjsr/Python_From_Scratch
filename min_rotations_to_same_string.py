def min_rotations_to_same_string(string):
    n = len(string)
    # Concatenate the string with itself to handle rotations
    concat_string = string + string
    for i in range(1, n + 1):
        substring = concat_string[i:i+n]
        if substring == string:
            return i
    # If no rotation produces the same string, return -1
    return -1

# Test the function
if __name__ == "__main__":
    string = "abracadabra"
    print("Minimum number of rotations to get the same string:", min_rotations_to_same_string(string))
