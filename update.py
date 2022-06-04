import mysql.connector as mariadb
con=mariadb.connect(host='localhost',user='user1',password='abc@123',database='Employee')
print("Connection Established Successfully!")
cur=con.cursor()
cur.execute("update Employee set salary=salary+10000")
print("Number of row updated!",cur.rowcount)
print("Data Updated Successfully!")
cur.close()
con.commit()
con.close()

