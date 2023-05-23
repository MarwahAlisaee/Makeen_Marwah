"""
class Stack:
    def __init__(self,items):
        self.items = items

    def push(self, item):
        self.items.append(item)

    def pop(self,r):
        for i in range(len(self.items)):
            r.append(self.items.pop())
        return r

    def hello(self):
        print("Hello")
        
my_stack = Stack([])
my_stack.hello()
my_stack.push('H')
my_stack.push('e')
my_stack.push('l')
my_stack.push('l')
my_stack.push('o')

reverse=''
for i in my_stack.pop([]):
    reverse +=i


print(reverse)
---------------------------------------------------------------------------------------------------
"""

str1 = input('Enter infix: ')
l = []

while str1 != '':
    l.append(str1)
    str1 = input('Enter infix: ')

print(l)

s = []
a = {'-': 1, '+': 1, '*': 2, '/': 2, '**': 3, '(': 4, ')': 4}

for i in a.keys():
    s.append(i)

print(s)

o = []

for i in range(len(l)):
    for k in range(len(s)):
        if l[i] == s[k]:
            o.append(l[i])

c = []

for i in range(len(l)):
    if l[i] not in '^*/+-':
        c.append(l[i])

print(' '.join(o[::-1] + c))

"""
class BankQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size

    def enqueue(self, customer):
        if None in self.queue:
            index = self.queue.index(None)
            self.queue[index] = customer
            print(f"Customer {customer} joined the queue at position {index+1}.")
        else:
            print("The queue is full. Customer cannot join at the moment.")

    def dequeue(self):
        if self.queue[0] is not None:
            customer = self.queue[0]
            self.queue = self.queue[1:] + [None]
            print(f"Customer {customer} has been served and left the queue.")
        else:
            print("No customer in the queue to serve.")

    def display_queue(self):
        print("Current Queue:")
        for i, customer in enumerate(self.queue):
            if customer is not None:
                print(f"Position {i+1}: {customer}")
            else:
                print(f"Position {i+1}: Empty")

# Create a bank queue with size 4
bank_queue = BankQueue(4)

# Example usage:
bank_queue.display_queue()

bank_queue.enqueue("c1")
bank_queue.enqueue("c2")
bank_queue.enqueue("c3")
bank_queue.enqueue("c4")

bank_queue.display_queue()

bank_queue.enqueue("c5")

bank_queue.dequeue()
bank_queue.dequeue()

bank_queue.display_queue()
"""

















        