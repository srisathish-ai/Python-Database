import os
from pymongo import MongoClient
from dotenv import load_dotenv

def mongo_connection():
    client = MongoClient("mongodb://{}:{}".format(os.getenv('MONGO_HOST'),os.getenv('MONGO_PORT')))
    db = client[os.getenv('MONGO_DB')]
    try: 
        db.command("serverStatus")
    except Exception as e: print(e)
    else:
        print("MongoDB connected!!!")
        list_of_databases = client.list_database_names()
        is_db_exists(list_of_databases)
        list_of_collection = db.list_collection_names()
        is_collection_exists(list_of_collection)
    client.close()

def is_db_exists(listofdatabases):
    if "admin" in listofdatabases:
        print("admin database is exists")
    else:
        print("admin database is not exists")

def is_collection_exists(listofcollection):
    if "customer" in listofcollection:
        print("customer database is exists")
    else:
        print("customer database is not exists")        
    


if __name__ == "__main__":
    load_dotenv(dotenv_path='../.env')
    mongo_connection()