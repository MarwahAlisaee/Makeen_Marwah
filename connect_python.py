"""
#QUSTION_1
import pyodbc

connection = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-FK6DE25V\MSSQLS;'
    'Database=Connect_python;'
    'Trusted_Connection=yes;'

)

cursor = connection.cursor()
cursor.execute("SELECT * FROM COLLEGE")

rows = cursor.fetchall()

for row in rows:
    print(row)


cursor.close()
connection.close()


"""
#QUSTION_2
import pyodbc
conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-FK6DE25V\MSSQLS;'
    'Database=TMS;'
    'Trusted_Connection=yes;'
)
conn.autocommit=True
cursor = conn.cursor()
#conn.close()

cursor.execute("create database MARWAH")

cursor.close()
conn.close()


"""
#QUSTION_3
import pyodbc
conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-FK6DE25V\MSSQLS;'
    'Database=Connect_python;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

cursor.execute('''
		CREATE TABLE product (
			product_id int primary key,
			product_name nvarchar(50),
			price int
			)
               ''')
cursor.execute('''
		INSERT INTO product (product_id, product_name, price)
		VALUES
			(1,'Desktop Computer',800),
			(2,'Laptop',1200),
			(3,'Tablet',200),
			(4,'Monitor',350),
			(5,'Printer',150)
''')
conn.commit()
cursor.close()
conn.close()
"""
"""
QUSTION_4

import pyodbc

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-FK6DE25V\MSSQLS;'
    'Database=Connect_python;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

# Define the SQL query to retrieve all records from a specific table
table_name = 'product'
query = f"SELECT * FROM {table_name}"

# Execute the query
cursor.execute(query)

# Fetch all the data from the query result
rows = cursor.fetchall()

# Print the fetched data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
"""
"""
#QUSTION_5
import pyodbc

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-FK6DE25V\MSSQLS;'
    'Database=Connect_python;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

#queries for retrievint all rows
retrieve = "Select price from product;"

# executing the queries
cursor.execute(retrieve)
rows = cursor.fetchall()
total=0
for i in rows:
    total=total + i[0]
avg=total/len( rows)

#calculating standard deviation of the dataset

print("Average price:",avg)

cursor.close()
conn.close()

"""
"""
#QUSTION_6

import pyodbc
import numpy as np

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-FK6DE25V\MSSQLS;'
    'Database=Connect_python;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

# Select subset of records based on specific criteria
cursor.execute('SELECT * FROM product WHERE price > ?', (500,))
selected_rows = cursor.fetchall()

# Get the price values from the selected rows
prices = [row.price for row in selected_rows]

# Calculate mean and standard deviation
mean = np.mean(prices)
std_dev = np.std(prices)

# Print the calculated statistics
print(f"Mean: {mean}")
print(f"Standard Deviation: {std_dev}")

cursor.close()
conn.close()
"""
