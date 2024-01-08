from tkinter import *
import tkinter.messagebox as MessageMox
import mysql.connector as mysql

r=Tk()
r.geometry("500x300")
r.title("MySQL CRUD ")

def Insert():
    id = ide.get()
    nm = nme.get()
    ph = phe.get()

    if(id == "" or nm == "" or ph == ""):
        MessageMox.showinfo("ALERT","Please Enter All Fields **")
    else:
        con = mysql.connect(host="localhost",user="root",password="",database="gcrud")
        cursor = con.cursor()
        cursor.execute("insert into data values ('"+id +"', '"+nm+"','"+ph+"')")
        cursor.execute("commit")

        MessageMox.showinfo("Status" , "Successfully Inserted !!")
        con.close();


def Del():
    if(ide.get() == ""):
        MessageMox.showinfo("ALERT" , "Please Enter ID to Delete Row")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="gcrud")
        cursor = con.cursor()
        cursor.execute("delete from  data where id='"+ide.get() +"' ")
        cursor.execute("commit")

        ide.delete(0,'end')
        nme.delete(0,'end')
        phe.delete(0,'end')

        MessageMox.showinfo("Status","Successfull Deleted")
        con.close()



def Update():
    id = ide.get()
    nm = nme.get()
    ph = phe.get()

    if (id == "" or nm == "" or ph == ""):
        MessageMox.showinfo("ALERT", "Please Enter All Fields **")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="gcrud")
        cursor = con.cursor()
        cursor.execute("update data set nm= '"+nm+"' ,ph ='"+ph+"' where id= '"+ id+"' ")
        cursor.execute("commit")

        MessageMox.showinfo("Status", "Successfull Updated")
        con.close()

def Select():
    if ( ide.get() == "" ):
        MessageMox.showinfo("ALERT", "ID is Required to Select Row !")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="gcrud")
        cursor = con.cursor()
        cursor.execute("select * from data where id='"+ide.get()+"'  ")
        rows =cursor.fetchall()

        for row in rows:
            nme.insert(0 ,row[1])
            phe.insert(0,row[2])

        con.close();







id=Label(r,text="Enter ID : ",font=("verdana 15"))
id.place(x=50,y=30)
ide=Entry(r,font=("verdana 15"))
ide.place(x=150,y=30)

nm=Label(r,text="Enter Name :",font=("verdana 15"))
nm.place(x=10,y=80)
nme=Entry(r,font=("verdana 15"))
nme.place(x=150,y=80)

ph =Label(r,text="Enter Phone :",font=("verdana 15"))
ph.place(x=10, y=130)
phe=Entry(r,font=("verdana 15"))
phe.place(x=150,y=130)


btnInsert = Button(r, text="Insert", command=Insert ,font=("verdana 15")).place(x=100,y=190)
btnDelete = Button(r, text="Delete", command=Del,font=("verdana 15") ).place(x=200,y=190)
btnUpdate = Button(r, text="Delete", command=Update,font=("verdana 15") ).place(x=320,y=190)
btnSelect = Button(r, text="Select", command=Select,font=("verdana 15") ).place(x=200,y=240)

r.mainloop()



