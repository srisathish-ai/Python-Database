import os
import cx_Oracle
from dotenv import load_dotenv

def oracle_connection():
    username = os.getenv('ORACLE_USER')
    password = os.getenv('ORACLE_PASSWORD')
    host = os.getenv('ORACLE_HOST')
    port = os.getenv('ORACLE_PORT')
    database = os.getenv('ORACLE_DB')
    conn = cx_Oracle.connect(username+'/'+password+'@'+host+':'+port+'/'+database,mode=cx_Oracle.SYSDBA)
    data = conn.cursor()
    data.execute('SELECT owner,table_name from all_tables')
    for i in data:
        print(i)

if __name__ == "__main__":
    load_dotenv(dotenv_path='../.env')
    oracle_connection()