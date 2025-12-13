from .snscrape_client import fetch_twitter_profile, fetch_tweets
from .storage_service import save_raw_data

async def collect_osint_data(username: str, platform: str):
    platform = platform.lower()

    if platform in ["twitter", "x"]:
        profile = fetch_twitter_profile(username)
        posts = fetch_tweets(username)

        combined = {
            "username": username,
            "platform": "twitter",
            "profile": profile,
            "posts": posts,
        }

        file_path = save_raw_data("twitter", username, combined)

        return {
            "status": "success",
            "file_saved": file_path,
            "profile_preview": profile,
            "post_count": len(posts)
        }

    else:
        return {"status": "error", "message": "Unsupported platform"}
