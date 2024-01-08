import mysql.connector

def insert():

    conn=mysql.connector.connect(host="localhost",user="root",password="",database="test")

    nm =input("Enter Your Name :- \t").upper()
    lnm =input("Enter Your Lastname :- \t").upper()
    surnm =input("Enter Your Surname :- \t").upper()
    mono =input("Enter Your MoNo :- \t").upper()
    city =input("Enter Your City :- \t").upper()

    cur =conn.cursor()

    cur.execute("insert into data values('"+nm+"','"+lnm+"','"+surnm+"','"+mono+"','"+city+"')")
    cur.execute("commit")

    print("..........RECORED SAVED..........")
    cur.close()

def delete():
    conn = mysql.connector.connect(host="localhost",user="root",password="",database="test")
    cur=conn.cursor()

    nm = input("Enter Your Name :- \t")

    if not nm.upper():
        print(" ______ NAME MUST HAVE UPPER CASE ______")

    cur.execute("delete from data where nm='"+nm+"' ")

    print("..........RECORED DELETED..........")
    cur.execute("commit")
    cur.close()

def select():
    conn =mysql.connector.connect(host="localhost",user="root",password="",database="test")

    # nm = input("Enter Your Name :- \t")

    cur =conn.cursor()
    # cur.execute("select * from data where nm= '"+nm+"' ")
    cur.execute("select * from data")
    row=cur.fetchall()
    for a in row:
        print(a)

    cur.execute("commit")
    cur.close()

def update():
    conn =mysql.connector.connect(host="localhost",user="root",password="",database="test")

    cur =conn.cursor()
    nm = input("Enter Your Name :- \t").upper()
    lnm = input("Enter Your Lastname :- \t").upper()
    surnm = input("Enter Your Surname :- \t").upper()
    mono = input("Enter Your MoNo :- \t").upper()
    city = input("Enter Your City :- \t").upper()

    cur.execute("update data set lnm='"+lnm+"',surnm='"+surnm+"',mono='"+mono+"',city='"+city+"' where nm='"+nm+"' ")

    print("...............DATA UPDATED...............")

    # cur.execute("update data set nm = '" + nm + "' ,ph = '" + ph + "'  where id ='" + id + "'  ")
    cur.execute("commit")
    cur.close()

while True:
    print("<<<<<<<<<<< WELCOME TO CRUD OPERATIONS >>>>>>>>>>>>>>>>")
    print("1 FOR INSERT")
    print("2 FOR DELETE")
    print("3 FOR SELECT")
    print("4 FOR UPDATE")
    print("5 FOR EXIT")

    ch = int(input(":::::: ENTER CHOICE :::::: :-> \t \t"))

    if ch == 1:
        insert()
    elif ch==2:
        delete()
    elif ch==3:
        select()
    elif ch==4:
        update()
    elif ch==5:
        exit()
    else:
        print("-----_-------- SOMTHING WRONG DO AGAIN -----_--------")



