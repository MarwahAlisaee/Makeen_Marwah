"""
file=open("input_file.txt", "r") 
s=[]
n=[]

for x in file:
    y = x.split(" ")
    l=float(y[0])
    s.append(l)
    n.append(y[1])

avg=sum(s) / len(s)

name=''
for i in range(len(n)):
    for j in range(len(s)):
        if s[i]==max(s):
            name=n[i]
    

print("the average is : ", avg)
print("the average is : ", name) 
-----------------------------------------------------------
file=open("file_1.txt", "r")
for i in file:
    p=i.split()
    s=int(p[0])
    t=int(p[1])
    x=s*t
    print (x)
----------------------------------------------------------------
file=open("file_2.txt", "r")
for i in file:
    p=i.split()
    s=int(p[0])
    
    for j in range(1,s+1):
        if s%j==0:
            print (j, end="")
    print()


---------------------------------------------------------------

lines= open("file_3.txt", "r")

for i in lines:
    e = i.split()
    t= int(e[0])
    num = list(map(int,e[1:]))
    print (num)
    count = num.count(t)
    print(count)
    
""" 
  
  
  
  
  
  
  
    



    



