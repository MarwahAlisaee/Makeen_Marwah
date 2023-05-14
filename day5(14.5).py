"""
string=input("Enter phone in the format (XXX)XXX-XXXX:")
valid = len(string) == 13
position = 0
while valid and position < len(string) :
   if position == 0:
     valid = string[position] == "("
   elif position == 4 :
     valid = string[position] == ")"
   elif position == 8 :
     valid = string[position] == "-"
   else:
     valid = string[position].isdigit()
position = position + 1
if valid :
  print("The string contains a valid phone number.")
else:
  print("The string does not contain a valid phone number.")
  
print("__________________________________________________________________________________________________________")

#enter the password and check the valiv or not. should stisfy the following: 8 characters, contain a lower case ,  contain a lower case , contain a mumber, aontains at lest one specal symbol (@, $, #, _)
password = input("Enter correct password: ")
valid = len(password) == 8
position = 0

while valid and position < len(password):
    valid = (password[position] >= "a" and password[position] <= "z") or \
            (password[position] >= "A" and password[position] <= "Z") or \
            (password[position].isdigit()) or \
            (password[position] >= ("[@, $, #,_]"))

    position = position+ 1

if valid:
    print("The password is valid.")
else:
    print("The password is not valid.")
    
print("__________________________________________________________________________________________________________")

text="**435-759,"
text= text.strip("-")
text= text.strip("*")
text= text.strip(",")
text= text.replac("-", " ")
print (text)

print("__________________________________________________________________________________________________________")


import random

print(round(random.random()*100,4))


print("__________________________________________________________________________________________________________")

# random function :

from random import randint
d1 = randint (1,100)
print (d1)
for i in range(100):
   
   d2 = int(input ( "Enter Your Random number " ))
   
   if d1>d2:
       print ( " Go more")
   elif d2>d1:
       print ( " Go lower")
   else:
       print (" Congrudation You Win ")
       break 
print("__________________________________________________________________________________________________________")

# continue function :

for i in range(10):
    if i == 5:
        continue
    print (i)
    
print("__________________________________________________________________________________________________________")

"""
# break function :
for i in range(10):
    if i == 5:
        break
    print (i)
    
print("__________________________________________________________________________________________________________")


    

    


       
 
   