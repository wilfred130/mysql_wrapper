# mysql-inter-wrapper

This is a lightweight Python utility that wraps common MySQL operations (CRUD) using mysql-connector-python. It provides clean, reusable methods for SELECT, INSERT, UPDATE, DELETE, and parameterized queries, with support for Pandas DataFrames and error handling. 

# MySQL DB Helper for Python 🐍🛠️

It provides most of the functionality using only 4 function so you don't need to burn hours watching tutorial. Each function can execute basic queries, join queries, stored procedures, transations and many more. Just know the right utility function to consume --> `execute_read' FOR all SELECT operations, `execute_update` FOR ALL updates, `execute_delete` all data removal, `execute_update` for insertions as well. So the only thing is!! Juggle your queries.

---

## ✅ Features

- Easy-to-use CRUD operations
- Parameterized query support
- Built-in error handling
- Clean connection management
- Returns query results as Pandas DataFrames

---

## 📦 Installation

```bash
pip install mysql-inter-wrapper==1.0.1
```

---

---

## 🔧 Usage Example

```python
from mysql_helper import DatabaseConnection

# database connection
mydb = DatabaseConnection(
    host='localhost',
    user='root',
    password='password',
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
```

---

## 📚 Stored Procedure Examples

### 1. Stored Procedure to Update User

**MySQL Stored Procedure:**

```sql
DELIMITER //
CREATE PROCEDURE updateUser(IN userId INT, IN newEmail VARCHAR(100))
BEGIN
    UPDATE users SET email = newEmail WHERE id = userId;
END //
DELIMITER ;
```

**Python Usage:**

```python
# Calling the stored procedure to update email
update_proc = "CALL updateUser(1, 'updated@example.com')"
mydb.execute_update(update_proc)
```

---

### 2. Stored Procedure to Handle Transaction

**MySQL Stored Procedure:**

```sql
DELIMITER //
CREATE PROCEDURE transferAmount(
    IN senderId INT,
    IN receiverId INT,
    IN amount DECIMAL(10,2)
)
BEGIN
    START TRANSACTION;
    UPDATE accounts SET balance = balance - amount WHERE id = senderId;
    UPDATE accounts SET balance = balance + amount WHERE id = receiverId;
    COMMIT;
END //
DELIMITER ;
```

**Python Usage:**

```python
# Transfer 100.00 from user 1 to user 2
transfer_proc = "CALL transferAmount(1, 2, 100.00)"
mydb.execute_update(transfer_proc)
```

---

---

## 🧪 Dependencies

- `mysql-connector-python`
- `pandas`

---

## 📄 License

MIT License
Copyright (c) 2025 Wilfred Kisitu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
