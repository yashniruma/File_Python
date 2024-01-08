import mysql.connector
from tkinter import *
import tkinter

master =Tk()
Label(master,text='Name ').grid(row=0)

Label(master,text='MobilNo').grid(row=1)

e1 =Entry(master)
e2 =Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

mainloop()


def insert(con,cur):


    nm=input("Enter Name :- \n ")
    mo=input("Enter Mobile Number :- \n")

    sql="INSERT INTO data (Name ,mobile) VALUES (%s,%s)"

    val =(nm,mo)

    cur.execute(sql,val)

    con.commit()

    print(cur.rowcount,"Data Inserted")

def update(con,cur):
    nm = input("Enter Name :- \n ")
    mo = input("Enter Mobile Number :- \n")

    sql ="update data set Name='"+nm+"',mobile='"+mo+"'"

    cur.execute(sql)

    con.commit()

    print(cur.rowcount,"#Data Updeted ")

def delete(con,cur):
    mo = input("Enter Mobile Number :- \n")

    sql = "delete FROM data where mobile ='"+mo+"'"

    cur.execute(sql)

    con.commit()

    print(cur.rowcount ,"Data Deleted.")

def display(con,cur):

    cur.execute("SELECT * FROM data")

    res= cur.fetchall()

    print("_______________*****___________________")

    print ("Name   Mobile No")
    print("______________________________________")

    for  e in res:
        # print(str(e[0] + " " +e[1]+""))
        print(e)
    print("_______________*****___________________")

def main():
    con =mysql.connector.connect(host="localhost",user="root",password="",database="pcrud")

    cur =con.cursor()


    ch=0

    while(ch<=4):

        print("1. INSERT")
        print("2. UPDATE")
        print("3. DELETE")
        print("4. DISPLAY")
        print("5. EXIT")

        ch=int(input("Enter Your Need :- "))

        if (ch==1):
            insert(con,cur)
        if (ch==2):
            update(con,cur)
        if (ch==3):
            delete(con,cur)
        if (ch==4):
            display(con,cur)

main()

















# import mysql.connector
#
# # try:
#
# con=mysql.connector.connect(host="localhost",user="root",password="",database="pcrud")
#
# if con.is_connected():
#      print("Done with connect **")
# else:
#     print("Somthing Wrong | DO Again ")
#
# cr=con.cursor()
#
# print("1 For Insert Data :-\n ")
# print("2 For Show Data :- \n ")
# print("3 For Delete Data :- \n ")
# print("4 For Update Data :- \n ")
#
# ch=int(input("Enter Your Need :- \n "))
#
# if ch==1:
#      name=input("Enter Your Name :-\n ")
#      mo=int(input("Enter Your Mobile Number :- \n"))
#
#      query='INSERT INTO data values (%s,%s)'
#
#      dt=(name,mo)
#
#      cr.execute(query,dt)
#
#      con.commit()
#
#      print("Data Inserted ")
#
# elif ch==2:
#     select=""" SELECT * FROM data """
#
#     cr.execute(select)
#
#     sdata=cr.fetchall()
#
#     print("*******************")
#
#     for e in sdata:
#         print(e)
#
#     con.close
#
#     print("*******************")
#
# elif ch==3:
#
#
#
#
#
# else:
#     print("Invalid Choice !!!!")
#
#
# # except :
# #     print("Somthing Wrong DO Again !!!")
