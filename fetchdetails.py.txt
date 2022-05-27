import mysql.connector as mariadb
con=mariadb.connect(host='localhost',user='user1',password='abc@123',database='Employee')
print("Connection Established Successfully!")
cur=con.cursor()
cur.execute("select * from Employee Where salary>50000")
for row in cur:
    print(row)
cur.close()
con.commit()
con.close()

