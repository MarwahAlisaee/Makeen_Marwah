
"""
# How to use Generator

def f_num(nums):
    x,y =0, 1
    for i in range(nums):
        x,y= y,x+y
        yield x
        
def squer(nums):
    for num in nums:
        yield num **2
        
def squer_2(squer):
    for num in squer:
        yield num **3

print(sum(squer(f_num(10))))
print(sum(squer_2(squer(f_num(10)))))
"""
"""
# you are given alist from 1 to 15, write generator function that generates a sequence of even number from the list 
     
lst=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]       
def even_num(lst):
    for num in lst:
        if num % 2 == 0:
            yield num

#print (next(even_num(lst)))

a = list(range(1, 16))
even_gen = even_num(a)

for n in even_gen:
    print(n)

"""
"""
def f1(fun):
    def w():
        print("hello")
        fun()
        print("welcome to python")
    return w
    
def f2():
    print("code academe")


f= f1(f2)    
f()
"""

import time
import math

def cal_tim(fun):
    def w(n):
        b=time.time()
        fun(n)
        e=time.time()
        print("time take in: ", fun.__name__, e - b)
    return w

@cal_tim

def factorial(num):
    time.sleep(2)
    print(math.factorial(num))
      
factorial(10)



