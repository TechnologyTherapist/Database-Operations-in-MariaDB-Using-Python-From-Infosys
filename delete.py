import mysql.connector as mariadb
con=mariadb.connect(host='localhost',user='user1',password='abc@123',database='Employee')
print("Connection Established Successfully!")
cur=con.cursor()
cur.execute("delete from Department where dname='Sales'")
print("Number of row deleted",cur.rowcount)
print("Data Deleted Successfully!")
cur.close()
con.commit()

con.close()
