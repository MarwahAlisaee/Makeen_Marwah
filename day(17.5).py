"""
x=[[1,2,3],
   [4,5,6]]

for i in range(2):
    for j in range(3):
        print ( x[i][j], end="")
    print ()

________________________________________________________________________

#Tables:
#  white code [1,1,1
#              2,2,2
#              3,3,3]
#  in python nested loop


x= []
for i in range(1,4):
    s = []
    for j in range(1,4):
        s.append(i)
    x.append(s)
    
for i in range(3):
    for j in range(3):
        print (x[i][j], end="   ")

    print()
    
___________________________________________________  
#write program where user detrmines row and columns, then take input from user for each row and columns as 2d list. finally print the table of 2d list 

r= int(input("Enter number of row: "))
c= int (input("Enter number of columns: "))

x= []
for i in range(r):
    s = []
    for j in range(c):
        num = int(input("enter num: "))
        s.append(num)
    x.append(s)
    
for i in range(r):
    for j in range(c):
        print (x[i][j], end="")

    print()
"""
 
# write a 2d list that print follwing
#    1000
#    2100
#    2210
#    2221
"""
n = 4  
x = [[0] * n for y in range(n)] 


for i in range(n):
    for j in range(n):
        if j < i:
            x[i][j] = 2
        elif j > i :
            x[i][j] = 0
        else:
            x[i][j] = 1  

for r in x:
    for v in r:
        print(v, end='')
    print()
__________________________________________________________
"""

n = 4  
x = [[0] * n for y in range(n)] 


for i in range(n):
    for j in range(n):
        #if (((i-j==2) or (j-i==2))and (i != 0)):
        if ((i-j==2) or (j-i==2)):
            x[i][j] = 1
        elif (j == i) :
            x[i][j] = 1
        else:
            x[i][j] = 0  

for r in x:
    for v in r:
        print(v, end='')
    print()


























