import asyncio
from collector.twitter.twikit_collector import TwikitHarvester
from database.mongo_manager import MongoManager

async def main():
    target = "Cristiano"
    
    # Initialize DBs
    mongo = MongoManager()
    
    # Initialize Harvester
    harvester = TwikitHarvester()
    
    # 1. Check Cache
    if mongo.get_cached_user(target):
        print(f"✅ Target {target} is already in the Aggregation Layer.")
    
    # 2. Collect Data
    data = await harvester.get_mega_data(target, tweet_count=100)
    
    # 3. Store Raw in Mongo (Point 5: Cache)
    mongo.upsert_user(data["account_metadata"])
    mongo.save_tweets(data["tweets"])
    
    print(f"📊 Harvest complete. Data persisted in Docker Stack.")

if __name__ == "__main__":
    asyncio.run(main())