import mysql.connector
database="test"
conn = mysql.connector.connect(host="localhost",user="root",password="",database="test")

if conn.is_connected():
    print(f"Connected To {database} ")

def insert():
    cur =conn.cursor()
    try :
        fnm = input("Enter First Name :- \t").upper()
        if fnm =="":
            while fnm == "":
                print("ALERT :::::: -->" , f"First name Needed")
                fnm = input("Enter First Name :- \t").upper()

        mnm = input("Enter Middle Name :- \t").upper()
        if mnm=="":
            while mnm == "":
                print("ALERT :::::: -->", f"Middle name Needed")
                mnm = input("Enter Middle Name :- \t").upper()

        lnm = input("Enter Last Name :- \t").upper()
        if lnm=="":
            while lnm == "":
                print("ALERT :::::: -->", f"Last name Needed")
                lnm = input("Enter Last Name :- \t").upper()

        mono = input("Enter Mobile No :- \t")
        # // use isdigit()
        #   do not use INT   but use   BIGINT
        while mono == "":
              if mono !=10:
                    print("ALERT :::::: -->", f"Mono Needed")
                    mono = input("Enter Mobile No :- \t")

        city = input("Enter City :- \t").upper()
        while city == "":
            print("ALERT :::::: -->", f"City is Needed ")
            city = input("Enter Your City:- \t").upper()

    except Exception as f:
        print(f"Error Are :- \t {f} ")

    cur.execute("insert into de values ('"+fnm+"','"+mnm+"','"+lnm+"','"+str(mono)+"','"+city+"' )")

    cur.execute("commit")

    # def gi():
    #     conn =mysql.connector.connect(host="localhost",user ="root",passwrod="",database="test")
    #     cur =conn.cursor()
    #     cur.execute("select * from de LIMIT 1")
    #     row=cur.fetchone()
    #
    #     print(row [0])
    #
    #     # print("id:-" , row)

    print("...... Data Inserted ...........")
    # print(f"Your Id No :- \t {gi()}")

    cur.close()

# insert()

def select():
    import mysql.connector

    conn = mysql.connector.connect(host="localhost",user='root',password="",database="test")



    if conn.is_connected():
        print ("::::::::::::::::::::::::::::::::: Database Ready For CRUD :::::::::::::::::::::::::::::::::")

    cur = conn.cursor()
    cur.execute("select * from de ")
    # cur.execute("select fnm from de ")


    dt =cur.fetchall()

    for a in dt:
        print(a)

    cur.execute("commit")
    cur.close()

def delete():
    conn  = mysql.connector.connect(host="localhost",user="root",password="",database="test")
    cur = conn.cursor()
    mono1 = input("Enter Mobile Number :- \t")
    cur.execute("delete from de where mono='"+mono1+"' ")
    cur.execute("commit")

    print("!!!!!!!!! Recored Deleted !!!!!!!!!!!!!!!!")
    cur.close()

def update():
    select()
    fnm = input("Update First Name :- \t ").upper()
    mnm = input("Update Middle Name :- \t ").upper()
    lnm = input("Update Last Name :- \t ").upper()
    mono = input("Update Mo Number Name :- \t ")
    city =input("Update City Name :- \t ").upper()

    conn =mysql.connector.connect(host="localhost",user ="root",password="",database="test")
    cur=conn.cursor()

    # mono = input("Update Mo Number Name :- \t ")
    # while mono == "":
    #     print("Mo No is Needed For Update data")
    #     mono = input("Update Mo Number Name :- \t ")

    # UPDATE `de` SET `fnm` = 'Kpl' WHERE `de`. `id` = 5;
    cur.execute("update de set fnm='"+fnm+"',mnm='"+mnm+"',lnm='"+lnm+"',mono='"+mono+"',city='"+city+"' where  mono='"+mono+"' ")
    cur.execute("commit")
    cur.close()


print("1 --> Insert Data ")
print("2 --> Show  Data ")
print("3 --> Delete  Data ")
print("4 --> Update  Data ")


choice  = int(input("Enter Choice :- \t"))

if choice == 1:
    insert()
elif choice ==2:
    select()
elif choice ==3:
    delete()
elif choice ==4:
    update()
else:
    print("!!!!!!!!! Select Properly !!!!!!!!!")







