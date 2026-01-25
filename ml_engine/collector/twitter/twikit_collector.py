import os
import asyncio
from twikit import Client, TooManyRequests
from database.mongo_manager import MongoManager # Import Cache

class TwikitHarvester:
    def __init__(self):
        self.client = Client("en-US")
        self.db = MongoManager() # Initialize Cache
        
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.cookies_path = os.path.abspath(
            os.path.join(BASE_DIR, "../../../storage/cookies.json")
        )

    def login(self):
        """Strict Manual Login logic..."""
        if not os.path.exists(self.cookies_path):
            raise FileNotFoundError("Manual cookies.json missing.")
        self.client.load_cookies(self.cookies_path)
        print("🍪 Session Injected.")

    async def get_mega_data(self, username, tweet_count=50):
        self.login()
        
        # --- 1. CHECK CACHE FOR USER ---
        cached_user = self.db.get_cached_user(username)
        if cached_user:
            print(f"📦 Found @{username} in Cache.")
            user_id = cached_user["user_id"]
        else:
            print(f"📡 @{username} not in cache. Fetching from X...")
            user = await self.client.get_user_by_screen_name(username)
            user_data = {
                "user_id": user.id,
                "username": user.screen_name,
                "name": user.name,
                "bio": user.description,
                "followers_count": user.followers_count
            }
            self.db.upsert_user(user_data)
            user_id = user.id

        # --- 2. FETCH TWEETS WITH DUPLICATE FILTERING ---
        print(f"📥 Scanning for new tweets for @{username}...")
        tweets_to_save = []
        
        # Initial Fetch
        fetched = await self.client.get_user_tweets(user_id, "Tweets", count=20)
        
        while fetched and len(tweets_to_save) < tweet_count:
            # Map Twikit objects to our dict format
            current_batch = []
            for t in fetched:
                current_batch.append({
                    "id": t.id,
                    "text": t.text,
                    "created_at": str(t.created_at),
                    "target_username": username
                })
            
            # CACHE CHECK: Filter out tweets we already have in Mongo
            new_tweets = self.db.filter_new_tweets(current_batch)
            
            if not new_tweets:
                print("🛑 All tweets in this batch are already cached. Stopping.")
                break
                
            tweets_to_save.extend(new_tweets)
            
            if len(tweets_to_save) >= tweet_count:
                break
                
            fetched = await fetched.next()
            await asyncio.sleep(3) # Human jitter

        # --- 3. PERSIST NEW DATA ---
        if tweets_to_save:
            print(f"💾 Saving {len(tweets_to_save)} new tweets to MongoDB.")
            self.db.save_tweets(tweets_to_save)
        
        return {
            "status": "Success",
            "new_items_collected": len(tweets_to_save),
            "cached_user": username
        }