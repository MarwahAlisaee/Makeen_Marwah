
#Array =[1,2,7,5,8,1,2] find First number not repeted 

Array = input("Enter Your Array: ")
for num in Array:
    if Array.count(num) == 1:
        print("First Number Not repeat: ",num)
        break
   
"""

print("__________________________________________________________________________________________________________")

# Qustion_1: Example about input 2 value from user in same time  
# Enter 2 number input from user
X, Y = input("Enter two numbers separated by a space: ").split()

# change value to integer:
X = int(X)
Y = int(Y)

# print sum of that 2 number:
print("The sum of", X, "and", Y, "is", X + Y)

print("__________________________________________________________________________________________________________")

# Qustion_2: example for defult value in python 
def greet(name, hi="Hi"):
    print(hi, name)

greet("Marwah")           # Output: Hi Alice
greet("Bob", "Hi there") # Output: Hi there Bob
"""