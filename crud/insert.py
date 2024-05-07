import mysql.connector 

def insert_data():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="pcrud")

    try:
        if conn:
            print("Connected To  DataBase")

            cur = conn.cursor()

            mhtid = int(input("Enter Mht ID :- \n "))
            name =input("Enter Name :- \n ")

            sql = "INSERT into prec (mhtid , name)  values(%s, %s)"
            values= (mhtid , name)

            cur.execute(sql , values)

            conn.commit()
            conn.close()

            print("DATA INSERTED SUCCESSFULLY")
            

    except Exception as e:
        print(f"Problem Are :- {e}, \t Do Again")


# insert_data()

def update_data():
    print("******** Start Updating Data ******** \n \n" )

    conn = mysql.connector.connect(host="localhost", user="root", password="", database="pcrud")

    try:
        if conn:
            print("Connected To  DataBase")

            cur = conn.cursor()

            eid = int(input("Enter mhtid :-\t "))

            print(f"You Enter mhtid :- {eid} \t Loading .....")

            cur.execute("select mhtid from prec")

            mhtid = cur.fetchall()
            
            for mid in mhtid:
                # print(mid )

                if eid in mid:
                    # print("Yes Id data is present :- ", eid)
                    eid=str(eid)

                     # selectdata = "select * from prec where mhtid='"+eid+"'" 
                    cur.execute( "select * from prec  WHERE mhtid = %s", (mid) )
                    row= cur.fetchall()

                    for i in row:
                        # print(f"Unique id {i[0] ,i[1], i[2]}")
                        print(f"Name Data :- {i[2]}")
                        name =input("Enter Updated Data :- \t ")
                        # print(name) 
                      
                        cur.execute("update prec set name='"+name+"' WHERE mhtid='"+eid+"' ")
                        print("...............DATA UPDATED...............")

                        conn.commit()
                     
                        break  # Exit the loop after updating the first matching ID
                   
                    else:
                        print("No matching ID found")
                    break  # Exit the loop after finding the matching ID
                    
                        
                else:
                    print("Wrong mhtid, Enter Right ID")        

    except Exception as e:
         print(f"Problem Are :- {e}, \t Do Again")
    finally:
        conn.close()
# update_data()

def delete_data():
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="pcrud")
    
        cur = conn.cursor()

        mh= int(input("Enter mhtid For Delete :- \t"))

    #   First Check  id  is  exisist  or not in databases
        cur.execute("select mhtid from prec")
        # d =cur.fetchall()
        # print(f"{d} \t {type(d)}")
      
        d = [item[0] for item in cur.fetchall()]
        print(d)
        if mh in d:
            print("Your  ID  is  present DO process")
            # print(f"Are you  sure to delete {mhtid } data  \t yes  or  no")

            ch = input("Enter Yes  Or  No :- \t ")

            if ch == 'yes' or 'YES' or 'Yes' or 'yES':
            # if  ch == 'yes':
                    mh=str(mh)
                    cur.execute("delete from prec where mhtid='"+mh+"' ")

                    print("!!!!!!!!!!!! Data  Deleted successfully")
                    conn.commit()
                    conn.close()

    
        else:
            print("Wrong ID  please  Enter Correct ID")
    
       
   
    except Exception as r:
        print(f"Problem Are :- {r}, \t Do Again")
    
# delete_data()

def show_data():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="pcrud")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prec")

    data =cursor.fetchall()

    for i in data:
        print(" ----------------------------------------------------------- ")
        print(f"Uniqe id :- { i[0]}No need for you \n mhtid :- {i[1]}, \n Name :- {i[2]}" )
        print(" ----------------------------------------------------------- ")


def menu():
    while True:
        print(" \n \t_______WELCOME In Python CRUD_______\n ")
        print("1 for New Recored \n ")
        print("2 for Updated Recored \n ")
        print("3 for Delete  \n ")
        print("4 for  Show All  Data \n ")
        print("5 for  Exit() \n ")

        ch =  int(input("Enter  Need :- \t "))
        if ch == 1:
            insert_data()
        elif ch == 2:
            update_data()
        elif ch == 3:
            delete_data()
        elif ch== 4:
            show_data()
        elif ch == 5:
            break 
    print(" \n \t _______Thanks For Use This SOFTAWER_______ ,have  a good day")

menu()