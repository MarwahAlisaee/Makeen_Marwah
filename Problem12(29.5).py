def multiples(num, length):
    result = []
    for i in range(1, length+1):
        result.append(num * i)
    return result

print (multiples(3,7))
print (multiples(10,4))