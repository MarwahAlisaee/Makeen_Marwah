def length(arr):
    total_length = 0
    for item in arr:
        if isinstance(item, list):
            total_length += length(item)
        else:
            total_length += 1
    return total_length
# Example 1
arr1 = [1, [2, 3]]
print(length(arr1))  # Output: 3

# Example 2
arr2 = [1, 2, 3, [4, 5, [6, 7]]]
print(length(arr2))  # Output: 7
