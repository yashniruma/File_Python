from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    # id = int (ide.get())
    id =  ide.get()
    unm = unme.get()
    pas = pase.get()



    # if id !="":
    #     MessageBox.showinfo("ALERT", "id allocete by SS ")
    if  unm== "" or pas == ""  :
            # MessageBox.showinfo("ALERT","Please enter all fields")
             MessageBox.showinfo("ALERT","id allocete by SS")



    else:
        con = mysql.connect(host ="localhost",user="root",password="",database="26\jun")
        cur =con.cursor()
        cur.execute("insert into amba values ('"+ide+"','"+unm+"','"+pas+"')")
        cur.execute("Commit ")

        MessageBox.showinfo("Status","Saved")
        con.close();




r=Tk()
r.geometry("500x500")
r.title("CRUD")


id =Label(r,text ="Enter ID NO Enter :- ",font=("verdana 15"))
id.place(x=50,y=30)
ide=Entry(r,font=("verada 15"))
ide.place(x=220,y=130)

unm =Label(r,text ="Enter Name :- ",font=("verdana 15"))
unm.place(x=50,y=130)
unme=Entry(r,font=("verada 15"))
unme.place(x=220,y=30)

pas =Label(r,text="Enter Pasword :-",font=("verdana 15"))
pas.place(x=10,y=80)
pase=Entry(r,font=("verdana 15"))
pase.place(x=210,y=90)



btnsave =Button(r,text="OK" ,command=insert,font=("verdana 15")).place(x=100,y=200)
# btnInsert = Button(r, text="Insert", command=Insert ,font=("verdana 15")).place(x=100,y=190)


r.mainloop()