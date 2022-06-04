import mysql.connector as mariadb
con=mariadb.connect(host='localhost',user='user1',password='abc@123',database='Employee')
print("Connection Established Successfully!")
cur=con.cursor()
cur.execute("insert into Employee values(1007,'Rita','Developer',1001,'2021-09-30',50000,20)")
print("Data Added Successfully!")
cur.close()
con.commit()

con.close()

