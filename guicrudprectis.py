# from distutils.util import execute
# import mysql.connector as mysql
import mysql.connector 
from tkinter import *

import tkinter.messagebox as MessageBox
# from c import insert

r=Tk()
r.geometry("500x500")
r.title("File No Sambhave Nikal")

n = Label(r,text="Enter Name :",font="verdana 15")
n.pack()
ne=Entry(r,font="verdana 15")
ne.pack()

m = Label(r,text="Enter Mo No :",font="verdana 15")
m.pack()
mo=Entry(r,font="verdana 15")
mo.pack()


def insert():
    n=ne.get()
    m=mo.get()

    if (n == "" or m ==""):
        MessageBox.showinfo("ALERT","All Filed Are REQUIRED")
    else:
        con = mysql.connector.connect(host="localhost",user="root",password="",database="26\jun")
        cur =con.cursor()
        cur.execute("insert into mox values('"+n+"','"+m+"')")
        cur.execute("commit")

        MessageBox.showwarning("Status","Data Saved")
        ne.delete(0,'end')
        mo.delete(0,'end')
        con.close()





save =Button(r,text="SAVE ",font="verdana 15",command=insert)
save.pack()





r.mainloop()




# con  =mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database ="26\jun"
# )

# if con.is_connected():
#     print("Connected >>>>>>>>>")

# cur = con.cursor()

# name =input("Enter your name :-\n ")
# mono  =input("Enter your mo no :-\n ")

# cur.execute("insert into mox values('"+name+"','"+mono+"')")
# cur.execute("commit")

# con.close()



# con = mysql.connect(host ="localhost",user="root",password="",database="26\jun")
#         cur =con.cursor()
#         cur.execute("insert into amba values ('"+ide+"','"+unm+"','"+pas+"')")
#         cur.execute("Commit ")

#         MessageBox.showinfo("Status","Saved")
#         con.close();

# import mysql.connector as onkar
# conn = onkar.connect(host="localhost:3307",user="root",password="",database="")







