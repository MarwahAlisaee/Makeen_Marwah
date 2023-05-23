"""
key = 2
arr = [1,5,7,8,2,3,9]
arr.sort() 
def Binary(arr, key):
    l = 0
    h = len(arr) - 1

    while l <= h:
        mid = (l + h) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            l = mid + 1
        else:
            h = mid - 1

    return -1

p= Binary(arr, key)

if p!= -1:
    print("Key in index:", p)
else:
    print("Key not in the list.")
-----------------------------------------------------------------------------------
"""
"""
# give non-nagitive integer x compute and return the squr root



def sq(key):
    l = 0
    h = key
    while 1 <= h:
        mid =(l + h)//2
        #return mid
        
        if (mid==float(key**(0.5))):
             return mid
             break 
        elif mid> float(key**(0.5)):
             h = mid -1
        else:
            l = mid +1


key = int(input("Enter Your Key: ")) 
print(sq(key))
"""
"""
def insertionSort(array):
    for step in range (1, len(array)):
        key =array[step]
        j= step -1
        
        while j >= 0 and key < array[j]:
            array[j+1] =array[j]
            j= j-1
            
            
        array[j+1]=key
    return array
         
array= [ 2, 1, 7, 5, 9]

print (insertionSort(array))

-----------------------------------------------------------------------------------------
"""


def insertionSort(array):
    for step in range (1, len(array)):
        key =array[step]
        j= step -1
        
        while j >= 0 and int(key.split(',')[1]) < int(array[j].split(',')[1]):
            array[j+1] =array[j]
            j= j-1
            
            
        array[j+1]=key
    return array
         
array=["Said,25", "Majid,19", "Salim,23", "Ali,21", "sultan,28"]

print (insertionSort(array))


 

