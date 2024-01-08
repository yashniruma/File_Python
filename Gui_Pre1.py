from _ast import Delete
from tkinter import *
import tkinter.messagebox as MessageBox

import  mysql
import mysql.connector as mysql

r=Tk()
r.geometry("1000x500")
r.title("R.CRUD")


def Insert():
    id=ide.get()
    nm=nme.get()
    ph=phe.get()

    if(id == "" or nm == "" or ph == ""):
        MessageBox.showinfo("ALERT","Please Enter All Field")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="guipre1")
        cur=con.cursor()
        cur.execute("insert into data values('"+ id +"','"+ nm +"','"+ ph +"')")
        cur.execute("commit")

        MessageBox.showinfo("Status", "Successfully Inserted !!")
        con.close();

def Delete():
    if(ide.get() == ""):
        MessageBox.showinfo("ALERT", "ID is Required !!!")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="guipre1")
        cu=con.cursor()
        cu.execute("delete from data where id='"+ide.get()+"' ")
        cu.execute("commit")

        ide.delete(0,"end")
        nme.delete(0,"end")
        phe.delete(0,"end")

        MessageBox.showinfo("Status", "Successfull Deleted")
        con.close()


def Update():
    id=ide.get()
    nm=nme.get()
    ph=phe.get()

    if(id == "" or nm == "" or ph==""):
        MessageBox.showinfo("ALERT", "All Field Required !!")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="guipre1")
        cur=con.cursor()
        cur.execute("update data set nm = '"+nm+"' ,ph = '"+ph+"'  where id ='"+id+"'  ")
        cur.execute("commit")

        MessageBox.showinfo("Status","Data Updeted #")
        con.close()

def Select():
    if (ide.get() == ""):
        MessageBox.showinfo("ALERT", "ID is Required !!")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="guipre1")
        cur=con.cursor()
        cur.execute("select * from data where id= '"+ide.get()+"'  ")
        rows= cur.fetchall()

        for row in rows:
            nme.insert(0,row[1])
            phe.insert(0,row[2])

        con.close()


id=Label(r,text="Enter Your ID :- ",font=("verdana 15 "),bg=("Green"),fg=("black"))
# id.place(x=50,y=30)
id.pack()
ide=Entry(r,font=("verdana 15"))
# ide.place(x=240,y=30)
ide.pack()

nm=Label(r,text="Enter Your Name :- ",font=("verdana 15"),bg=("green"),fg=("black"))
# nm.place(x=30,y=80)
nm.pack()
nme=Entry(r,font=("verdana 15"))
# nme.place(x=240,y=30)
nme.pack()

ph=Label(r,text="Enter PhoneNo :- ",font=("verdana 15"), bg=("green"),fg=("black"))
ph.pack()
phe=Entry(r,font=("verdana 15"))
phe.pack()

bin=Button(r,text="INSERT",command=Insert,font=("verdana 15")).place(x=100,y=100)
bdel=Button(r,text="DELETE", command=Delete,font=("verdana 15")).place(x=100,y=140)
bup=Button(r,text="UPDATE", command=Update,font=("verdana 15")).place(x=100,y=180)
bsel=Button(r,text="SELECT", command=Select,font=("verdana 15")).place(x=100,y=220)

r.mainloop()