import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

class MongoManager:
    def __init__(self):
        # Load URI and DB Name from .env
        uri = os.getenv("MONGO_URI")
        db_name = os.getenv("MONGO_DB_NAME", "osint_persona_mapping")
        
        if not uri:
            raise ValueError("❌ MONGO_URI not found in .env file")

        # Initialize Client
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        
        self.users = self.db["users"]
        self.tweets = self.db["tweets"]
        
        # This is where it failed before; it should work now with authSource=admin
        print(f"📡 Connecting to MongoDB: {db_name}...")
        self.users.create_index("username", unique=True)
        self.tweets.create_index("id", unique=True)