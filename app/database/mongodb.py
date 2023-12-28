# TextClassificationAPI/app/database/mongodb.py

from pymongo import MongoClient
from app import config

def get_mongo_client():
    mongo_uri = config.Config.MONGODB_URI
    client = MongoClient(mongo_uri)
    return client

def save_to_mongodb(data):
    try:
        client = get_mongo_client()
        db = client.get_database("TextClassification")
        collection = db.get_collection("Cluster0")

        result = collection.insert_one(data)

        print(f"Data saved to MongoDB. Inserted ID: {result.inserted_id}")
    except Exception as e:
        print(f"Error saving data to MongoDB: {e}")
    finally:
        client.close()