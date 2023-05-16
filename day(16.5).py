"""
s=[1,2,3]
s.extend([4,6])

print (s)
--------------------------------------------

s=[1,2,3]
#s= "|".join((str(s)))
s="|".join(map(str, s))
print(s)


--------------------------------------------

result=[]
for i in range (5):
    result.append(i**2)
print (result)

# other solution
result=[i**2 for i in range (5)]
print (result)
-------------------------------------------------------

result=[]
for i in range (5):
    if(i%2==0):
        result.append(i)
print (result)

# other solution

result=[i for i in range (5) if i%2==0]
print (result)
-------------------------------------------------------------------------------------------------------


sides =int(input("Enter the number of side: "))
def freq(sides):
    freq_1 = []
    for s in range(sides):
        s= int(input(" Enter your counters: "))
        if s>=0:
            freq_1.append(s)
        else:
            break
        
    return freq_1


def counter_inp(frequ_1):
    for i in frequ_1:
        if frequ_1.count(i)>1:
            
            print(i,":",frequ_1.count(i)," ",end='')
        
        else:
            print(i+1,":",frequ_1.count(i)," ",end='')
freq_1 = freq(sides)
print (counter_inp(freq_1))
-------------------------------------------------------------------------------------------------------
COUNTRIES=7
MEDALS=3
counts=[
    [0,3,0],
    [0,0,1],
    [0,0,1],
    [1,0,0],
    [3,1,1],
    [0,1,0],
    [1,0,1]
    ]

for i in range(COUNTRIES):
    for j in range(MEDALS) :
        print("%8d" % counts[i][j], end="")
    print()
print('counts of [i][j] is : ',counts[0][1])
-------------------------------------------------------------------

"""
#Tupes
   
contact = {"k1": {"name": "p1", "Age": 22},
            "k2": {"name": "p2", "Age": 27}}

for key, value in contact.items():
    age = int(value["Age"])
    if age > 22:
        print(contact[key]["name"])
        
#other solurion

for key in contact:
    x=contact[key]["Age"]
    if(x>22):
        print(contact[key]["name"])
   





