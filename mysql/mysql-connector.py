import os
import mysql.connector
from dotenv import load_dotenv

    
def Mysql_connection():
    try:
        mydb = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            passwd=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DB')
        )

        mycluster = mydb.cursor()
        print("Mysql Connection")
        mycluster.execute('SELECT * FROM db')
        for i in mycluster:
            print(i)
    except mysql.connector.DatabaseError as error:
        print("There is a problem with mysql connection \n",error)
    finally:
        if mycluster is not None:
            mycluster.close()
            print("The MySQL connection is Closed")

if __name__ == "__main__":
    load_dotenv(dotenv_path='../.env')
    Mysql_connection()
