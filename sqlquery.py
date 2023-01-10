import mysql.connector as ms
conn = ms.connect(host = 'localhost',user = 'root',passwd = 'nkr7exfkyg',database = 'mydb2')
if conn.is_connected():
    print('Connected!')
mycursor = conn.cursor()
# ecode = input('Enter employee code: ')
# ename = input('Enter employee name: ')
# salary = int(input('Enter salary: '))
# query = "INSERT INTO EMP VALUES ('{}','{}',{})".format(ecode,ename,salary)
query = "SELECT * FROM EMP"
mycursor.execute(query)
data  = mycursor.fetchall()
for i in data:
    print(i[0],i[1],i[2])