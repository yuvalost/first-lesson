import sqlite3
connect_manager = sqlite3.connect("users.db")
cursor = connect_manager.cursor()

# Step 1
first_name = input("please insert first name? ")
last_name = input("please insert last name? ")
age = int(input("please insert age? "))
address = input("please insert address? ")

# Step 2

# Step 3
table_create_query = """
CREATE TABLE IF NOT EXISTS users (first_name TEXT, last_name TEXT, age INT, address TEXT)

"""

connect_manager.execute(table_create_query)

data_insert_query = """
INSERT INTO user (first_name, last_name, age, address) VALUES (?,?,?,?)
"""

# Step 4
data_insert_tuple = (first_name, last_name, age, address)
cursor.execute(data_insert_query, data_insert_tuple)

connect_manager.commit()

# Last Step
for row in cursor.execute("SELECT * FROM users"):
    print(row)

connect_manager.close()
