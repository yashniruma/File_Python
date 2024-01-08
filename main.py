# import mysql.connector as onkar
# conn = onkar.connect(host="localhost:3307",user="root",password="",database="")
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pcrud"
    # database="onkar"    is's a table name
)

if conn.is_connected():
    print("Done with Connecte")

cr=conn.cursor()

# i=input("Enter Your ID Number  :- \n ")
nm=input("Enter Your Full Name :- \n ")
m=input("Enter Your Mobile Number  :- \n ")


# insert_query='INSERT INTO data values (%s,%s,%s)'
insert_query='INSERT INTO data values (%s,%s)'

# data =(nm,m,i)
data =(nm,m)

cr.execute(insert_query,data)

conn.commit()




