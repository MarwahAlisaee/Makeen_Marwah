def split_string(string, n):
    if len(string) % n != 0:
        return "error"
    
    substrings = [string[i:i+n] for i in range(0, len(string), n)]
    return substrings

# Example:
result = split_string("Establish", 3)
print(result)

result = split_string("Recollective", 6)
print(result)

result = split_string("Strongest", 4)
print(result)
