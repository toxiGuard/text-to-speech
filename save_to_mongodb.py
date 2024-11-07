import os
from pymongo import MongoClient
from datetime import datetime

def save_to_mongodb(name):
    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        raise ValueError("MONGO_URI environment variable is not set")

    client = MongoClient(mongo_uri)
    try:
        db = client['test']  # Replace 'test' with your database name
        collection = db['test']  # Replace 'greetings' with your collection name
        
        doc = {
            "name": name,
            "date": datetime.now()
        }
        
        result = collection.insert_one(doc)
        print(f"Name '{name}' saved to MongoDB with ID: {result.inserted_id}")
    except Exception as e:
        print("Error saving to MongoDB:", e)
    finally:
        client.close()

if __name__ == "__main__":
    name = os.getenv("NAME")
    if name:
        save_to_mongodb(name)
    else:
        print("No name provided")
