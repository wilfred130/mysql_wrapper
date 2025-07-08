from mysql_wrapper import DatabaseConnection

# database connection
mydb = DatabaseConnection(
    host='localhost',
    user='root',
    password='root',
    database='db'
)


# update data
query = "UPDATE user SET name= 'karmal Rayan' WHERE user_id = 1;"
mydb.execute_update(query)

# insert user
query = "INSERT INTO user(name, email) VALUES('Gift Franklyne', 'franklyne@example.com')"
mydb.execute_update(query)

# Reading data
query= 'SELECT * FROM user;'
users = mydb.execute_read(query)
print(users)

# delete user
query = 'DELETE FROM user WHERE user_id = 10'
mydb.execute_delete(query)

# Reading data
query= 'SELECT * FROM user;'
users = mydb.execute_read(query)
print(users)
