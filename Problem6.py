def left_rotate_array(array, rotations):
    rotations %= len(array)
    reversed_arr = list(reversed(array))
    r_array = list(reversed_arr[rotations:] + reversed_arr[:rotations])
    return r_array

# Example
array = [1, 2, 3, 4, 5]
rotation_t = 2
result = left_rotate_array(array, rotation_t)
print(result)
