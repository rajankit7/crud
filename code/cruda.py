import mysql.connector as ankit
conn=ankit.connect(host="localhost",user="root",password="",database="ankit")
cursor=conn.cursor()
def insert():
  name=input("Enter your name:")
  phone=input("Enter your phone:")
  sql="insert into ankit(name,phone)values(%s,%s)"
  val=(name,phone)
  try:
    cursor.execute(sql,val)
    conn.commit()
    print("Succesful")
    menu()
  except exception as e:
    print(e)
    menu()
def read():
  sql="select*from ankit"
  try:
    cursor.execute(sql)
    data=cursor.fetchall()
    for x in data:
       print(x)
    print("Successful")
    menu()
  except:
    print("Error occured")
    menu()
def delete():
  ch=input("Do you have row id?(y/n)").lower()
  if(ch=='y'):
     idd=input("Enter your row id")
     sql="delete from ankit where id=%s"
     val=(idd,) 
     try:
       cursor.execute(sql,val)
       conn.commit()
       print("Succesful")
       menu()
     except:
       print("Error")
       menu()
       
  else:
    print("Go to read section and get your id")
    menu()
def update():
   ch=input("Do you have row id?(y/n)").lower()
   if(ch=='y'):
     idd=input("Enter your row id")
     sql="select * from ankit where id=%s"
     val=(idd,)
     try:
        cursor.execute(sql,val)
        data=cursor.fetchall()
        for x in data:
          name=x[1]
          phone=x[2]
        print("1.update phone\n2.update name")
        ch=int(input("Enter your choice:"))
        if(ch==1):
           phone=input("Enter your value")
        elif(ch==2):
            name=input("Enter your new name")
        else:
          print("Wrong input")
          menu()
        sql="update ankit set name=%s,phone=%s where id=%s"
        val=(name,phone,idd)
        try:
            cursor.execute(sql,val)
            conn.commit()
            print("succesful")
            menu()
        except exception as e:
           print(e)
           menu()
     except:
         print("error")
         menu()
        
  
def menu():
  print("Select any option\n1.Insert\n2.Read\n3.Update\n4.Delete")
  ch=int(input("Enter your choice:"))
  if(ch==1):
      insert()
  elif(ch==2):
      read()
  elif(ch==3):
      update()
  elif(ch==4):
      delete()
  else:
    print("Wrong input choose")
    menu()


menu()
