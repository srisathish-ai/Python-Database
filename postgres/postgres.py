import os
import psycopg2
from dotenv import load_dotenv


def postgres_connection():
    load_dotenv(dotenv_path='../.env')
    try:
        conn = psycopg2.connect(
            host=os.getenv('PG_HOST'),
            port=os.getenv('PG_PORT'),
            user=os.getenv('PG_USER'),
            password=os.getenv('PG_PASSWORD'),
            database=os.getenv('PG_DB')
        )

        mycluster = conn.cursor()
        print('Postgres connection')
        mycluster.execute('SELECT * FROM public.role')
        for i in mycluster:
            print(i)
    except psycopg2.DatabaseError as error:
        print("There is a problem with postgres \n",error)
    finally:
        if mycluster is not None:
            mycluster.close()
            print("The Postgres connection is Closed")

if __name__ == "__main__":
    postgres_connection()