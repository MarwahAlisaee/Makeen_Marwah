numbers = [1, 4, 5, 7, 3, 0]
s = len(numbers)
result = []
max_value = max(numbers)

for i in range(s):
    if numbers[i] == max_value:
        result = numbers[i:]
        break

print(result)
