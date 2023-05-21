# The most frequent number
# input 
# arr[]={1,8,7,4,1,2,2,2}
# output 
# 2

from collections import Counter

def most_frequent_number(arr):
    count = Counter(arr)
    most_common = count.most_common(1)
    return most_common[0][0]

arr = [1, 8, 7, 4, 1, 2, 2, 2]
most_frequent = most_frequent_number(arr)
print(most_frequent)
