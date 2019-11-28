import mysql.connector

class Mysql:
    def Mysql_connection():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Sathish-12#",
            database="mysql"
        )

        mycluster = mydb.cursor()

        mycluster.execute('SELECT * FROM db')
        for i in mycluster:
            print(i)

if __name__ == "__main__":
    Mysql.Mysql_connection()
