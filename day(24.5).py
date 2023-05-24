"""
# lambda function:

a= lambda x, y: x+y

print(a(1,2))

# working with defult value

a= lambda x=3,y=1 : x+y

print(a( ))
----------------------------------------------------------------------------------------------------
"""
"""
# how to use lambda to sorted dictinery list with age:
 
p=[{'name':'Ahmed', 'age':23},
   {'name':'said', 'age' :20},
   {'name':'salim', 'age' :29},
   {'name':'mohammed', 'age' :18}]

#p.sort (age= lambda x:x['age'])
a= sorted(p, key=lambda x:x['age'])
print(a)

"""
"""
# filter lowercase and uppercase in that list using filter()check

list_1=['MARWAH', 'sara', 'muna', 'Hana']
a= list(filter(lambda x: x[0].islower() , list_1))
b= list(filter(lambda x:x[0].isupper(), list_1))
print(a)
print(b)
"""
"""
# enter the string list and change to uppercase :

list_1 = ['marwah', 'sara', 'muna', 'hana']
l = list(map(str.upper, list_1))
print(l)

"""
#sum of squares reduce of list number using reduce() 
from functools import reduce

def square(x):
    return x ** 2

def sum_s(num):
    return reduce(lambda x, y: x + y,map(square,num))

num = [1, 2, 3, 4, 5]
result = sum_s(num)
print(result) 

