def divide_matrix(arr):
    total_sum = sum(arr)
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum == total_sum - current_sum:
            return arr[:i + 1], arr[i + 1:]

    return False

# Example
arr = [2, 6, 1, 9]
result = divide_matrix(arr)

if result:
    print(f"The array is {result[0]} and {result[1]}")
else:
    print("False")
