"""
#sum1(231) result is 2+3+1= 6
def main():
    result= input("Enter three numbers separated by a space: ")
    print (sumdigits(result))

def sumdigits(result):
    s=str(result)
    add=0
    for i in s:
        add= add+int(i)
    return add

main()

print("__________________________________________________________________________________________________________")

import math
#return area of a regular poloygon using header: area(n, side)
#Enter number of side and the side and area of poloygon
def area1 (n, side):
    area= (n*side**2)/(4*math.tan(math.pi/n))
    return area

n = int(input("Enter the number of side: "))
side = float(input("Enter side: "))

print (area1(n,side))

print("__________________________________________________________________________________________________________")


# def countVowels(string) return count vowels in the string, vowels are letter a,e,i,o and u and thir uppercase varient


string= str(input("Enter Your String: "))

def countVowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

print (countVowels(string))

print("__________________________________________________________________________________________________________")


list=[1,2,3,4,5]
print (list)
print("__________________________________________________________________________________________________________")

#Write for loops that iterate over the elements of a list without the use of the
#range function for the following tasks.
#a. Printing all elements of a list in a single row, separated by spaces.
#b. Computing the product of all elements in a list.
#c. Counting how many elements in a list are negative.

List=[22,3,-2,-1,10,1]
print ((List), end="")
print ("\n")
count=0
total = 1
for i in List:
    print ((i)," ", end="")
    total = total*i
        
    if i < 0:
       count +=1
print ("\n")
print ("Computing the product= ",count)
print("elements in a list are negative",total)

print("__________________________________________________________________________________________________________")



#v = [3,'a', 4, 'b']
#v.sort()
print("__________________________________________________________________________________________________________")


s=[22,30,-2,-1,10,1]
print (s[2:4])
print (s[-1:-3])
print (s[-3:-1])
print (s[-3: ])

print("__________________________________________________________________________________________________________")


#Execise:

Values = [0, 0, 0, 0, 0, 0, 0]
Values[0] = 10 
Values[-1] = 10

#Reverse the following list without using the reverse() function:[6, 3, 8, 1, 7]

h = [6, 3, 8, 1, 7]
reversed_list = h[::-1]

print(reversed_list)
------------------------------------------------
input_1= ['red', 'yellow', 'pink', 'black']

input_1.insert(1, 'purple')
input_1.insert(3, 'Black')
input_1.append('green')

print (input_1)
-----------------------------------------------    

input_1 = [23, 54, 76, 12, 90]
output_1 = ' | '.join(map(str, input_1))
print(output_1)

-------------------------------------------
def count_z(numbers):
    count = 0
    for num in numbers:
        if num == 0:
            count += 1
    return count


list = [1, 0, 5, 0, 0, 3, 0]
zero = count_z(list)
print("Number of zeros:", zero)


-------------------------------------------

h = [6, 3, 8, 1, 7]
reversed_list = h[::-1]

print(reversed_list)


n = int(input("Enter number: "))
words = ['Marwah', 'Sara', 'Mohammed', 'Amal', 'Abdulaziz', 'Ali', 'Ead']

def find_w(list_w, n):
    l = []
    for word in list_w:
        if len(word) > n:
            l.append(word)
    return l



result = find_w(words, n)

print("Words longer than", n, result)

"""

input_1= ['red', 'yellow', 'pink', 'black']

input_1.insert(1, 'purple')
input_1.insert(3, 'Black')
input_1.append('green')

print (input_1)
  
  