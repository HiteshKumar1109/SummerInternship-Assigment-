import sqlite3
conn =sqlite3.connect("First.db")
# first table creation
sql="""
CREATE TABLE DEMO1(
STU_ID INTEGER PRIMARY KEY,
STU_NAME VARCHAR(20),
STU_AGE INTEGER,
STU_CLASS VARCHAR(20)
);"""
# create the second table
sql2="""
CREATE TABLE DEMO2(
EMP_ID INTEGER PRIMARY KEY,
EMP_NAME VARCHAR(20),
EMP_AGE INTEGER,
EMP_SALARY DECIMAL(10,2)
);"""
# THIRD TABLE CREATION
sql3="""
CREATE TABLE DEMO3(
PROD_ID INTEGER PRIMARY KEY,
PROD_NAME VARCHAR(20),
PROD_PRICE DECIMAL(10,2)
);"""


# FIRST INSERT THE DATA INTO THE FIRST TABLE
sql_insert1="""
INSERT INTO DEMO1(STU_ID,STU_NAME,STU_AGE,STU_CLASS) VALUES(1,'John',20,'A'),
(2,'Alice',22,'B'),(3,'Bob',21,'C');"""

# NOW INSERT THE DATA INTO THE SECOND TABLE
sql_insert2="""
INSERT INTO DEMO2(EMP_ID,EMP_NAME,EMP_AGE,EMP_SALARY) VALUES(1,'David',30,50000.00),
(2,'Emma',28,60000.00),(3,'Michael',35,70000.00);"""

# NOW INDERT THE DATA INTO THE THIRD TABLE
sql_insert3="""
INSERT INTO DEMO3(PROD_ID,PROD_NAME,PROD_PRICE) VALUES(1,'Laptop',1000.00),
(2,'Smartphone',500.00),(3,'Tablet',300.00);"""


#Perform diffrent select operations
#select whole data from all tbales
sql_select1="SELECT * FROM DEMO1;"
sql_select2="SELECT * FROM DEMO2;"
sql_select3="SELECT * FROM DEMO3;"
data=conn.execute(sql_select1)
for row in data:
    print(row)
# (1, 'John', 20, 'A')
# (2, 'Alice', 22, 'B')
# (3, 'Bob', 21, 'C')
data1=conn.execute(sql_select2)
for row in data1:
    print(row)
# (1, 'David', 30, 50000)
# (2, 'Emma', 28, 60000)
# (3, 'Michael', 35, 70000)
data2=conn.execute(sql_select3)
for row in data2:
    print(row)
# (1, 'Laptop', 1000.00)
# (2, 'Smartphone', 500.00)
# (3, 'Tablet', 300.00)

data4=conn.execute("select stu_name from Demo1 where stu_age>20;")
for row in data4:
    print(row)
# ('Alice',)
# ('Bob',)
data5=conn.execute("select * from demo2 order by emp_salary desc;")
for row in data5:
    print(row)
# (3, 'Michael', 35, 70000)
# (2, 'Emma', 28, 60000)    
# (1, 'David', 30, 50000)
data6=conn.execute("select * from demo3 where prod_price>400;") 
for row in data6:
    print(row)
# (1, 'Laptop', 1000.00)
# (2, 'Smartphone', 500.00)

#update the data in table
conn.execute("update demo1 set stu_age=70 where stu_id=2 ;")
data7=conn.execute("select * from demo1;")
for row in data7:
    print(row)
# (1, 'John', 20, 'A')
# (2, 'Alice', 70, 'B')
# (3, 'Bob', 21, 'C')
conn.commit()
conn.execute("update demo2 set emp_salary=80000 where emp_id=1;")
conn.commit()
data8=conn.execute("select * from demo2;")
for row in data8:    print(row)
# (1, 'David', 30, 80000)

conn.execute("delete from demo3 where prod_id=3;")
conn.commit()
data9=conn.execute("select * from demo3;")
for row in data9:
    print(row)  
# (1, 'Laptop', 1000)
# (2, 'Smartphone', 500) 