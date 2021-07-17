import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',user='bhaskar',password='bhaskar123',database='pythontest',auth_plugin='mysql_native_password')
        query = 'create table if not exists user(userId int primary key,username varchar(200), phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")

    def insert_user(self,userId,username,phone):
        query="insert into user(userId,username,phone) values ({},'{}','{}')".format(userId,username,phone)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("USer Id: " ,row[0])
            print("User Name: " ,row[1])
            print("User Phone: " ,row[2])

    def delete_user(self,userId):
        query="delete from user where userId={}".format(userId)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

    def update_user(self,userId,newName,newPhone):
        query="update user set username='{}' ,phone='{}' where userId={}".format(newName,newPhone,userId)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")
