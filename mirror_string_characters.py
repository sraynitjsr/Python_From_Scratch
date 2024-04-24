def compute(string, n):
    reverse_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    l = len(string)
    answer = ""
    for i in range(n):
        answer += string[i]
    for i in range(n, l):
        answer += reverse_alphabet[ord(string[i]) - ord('a')]
    return answer

if __name__ == "__main__":
    string = "paizwlc"
    n = 3
    print(compute(string, n - 1))
