import os
import mysql.connector
from dotenv import load_dotenv

class Mysql:
    load_dotenv(dotenv_path='../.env')
    def Mysql_connection():
        mydb = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            passwd=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DB')
        )

        mycluster = mydb.cursor()

        mycluster.execute('SELECT * FROM db')
        for i in mycluster:
            print(i)

if __name__ == "__main__":
    Mysql.Mysql_connection()
