# problem 1 - prefix

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
stack = []

def precedence(op):
    if op in ['-', '+']:
        return 1
    elif op in ['*', '/']:
        return 2
    elif op == '**':
        return 3
    return 0

for i in range(len(l)):
    if l[i] in s:  # If the element is an operator
        while stack and precedence(l[i]) <= precedence(stack[-1]):
            o.append(stack.pop())
        stack.append(l[i])
    else:  # If the element is an operand
        o.append(l[i])

while stack:
    o.append(stack.pop())

print(' '.join(o[::-1]))
"""
import queue

def distribute_customers(num_offices, customers):
    # Create a queue for each office
    offices = [queue.Queue() for _ in range(num_offices)]

    # Distribute customers to offices
    for customer in customers:
        # Find the office with the fewest customers
        min_office = min(offices, key=lambda q: q.qsize())
        min_office.put(customer)

    # Process customers in each office
    while any(not office.empty() for office in offices):
        for office in offices:
            if not office.empty():
                customer = office.get()
                # Process the customer (e.g., serve or handle their request)
                print("Processing customer:", customer)

                # Add new customers if the office becomes empty
                if office.empty():
                    if not customers.empty():
                        new_customer = customers.get()
                        office.put(new_customer)

# Example usage
num_offices = 3
customers = queue.Queue()
customers.put("Customer 1")
customers.put("Customer 2")
customers.put("Customer 3")
customers.put("Customer 4")
customers.put("Customer 5")

distribute_customers(num_offices, customers)
"""
