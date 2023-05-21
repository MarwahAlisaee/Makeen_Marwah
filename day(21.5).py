"""
try:
    file=open("file_1.xt", "r")
    for i in file:
        p=i.split()
        s=int(p[0])
        t=int(p[1])
        x=s*t
        print (x)
        
except IOError :
    
   print("Error: file not found.")
   
except ValueError as exception :
    
   print("Error:", str(exception))
   
---------------------------------------------------------------------------------

class Person:
    no_of_person=0
    def __init__ (self, name , age):
        self.name=name
        self.__age=age
        Person.no_of_person +=1
    def __str__(self):
        return f" this person name is {self.name} and age {self.__age}"
        return " this person name is { } and age { }".format(self.name, self.__age)

    def set_age(self, new_age):
         self.__age= new_age
         
p1 = Person("Marwah" , 22)
p2 = Person("Amal" , 20)
p2.set_age(40)
#print (p2.set_age( ))
p2.age=30
print (p1.__str__())
print (p1.no_of_person)
print (dir(Person))

p1.age=25
print(p1.__str__())

___________________________________________________________________________________________

# in python class Employee wiht attribute like emp_id, emp_name, emp_selery and depatement and print employee detailes semple data
#"ADAMS", "E344", "45666", "Accounting"
#"MARTHN", "E3556", "50439", "Sales"
# assign departmint
#print employee deleats
# calculate emp_salary
#overtime =hours_worked-50
#overtime amount =(overtime*(salary/50))

class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.department = department
    
    def print_d(self):
        print("Employee Name:", self.emp_name)
        print("Employee ID:", self.emp_id)
        print("Employee Salary:", self.emp_salary)
        print("Department:", self.department)
        
        
    def assign_department(self, department):
        self.department = department
    
    def salary_c(self, hour_w):
        if hour_w <= 50:
            return self.emp_salary
        else:
            overtime = hour_w - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            return self.emp_salary + overtime_amount


employee1 = Employee("ADAMS", "E344", 45666, "Accounting")
employee2 = Employee("MARTHN", "E3556", 50439, "Reserching")
employee3 = Employee("JONES", "E344", 45666, "operation")
employee4 = Employee("SMITH", "E3556", 50439, "Sales")


employee1.print_d()
employee2.print_d()
employee3.print_d()
employee4.print_d()



employee1.assign_department("Accounting")
employee2.assign_department("Reserching")
employee2.assign_department("operation")
employee2.assign_department("Sales")


employee1_salary = employee1.salary_c(80)
employee2_salary = employee2.salary_c(90)
employee1_salary = employee1.salary_c(30)
employee2_salary = employee2.salary_c(20)

print("Employee 1 Salary:", employee1_salary)
print("Employee 2 Salary:", employee2_salary)
print("Employee 3 Salary:", employee1_salary)
print("Employee 4 Salary:", employee2_salary)

------------------------------------------------------------------------------------
from datetime import date

class Person:
    def __init__(self, name, age, address, height):
        self.name = name
        self.age = age
        self.address = address
        self.height = height

    def class_type(self):
        return "This is parent class"

class Student(Person):
    def __init__(self, name, age, address, height, grade):
        super().__init__(name, age, address, height)
        self.grade = grade

    def class_type(self):
        return "This is Student class"

    @classmethod
    def new_student(cls, name, birth_year, address, height, grade):
        age = date.today().year - birth_year
        return cls(name, age, address, height, grade)

s1 = Student("Mem", 23, "msucat", 180, [3.1, 2.5, 2])
p1 = Person("Hind", 33, "Sohar", 223)

s2 = Student.new_student("Mem", 1993, "msucat", 180, [3.1, 2.5, 2])
print(s2.age)

print(s1.class_type())
print(p1.class_type())

-----------------------------------------------------------------------------------------
"""
# in python the class is Restaurent with attribute like menu_items, book_table, customer_order
# and method is add_item_to_menu, book_table, and customer_order.
# now add items to menu
# make table revestion
# take customer order
# print the menu
# print table revestion
# Print customer order

class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []
    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price
    def book_tables(self, table_number):
        self.book_table.append(table_number)
    def customer_order(self, table_number, order):
        order_details = {'table_number': table_number, 'order': order}
        self.customer_orders.append(order_details)
    def print_menu_items(self):
        for item, price in self.menu_items.items():
            print("{}: {}".format(item, price))
    def print_table_reservations(self):
        for table in self.book_table:
            print("Table {}".format(table))
    def print_customer_orders(self):
        for order in self.customer_orders:
            print("Table {}: {}".format(order['table_number'], order['order']))
            

restaurant = Restaurant()

# Add items
restaurant.add_item_to_menu("Cheeseburger", 9.99)
restaurant.add_item_to_menu("Caesar Salad", 8)
restaurant.add_item_to_menu("Grilled Salmon", 19.99)
restaurant.add_item_to_menu("French Fries", 3.99)
restaurant.add_item_to_menu("Fish & Chips:", 15)
# Book table
restaurant.book_tables(1)
restaurant.book_tables(2)
restaurant.book_tables(3)
# Order items
restaurant.customer_order(1, "Cheeseburger")
restaurant.customer_order(1, "Grilled Salmon")
restaurant.customer_order(2, "Fish & Chips")
restaurant.customer_order(2, "Grilled Salmon")

print("\nPopular dishes in the restaurant along with their prices:")
restaurant.print_menu_items()
print("\nTable reserved in the Restaurant:")
restaurant.print_table_reservations()
print("\nPrint customer orders:")
restaurant.print_customer_orders()
"""
--------------------------------------------------------------------------------------


#write python Class BankAccount with attrubuta Account_number, balence, date_of_opining, and customer_name. and the method like depsit, wirthdrow, and check_balence
class Bank_Account:
    def __init__(self, Account_number, balance, date_of_opining, customer_name):
        self.Account_number = Account_number
        self.balance = balance
        self.date_of_opining = date_of_opining
        self.customer_name = customer_name
        
    def print_d(self):
        print("Account_number: ", self.Account_number)
        print("balence: ", self.balance)
        print("date_of_opining:", self.date_of_opining)
        print("customer_name:", self.customer_name)
        

    def deposit(self, amount):
        self.balance += amount
        return ("Deposited {}".format(self.balance))
        
    def wirthdrow(self,amount):
        self.balance -=amount
        return ("wirthdrow {}".format( self.balance))
        
    def check_balance(self):
        return self.balance
account1 = Bank_Account("123456789", 1000, "2023-01-01", "Sam")
account1.print_d()
print(account1.deposit(500))
print(account1.wirthdrow(200))
print("Check Balence: ",account1.check_balance())

"""

    